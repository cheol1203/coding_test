# SWEA 1209 ➕ Sum (Java)

## 느낀점
>
- 한번에 맞춘 문제

---

## 흐름
1. 테스트케이스는 총 10개이므로 10번 반복
2. 테스트케이스 번호 `t` 입력
3. `100 x 100` 배열 입력
4. 각 행의 합을 구하고 최댓값 갱신
5. 각 열의 합을 구하고 최댓값 갱신
6. 왼쪽 위 → 오른쪽 아래 대각선 합 계산
7. 오른쪽 위 → 왼쪽 아래 대각선 합 계산
8. 행, 열, 양쪽 대각선 합 중 최댓값 출력

---

## 코드

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
            int t = sc.nextInt();

            int[][] arr = new int[100][100];

            for(int i = 0; i < 100; i++) {
                for(int j = 0; j < 100; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int rowMax = 0;

            for(int i = 0; i < 100; i++) {
                int rowSum = 0;

                for(int j = 0; j < 100; j++) {
                    rowSum += arr[i][j];
                }

                if(rowSum > rowMax) {
                    rowMax = rowSum;
                }
            }

            int colMax = 0;

            for(int i = 0; i < 100; i++) {
                int colSum = 0;

                for(int j = 0; j < 100; j++) {
                    colSum += arr[j][i];
                }

                if(colSum > colMax) {
                    colMax = colSum;
                }
            }

            int leftCrossSum = 0;

            for(int i = 0; i < 100; i++) {
                leftCrossSum += arr[i][i];
            }

            int rightCrossSum = 0;

            for(int i = 0; i < 100; i++) {
                rightCrossSum += arr[i][99 - i];
            }

            int result = Math.max(rowMax, colMax);
            result = Math.max(result, leftCrossSum);
            result = Math.max(result, rightCrossSum);

            System.out.println("#" + t + " " + result);
        }
    }
}
```

## 질문 & 실수 정리

### 실수했던 부분

- 이번 코드는 큰 실수 없이 잘 작성했다
- 다만 `rowMax`, `colMax`, `leftCrossSum`, `rightCrossSum`을 따로 관리해서 코드가 조금 길어졌다
- 배열 크기 `100`이 여러 곳에 반복되므로 상수로 분리하면 가독성이 좋아질 수 있다

---

## AI 코드 리뷰

### 개선할 점

1. 최댓값 변수를 하나로 관리 가능
   - `rowMax`, `colMax`를 따로 두지 않고 `answer` 하나로 갱신할 수 있다

2. 행 합과 열 합을 한 반복문에서 동시에 계산 가능
   - 같은 `i`에 대해 `rowSum`, `colSum`을 동시에 구할 수 있다

3. 대각선 합도 배열 입력 중에 계산 가능
   - 다만 처음에는 지금처럼 분리해서 작성하는 것이 더 이해하기 쉽다

4. 상수 사용 가능
   - `100` 대신 `SIZE = 100`을 쓰면 의미가 명확해진다

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    static final int SIZE = 100;

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int test_case = 1; test_case <= 10; test_case++) {
            int caseNumber = sc.nextInt();
            int[][] arr = new int[SIZE][SIZE];

            for (int row = 0; row < SIZE; row++) {
                for (int col = 0; col < SIZE; col++) {
                    arr[row][col] = sc.nextInt();
                }
            }

            int answer = 0;
            int leftDiagonalSum = 0;
            int rightDiagonalSum = 0;

            for (int i = 0; i < SIZE; i++) {
                int rowSum = 0;
                int colSum = 0;

                for (int j = 0; j < SIZE; j++) {
                    rowSum += arr[i][j];
                    colSum += arr[j][i];
                }

                answer = Math.max(answer, rowSum);
                answer = Math.max(answer, colSum);

                leftDiagonalSum += arr[i][i];
                rightDiagonalSum += arr[i][SIZE - 1 - i];
            }

            answer = Math.max(answer, leftDiagonalSum);
            answer = Math.max(answer, rightDiagonalSum);

            System.out.println("#" + caseNumber + " " + answer);
        }
    }
}
```