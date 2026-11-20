"""Update only marked README statistics; --staged uses the Git index."""

import argparse
from collections import Counter
from html import escape
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


PLATFORMS = {"SWEA": "SWEA", "Programmers": "프로그래머스"}
CATEGORIES = {
    "Implementation": ("🛠️ 구현", "배열 · 시뮬레이션 · 조건 처리"),
    "Stack_Queue": ("📚 스택 / 큐", "괄호 · 인접 제거 · 순환 처리"),
    "BFS_DFS": ("🔍 BFS / DFS", "탐색 · 백트래킹"),
    "Brute_Force": ("🧮 완전탐색", "모든 후보와 조합 확인"),
    "DP": ("🧠 DP", "점화식 · 이전 결과 재사용"),
    "Greedy": ("⚡ 그리디", "선택 기준 · 상태 변화"),
    "String": ("🔤 문자열", "문자 비교 · 변환 · 검색"),
    "Sorting": ("↕️ 정렬", "정렬 후 순서 활용"),
}


def git(root, *args, data=None):
    result = subprocess.run(["git", *args], cwd=root, input=data, capture_output=True)
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def statistics(paths, readme):
    levels_by_path = {}
    for line in readme.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            continue
        link = re.search(r'(?:href="|\]\()(\./solutions/[^"\)]+)', cells[4])
        if link:
            levels_by_path[link[1].removeprefix("./")] = cells[1] or "미분류"

    platforms, levels, categories = Counter(), Counter(), Counter()
    for name in paths:
        path = PurePosixPath(name)
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9]*)_\d+_.+\.md", path.name)
        if not match:
            continue
        platform = PLATFORMS.get(match[1], match[1])
        platforms[platform] += 1
        levels[platform, levels_by_path.get(name, "미분류")] += 1
        categories[path.parts[1]] += 1
    return platforms, levels, categories


def render(readme, stats):
    platforms, levels, categories = stats
    total = sum(platforms.values())
    cards = [("📚 전체 풀이", total), ("🔷 SWEA", platforms["SWEA"]),
             ("🟣 프로그래머스", platforms["프로그래머스"])]
    cards.extend((source, count) for source, count in sorted(platforms.items())
                 if source not in PLATFORMS.values())
    summary = "<table>\n  <tr>\n"
    summary += "".join(f"    <th>{escape(label)}</th>\n" for label, _ in cards)
    summary += "  </tr>\n  <tr>\n"
    summary += "".join(f'    <td align="center"><strong>{count}문제</strong></td>\n'
                       for _, count in cards)
    summary += "  </tr>\n</table>"

    level_lines = ["| 출처 | 난이도 | 문제 수 |", "|:---|:---:|---:|"]
    source_order = {"SWEA": 0, "프로그래머스": 1}
    for (source, level), count in sorted(
            levels.items(), key=lambda item: (source_order.get(item[0][0], 2), item[0])):
        level_lines.append(f"| {source} | {level} | {count} |")
    level_lines.append(f"| **전체** | | **{total}** |")

    category_lines = ["| 분류 | 문제 수 | 연습 내용 |", "|:---|---:|:---|"]
    directories = [name for name in CATEGORIES if name in categories]
    directories += sorted(set(categories) - set(CATEGORIES))
    for directory in directories:
        label, description = CATEGORIES.get(directory, (directory, ""))
        category_lines.append(
            f"| [{label}](./solutions/{directory}) | {categories[directory]} | {description} |")
    category_lines.append(f"| **합계 · {len(categories)}개 분류** | **{total}** | |")

    newline = "\r\n" if "\r\n" in readme else "\n"
    blocks = {"summary": summary, "levels": "\n".join(level_lines),
              "categories": "\n".join(category_lines)}
    for section, content in blocks.items():
        start, end = f"<!-- stats:{section}:start -->", f"<!-- stats:{section}:end -->"
        if readme.count(start) != 1 or readme.count(end) != 1:
            raise ValueError(f"Missing or duplicate stats markers: {section}")
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
        replacement = start + newline + content.replace("\n", newline) + newline + end
        readme, count = pattern.subn(lambda _: replacement, readme)
        if count != 1:
            raise ValueError(f"Invalid stats markers: {section}")
    return readme


def update(root, staged=False):
    path = root / "README.md"
    working_bytes = path.read_bytes()
    working = working_bytes.decode("utf-8")
    if staged:
        entries = git(root, "ls-files", "--stage", "-z").decode("utf-8").split("\0")
        paths, readme_mode = [], None
        for entry in filter(None, entries):
            metadata, name = entry.split("\t", 1)
            mode, _, stage = metadata.split()
            if stage != "0":
                raise ValueError("Resolve merge conflicts before updating statistics.")
            if name == "README.md":
                readme_mode = mode
            if name.startswith("solutions/"):
                paths.append(name)
        if readme_mode is None:
            raise ValueError("Stage README.md before enabling its statistics hook.")
        indexed = git(root, "show", ":README.md").decode("utf-8")
        stats = statistics(paths, indexed)
        updated_index = render(indexed, stats)
    else:
        paths = [p.relative_to(root).as_posix() for p in (root / "solutions").rglob("*.md")]
        stats = statistics(paths, working)

    updated_working = render(working, stats).encode("utf-8")
    if path.read_bytes() != working_bytes:
        raise ValueError("README.md changed during the update; retry the command.")
    if staged and updated_index != indexed:
        blob = git(root, "hash-object", "-w", "--path=README.md", "--stdin",
                   data=updated_index.encode("utf-8")).decode("ascii").strip()
        git(root, "update-index", "--cacheinfo", readme_mode, blob, "README.md")
    if updated_working != working_bytes:
        path.write_bytes(updated_working)
    print(f"README statistics updated ({sum(stats[0].values())} problems).")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true", help="Count only files in the Git index")
    args = parser.parse_args()
    try:
        root = Path(git(Path.cwd(), "rev-parse", "--show-toplevel").decode("utf-8").strip())
        update(root, args.staged)
    except (OSError, ValueError) as error:
        print(f"README statistics: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
