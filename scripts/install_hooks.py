"""Install the repository's README statistics hook without replacing other hooks."""

import os
from pathlib import Path
import shlex
import subprocess
import sys


SIGNATURE = "# algorithm-readme-stats-hook"


def main():
    try:
        root = Path(subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], encoding="utf-8").strip())
        hook = Path(subprocess.check_output(
            ["git", "rev-parse", "--git-path", "hooks/pre-commit"],
            cwd=root, encoding="utf-8").strip())
        if not hook.is_absolute():
            hook = root / hook
        if hook.exists() and SIGNATURE not in hook.read_text(encoding="utf-8"):
            raise ValueError("An existing pre-commit hook was preserved; install manually.")
        python = shlex.quote(Path(sys.executable).as_posix())
        content = (f"#!/bin/sh\n{SIGNATURE}\n"
                   f"exec {python} scripts/update_readme_stats.py --staged\n")
        hook.parent.mkdir(parents=True, exist_ok=True)
        hook.write_text(content, encoding="utf-8", newline="\n")
        os.chmod(hook, 0o755)
        print("Installed the README statistics pre-commit hook.")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Hook installation: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
