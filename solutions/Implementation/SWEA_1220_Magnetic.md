# SWEA 1220 🧲 Magnetic (Java)

## 느낀점
>
- 처음에는 자성체를 직접 한 칸씩 움직이는 시뮬레이션으로 풀려고 했는데, 문제를 단순하게 볼 필요가 있었다
- 실제 이동 과정을 구현하지 않아도, 각 열에서 `1 → 2` 형태가 몇 번 나오는지만 세면 된다는 점이 핵심이었다
- 상태를 하나 기억하는 `boolean` 변수를 사용하면 깔끔하게 해결할 수 있었다

---

## 흐름
1. 테스트케이스는 총 10개이므로 10번 반복
2. 배열 크기 `n` 입력
3. `n x n` 자성체 배열 입력
4. 각 열을 위에서 아래로 탐색
5. `1`을 만나면 `pair = true`로 표시
6. 그 이후 `2`를 만나면 교착 상태가 1개 생긴 것이므로 `count++`
7. 하나의 교착 상태를 센 뒤에는 다시 `pair = false`
8. 모든 열 탐색 후 교착 상태 개수 출력

---

## 코드

```java
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = 10;

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int n = sc.nextInt();
            int[][] arr = new int[n][n];

            for(int i = 0 ; i < n; i++) {
                for(int j = 0 ; j < n; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int count = 0;

            for(int i = 0 ; i < n; i++) {
                boolean pair = false;

                for(int j = 0 ; j < n; j++) {
                    if(arr[j][i] == 1) {
                        pair = true;
                    } else if(arr[j][i] == 2 && pair == true) {
                        pair = false;
                        count++;
                    }
                }
            }

            System.out.println("#" + test_case + " " + count);
        }
    }
}
```
## 질문 & 실수 정리

### 실수했던 부분

- 처음에는 자성체를 직접 이동시키는 방식으로 접근했다
  - 이 방식은 인덱스 에러가 나기 쉽고 구현도 복잡하다
  - 하지만 문제는 최종 교착 상태 개수만 세면 된다

- 변수명 `pair`는 동작은 맞지만 의미가 조금 애매할 수 있다
  - `hasN`, `seenN`, `isMatchedReady` 같은 이름이 더 직관적일 수 있다

- `pair == true`는 줄여서 그냥 `pair`라고 써도 된다

---

## AI 코드 리뷰

### 개선할 점

1. 변수명 개선
   - `arr` → `board`
   - `pair` → `hasN`
   - `count`는 그대로 써도 괜찮다

2. 조건문 간소화
   - `pair == true` 대신 `pair`로 써도 된다

3. 반복문 변수명 개선
   - `i`, `j`도 가능하지만 `col`, `row`처럼 쓰면 세로 탐색이라는 의미가 더 분명해진다

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            int n = sc.nextInt();
            int[][] board = new int[n][n];

            for (int row = 0; row < n; row++) {
                for (int col = 0; col < n; col++) {
                    board[row][col] = sc.nextInt();
                }
            }

            int count = 0;

            for (int col = 0; col < n; col++) {
                boolean hasN = false;

                for (int row = 0; row < n; row++) {
                    if (board[row][col] == 1) {
                        hasN = true;
                    } else if (board[row][col] == 2 && hasN) {
                        count++;
                        hasN = false;
                    }
                }
            }

            System.out.println("#" + test_case + " " + count);
        }
    }
}
```
