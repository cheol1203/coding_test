# SWEA 1213 🔎 String (Java)

## 느낀점
- 시작 위치별 문자 비교, 탐색 범위와 일치 여부 초기화 주의
- 굳이 첫 문자가 같아야 내부 로직을 시작하는 방식이 아닌 첫 글자부터 내부 로직을 시작하면 된다.
- 인덱스 범위를 더 효율적으로 작성해야한다
- 처음에 길이가 1인 경우를 생각하지 못했다.

## 흐름

1. 총 10개의 테스트케이스를 처리한다.
2. 테스트케이스 번호 `T`, 찾을 문자열 `str`, 검색할 문장 `sentence`를 입력받는다.
3. 검색어 전체가 들어갈 수 있는 시작 위치만 검사한다.
   - 시작 인덱스 범위는 `0 <= i <= sentence.length() - str.length()`이다.
4. 각 시작 위치에서 `boo = true`로 설정한다.
5. 검색어의 첫 글자부터 문장의 `i + j`번째 글자와 차례로 비교한다.
6. 다른 글자가 나오면 `boo = false`로 바꾸고 내부 반복문을 종료한다.
7. 끝까지 일치해 `boo`가 `true`이면 `count`를 증가시킨다.
8. 시작 위치를 한 칸씩 옮겨 모든 후보를 검사한 뒤 테스트케이스 번호와 개수를 출력한다.

## 작성 코드

기본 안내 주석과 주석 처리된 파일 입력 예시를 제외하고, 처음 오답 코드와 마지막 수정 코드를 함께 기록했다.

**처음 작성 코드 (오답)**

```java
import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int T = sc.nextInt();
            String str = sc.next();
            String sentence = sc.next();
            int count = 0;
            for(int i = 0 ; i<sentence.length(); i++) {
                boolean boo = false;
                if(sentence.charAt(i)==str.charAt(0)) {
                    for(int j = 1; j<str.length();j++) {
                        if(i+j < sentence.length()) {
                            if(str.charAt(j)!=sentence.charAt(i+j)) {
                                boo=false;
                                break;
                            }else {
                                boo=true;
                            }
                        }
                    }
                    if(boo) {
                        count++;
                        i+=str.length();
                    }
                }
            }
            System.out.println("#"+ T + " " + count);
        }
    }
}
```

**마지막 수정 코드**

```java
import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int T = sc.nextInt();
            String str = sc.next();
            String sentence = sc.next();
            int count = 0;
            for(int i = 0 ; i <= sentence.length() - str.length(); i++) {
                boolean boo = true;
                for(int j=0; j < str.length(); j++) {
                    if(sentence.charAt(i+j)!=str.charAt(j)) {
                        boo = false;
                        break;
                    }
                }
                if(boo) {
                    count++;
                }
            }
            System.out.println("#"+ T + " " + count);
        }
    }
}
```

## AI 코드 리뷰

### 개선할 점

- `boo`는 `matched`, `str`는 `keyword`, `T`는 `caseNumber`로 바꾸면 각 변수의 역할이 더 명확해진다.
- 문장 길이와 검색어 길이를 변수에 저장하면 반복문의 범위를 읽기 쉬워진다.
- 불일치를 발견한 즉시 `break`하는 마지막 코드는 남은 문자를 불필요하게 비교하지 않는다.
- 처음 코드의 `i += str.length()`는 바깥 반복문의 `i++`까지 더해져 다음 시작점을 건너뛰었다. 마지막 코드처럼 시작점을 한 칸씩 옮기면 연속해서 등장하거나 겹쳐 등장하는 경우를 검사할 수 있다.
- 처음 코드에서는 문장 끝에서 비교할 문자가 없어도 기존의 `true`가 남을 수 있었다. 시작 위치를 `문장 길이 - 검색어 길이`까지로 제한하면 검색어 전체를 비교할 수 있는 후보만 남는다.
- `matched = true`로 시작한 뒤 `j = 0`부터 비교하면 길이가 1인 검색어도 같은 로직으로 처리할 수 있다.
- 예를 들어 `ab`를 `ababab`에서 찾으면 3번이고, `aab`를 `aa`에서 찾으면 0번이며, `a`를 `aaa`에서 찾으면 3번이다.
- 문장 길이를 `N`, 검색어 길이를 `M`이라 할 때 검색의 최악 시간 복잡도는 `O(NM)`, 입력 문자열을 제외한 추가 공간 복잡도는 `O(1)`이다.
- 사용하지 않는 `FileInputStream` import는 개선 코드에서 제거했다.

첫 오답 코드의 검색 부분을 실행해 확인한 반례는 다음과 같다.

| 검색어 | 문장 | 기대 개수 | 첫 오답 코드 결과 | 원인 |
|---|---|---:|---:|---|
| `ab` | `ababab` | 3 | 2 | 검색 성공 후 다음 시작점을 건너뜀 |
| `aab` | `aa` | 0 | 1 | 문장 끝에서 남은 글자를 비교하지 않아도 `true`가 유지됨 |
| `a` | `aaa` | 3 | 0 | 내부 반복문이 실행되지 않아 `boo`가 `false`로 남음 |

### AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int testCase = 1; testCase <= 10; testCase++) {
            int caseNumber = sc.nextInt();
            String keyword = sc.next();
            String sentence = sc.next();
            int keywordLength = keyword.length();
            int sentenceLength = sentence.length();
            int count = 0;

            for (int start = 0; start <= sentenceLength - keywordLength; start++) {
                boolean matched = true;

                for (int offset = 0; offset < keywordLength; offset++) {
                    if (sentence.charAt(start + offset) != keyword.charAt(offset)) {
                        matched = false;
                        break;
                    }
                }

                if (matched) {
                    count++;
                }
            }

            System.out.println("#" + caseNumber + " " + count);
        }
    }
}
```
