# SWEA 3282 🎒 0/1 Knapsack (Java)

## 느낀점
>
- 물건을 안 넣는 경우와 넣을 경우를 비교하여 dp배열 갱신
- 처음에는 5215번처럼 DFS 선택/비선택 구조로 풀려고 했다
- 하지만 3282번은 물건 개수가 커질 수 있어서 DFS로 풀면 시간 초과가 날 수 있었다
- 0/1 Knapsack은 `dp[용량] = 해당 용량에서 만들 수 있는 최대 가치`로 생각하면 된다
- 같은 물건을 여러 번 사용하지 않기 위해 DP 배열을 뒤에서부터 갱신해야 한다는 점이 핵심이었다

---

## 흐름
1. 테스트케이스 개수 `T` 입력
2. 물건 개수 `N`, 가방 부피 제한 `K` 입력
3. `dp` 배열을 `K + 1` 크기로 생성
4. 각 물건의 부피 `v`, 가치 `c` 입력
5. 현재 물건을 넣을 수 있는 용량부터 뒤에서 앞으로 순회
6. 현재 물건을 넣지 않는 경우와 넣는 경우 중 더 큰 값으로 갱신
7. 최종적으로 `dp[K]` 출력

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
            int n = sc.nextInt();
            int k = sc.nextInt();

            int[] dp = new int[k + 1];

            for(int i = 0; i < n; i++) {
                int v = sc.nextInt();
                int c = sc.nextInt();

                for(int j = k; j >= v; j--) {
                    dp[j] = Math.max(dp[j], dp[j - v] + c);
                }
            }

            System.out.println("#" + test_case + " " + dp[k]);
        }
    }
}
```
## 질문 & 실수 정리

### 새로 배운 것

- 0/1 Knapsack은 각 물건을 한 번만 선택할 수 있는 배낭 문제다
- `dp[j]`는 부피 제한이 `j`일 때 만들 수 있는 최대 가치를 의미한다
- 현재 물건을 넣는 경우는 `dp[j - v] + c`로 계산한다
- 현재 물건을 넣지 않는 경우는 기존 `dp[j]` 값이다
- 따라서 점화식은 `dp[j] = Math.max(dp[j], dp[j - v] + c)`이다
- 0/1 Knapsack에서는 같은 물건을 여러 번 사용하지 않기 위해 뒤에서부터 순회해야 한다

---

### 실수했던 부분

- 처음에는 DFS로 풀려고 했다
    - 구조는 맞지만 경우의 수가 `2^N`이라 시간 초과 가능성이 크다
    - 3282번은 DP로 푸는 것이 적합하다

- 처음 DFS 코드에서는 `v`, `c` 배열을 지역변수로 선언했다
    - 그러면 DFS에서 사용하는 static 배열은 초기화되지 않는다
    - 이후 `v = new int[n]`, `c = new int[n]`으로 수정했다

- DP 코드에서 처음에는 `dp[k - v] + c`를 사용했다
    - 하지만 현재 확인 중인 용량은 `j`이므로 `dp[j - v] + c`가 맞다
    - `k`는 전체 최대 용량이고, `j`는 현재 갱신 중인 용량이다

- 앞에서부터 순회하면 같은 물건을 여러 번 사용하는 문제가 생긴다
    - 따라서 `for(int j = k; j >= v; j--)`처럼 뒤에서부터 순회해야 한다

---

## AI 코드 리뷰

### 개선할 점

1. 변수명 개선
    - `n` → `itemCount`
    - `k` → `limit`
    - `v` → `volume`
    - `c` → `value`
    - `j` → `capacity`

2. 문제 복습용으로는 주석 추가 추천
    - DP 의미와 뒤에서부터 도는 이유를 주석으로 남기면 나중에 다시 볼 때 이해하기 쉽다

3. 2차원 DP도 알아두면 좋음
    - 최대 가치만 필요하면 1차원 DP가 좋다
    - 어떤 물건을 골랐는지까지 추적해야 하면 2차원 DP가 더 편하다

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int itemCount = sc.nextInt();
            int limit = sc.nextInt();

            int[] dp = new int[limit + 1];

            for (int i = 0; i < itemCount; i++) {
                int volume = sc.nextInt();
                int value = sc.nextInt();

                for (int capacity = limit; capacity >= volume; capacity--) {
                    dp[capacity] = Math.max(
                        dp[capacity],
                        dp[capacity - volume] + value
                    );
                }
            }

            System.out.println("#" + test_case + " " + dp[limit]);
        }
    }
}
```
