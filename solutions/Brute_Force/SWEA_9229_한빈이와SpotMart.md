# SWEA 9229 🍪 한빈이와 Spot Mart (Java)

## 느낀점

- 서로 다른 두 봉지의 조합을 모두 확인하고, 무게 제한 이하인 합 중 최댓값을 구한다. 가능한 조합이 없으면 -1을 유지한다.
- 쉽게 풀었다

## 흐름

1. 테스트케이스 개수 `T`, 과자 봉지 개수 `N`, 무게 제한 `M`을 입력받는다.
2. 각 과자 봉지의 무게를 배열 `arr`에 저장한다.
3. 정답 `total`을 `-1`로 초기화한다.
4. 첫 번째 봉지를 인덱스 `i`로 선택하고, 두 번째 봉지는 `j = i + 1`부터 선택한다.
   - 같은 봉지를 두 번 고르지 않고, 두 봉지의 순서만 바뀐 중복 조합도 제외한다.
5. 두 봉지의 무게 합이 `M` 이하이면 `Math.max()`로 정답을 갱신한다.
6. 모든 조합을 확인한 뒤 테스트케이스 번호와 정답을 출력한다. 조건을 만족하는 조합이 없으면 초기값 `-1`이 출력된다.

## 작성 코드

기본 안내 주석과 주석 처리된 파일 입력 예시를 제외한 작성 코드이다.

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
            int N = sc.nextInt();
            int M = sc.nextInt();

            int[] arr = new int[N];

            for(int i = 0 ; i< arr.length; i++) {
                arr[i] = sc.nextInt();
            }

            int total = -1;
            for(int i = 0; i < arr.length; i++) {
                for(int j = i+1; j < arr.length; j++) {
                    if(arr[i] + arr[j] <= M) {
                        total = Math.max(total, arr[i] + arr[j]);
                    }
                }
            }

            System.out.println("#" + test_case + " " + total);
        }
    }
}
```

## AI 코드 리뷰

### 개선할 점

- `j = i + 1`부터 탐색해 서로 다른 두 봉지만 선택하고 중복 조합을 제외한 점이 적절하다.
- `<= M`으로 무게 제한과 같은 경우도 포함하고, 정답을 `-1`로 초기화해 가능한 조합이 없는 경우를 별도 변수 없이 처리했다.
- `arr[i] + arr[j]`를 `sum` 변수에 한 번 저장하면 조건 검사와 최댓값 갱신에서 재사용할 수 있다.
- `arr`는 `weights`, `N`은 `snackCount`, `M`은 `limit`, `total`은 `answer`로 바꾸면 각 변수의 의미가 명확해진다.
- 첫 번째 봉지의 반복 범위를 `i < snackCount - 1`로 정하면 두 번째 봉지를 선택할 수 없는 마지막 인덱스는 생략할 수 있다.
- 작성 코드와 개선 코드 모두 시간 복잡도는 `O(N²)`, 배열 저장 공간은 `O(N)`이다. 아래 개선 코드는 기존 완전탐색 방식을 유지하며 표현을 정리한 예시이다.

### AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCount = sc.nextInt();

        for (int testCase = 1; testCase <= testCount; testCase++) {
            int snackCount = sc.nextInt();
            int limit = sc.nextInt();
            int[] weights = new int[snackCount];

            for (int i = 0; i < snackCount; i++) {
                weights[i] = sc.nextInt();
            }

            int answer = -1;

            for (int first = 0; first < snackCount - 1; first++) {
                for (int second = first + 1; second < snackCount; second++) {
                    int sum = weights[first] + weights[second];

                    if (sum <= limit) {
                        answer = Math.max(answer, sum);
                    }
                }
            }

            System.out.println("#" + testCase + " " + answer);
        }
    }
}
```
