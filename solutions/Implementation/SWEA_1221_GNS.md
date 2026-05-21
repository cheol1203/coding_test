# SWEA 1221 🔢 GNS (Java)

## 느낀점
>
- AI 풀이 참고한 문제, 다시 풀어보자!
- map 자료구조를 활용해 풀면 더 효율적인 코드를 작성할 수 있다!
- `ZRO`, `ONE`, `TWO` 같은 문자열마다 순서가 정해져 있으므로 카운팅 배열을 사용하면 쉽게 풀 수 있었다
- 입력받은 문자열이 어떤 숫자인지 찾아서 해당 인덱스의 개수를 증가시키는 방식으로 해결했다
- 정렬을 직접 하지 않고, 정해진 순서 배열을 기준으로 개수만큼 출력하는 방식이 효율적이었다

---

## 흐름
1. 테스트케이스 개수 `T` 입력
2. 테스트케이스 번호 문자열 `t`와 숫자 개수 `length` 입력
3. 외계어 숫자의 정해진 순서를 배열에 저장
4. 숫자 개수를 셀 `quantity` 배열 생성
5. 입력받은 외계어 숫자가 순서 배열의 몇 번째 값인지 찾기
6. 해당 위치의 개수 증가
7. `ZRO`부터 `NIN`까지 정해진 순서대로 개수만큼 출력

---

## 코드

```java
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            String t = sc.next();
            int length = sc.nextInt();

            String[] number = {
                "ZRO", "ONE", "TWO", "THR", "FOR",
                "FIV", "SIX", "SVN", "EGT", "NIN"
            };

            int[] quantity = new int[10];

            for(int i = 0; i < length; i++) {
                String num = sc.next();

                for(int j = 0; j < 10; j++) {
                    if(num.equals(number[j])) {
                        quantity[j]++;
                    }
                }
            }

            System.out.println(t);

            for(int i = 0; i < 10; i++) {
                for(int j = 0; j < quantity[i]; j++) {
                    System.out.print(number[i] + " ");
                }
            }

            System.out.println();
        }
    }
}

```

## 코드(map 활용)

```java
import java.util.Map;
import java.util.Scanner;
import java.util.HashMap;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            String t = sc.next();
            int length = sc.nextInt();

            String[] number = {
                "ZRO", "ONE", "TWO", "THR", "FOR",
                "FIV", "SIX", "SVN", "EGT", "NIN"
            };

            int[] quantity = new int[10];

            Map<String,Integer> map = new HashMap<>();

            for(int i = 0; i < 10; i++) {
                map.put(number[i], i);
            }

            for(int i = 0; i < length; i++) {
                String num = sc.next();

                int count = map.get(num);
                quantity[count]++;
            }

            System.out.println(t);

            for(int i = 0; i < 10; i++) {
                for(int j = 0; j < quantity[i]; j++) {
                    System.out.print(number[i] + " ");
                }
            }

            System.out.println();
        }
    }
}
```

## 질문 & 실수 정리

### 새로 배운 것

- `Map`은 key와 value를 쌍으로 저장하는 자료구조다
- `Map<String, Integer>`를 사용하면 문자열을 숫자 인덱스로 바꿀 수 있다
- `map.put(key, value)`로 값을 저장한다
- `map.get(key)`로 key에 해당하는 value를 가져올 수 있다
- 이 문제에서는 `"ZRO" → 0`, `"ONE" → 1`처럼 외계어 숫자와 순서를 매핑했다
- 문자열에 정해진 순서가 있을 때 `Map`을 사용하면 인덱스를 빠르게 찾을 수 있다


---

## AI 코드 리뷰


### 개선할 점

1. 찾은 뒤 `break` 추가
    - 문자열이 일치하는 인덱스를 찾았으면 더 이상 나머지 숫자와 비교할 필요가 없다

2. 변수명 개선
    - `number` → `numbers` 또는 `gnsNumbers`
    - `quantity` → `count`
    - `num` → `word`

3. `StringBuilder` 사용
    - 출력 문자열을 한 번에 만들면 코드가 더 깔끔하고 출력 성능도 좋아진다

4. `number` 배열 위치 이동
    - 매 테스트케이스마다 새로 만들 필요 없이, 반복문 밖에서 한 번만 만들어도 된다

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    static final String[] GNS_NUMBERS = {
        "ZRO", "ONE", "TWO", "THR", "FOR",
        "FIV", "SIX", "SVN", "EGT", "NIN"
    };

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            String caseNumber = sc.next();
            int length = sc.nextInt();

            int[] count = new int[10];

            for (int i = 0; i < length; i++) {
                String word = sc.next();

                for (int j = 0; j < GNS_NUMBERS.length; j++) {
                    if (word.equals(GNS_NUMBERS[j])) {
                        count[j]++;
                        break;
                    }
                }
            }

            StringBuilder answer = new StringBuilder();
            answer.append(caseNumber).append("\n");

            for (int i = 0; i < GNS_NUMBERS.length; i++) {
                for (int j = 0; j < count[i]; j++) {
                    answer.append(GNS_NUMBERS[i]).append(" ");
                }
            }

            System.out.println(answer);
        }
    }
}
```
