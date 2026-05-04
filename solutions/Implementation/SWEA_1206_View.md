# SWEA 1206 🏙️ View (Java)

## 느낀점
>
- 첫 D3문제 치곤 쉬운?
- continue 랑 break 를 헷갈리는 어이없는 실수 발생

---

## 흐름
1. 테스트케이스는 총 10개이므로 `1`부터 `10`까지 반복
2. 건물 개수 `N` 입력
3. 건물 높이를 배열에 저장
4. 양쪽 2칸이 필요하므로 인덱스 `2`부터 `N - 3`까지 반복
5. 현재 건물이 주변 4개 건물보다 모두 높은지 확인
6. 높다면 주변 건물과의 차이 중 가장 작은 값을 조망권 세대 수에 더함
7. 최종 조망권 세대 수 출력

---

## 코드

```java
import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
        {
            int n = sc.nextInt();

            int[] arr = new int[n];

            for(int i = 0; i < arr.length; i++){
                arr[i] = sc.nextInt();
            }

            int sum = 0;

            for(int i = 2; i < arr.length - 2; i++){
                int diff = 1000;

                if(arr[i] - arr[i - 2] <= 0 ||
                   arr[i] - arr[i - 1] <= 0 ||
                   arr[i] - arr[i + 1] <= 0 ||
                   arr[i] - arr[i + 2] <= 0){
                    continue;
                }

                diff = Math.min(arr[i] - arr[i - 2], diff);
                diff = Math.min(arr[i] - arr[i - 1], diff);
                diff = Math.min(arr[i] - arr[i + 1], diff);
                diff = Math.min(arr[i] - arr[i + 2], diff);

                sum += diff;
            }

            System.out.println("#" + test_case + " " + sum);
        }
    }
}
```

## 질문 & 실수 정리

### 새로 배운 것

---

### 실수했던 부분

- continue를 써야하는데 break를 썼다.

---

## AI 코드 리뷰

### 좋았던 점

1. 반복 범위를 잘 잡음
   - 양쪽 2칸을 비교해야 하므로 `i = 2`부터 `arr.length - 2` 전까지 순회한 점이 좋다

2. 주변 4개 건물과 비교
   - `i - 2`, `i - 1`, `i + 1`, `i + 2`를 모두 확인해서 문제 조건을 잘 반영했다

3. 차이의 최솟값을 누적
   - 현재 건물이 주변 건물보다 모두 높을 때, 차이 중 최솟값을 더하는 방식은 올바른 접근이다

---

### 개선할 점

1. 주변 최댓값 방식 사용
   - `diff`를 여러 번 갱신하는 것보다 주변 건물 중 최댓값을 구하고 차이를 더하면 더 직관적이다

2. 변수명 개선
   - `arr` → `buildings`
   - `sum` → `viewCount`
   - `diff` → `view`

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int test_case = 1; test_case <= 10; test_case++) {
            int n = sc.nextInt();
            int[] buildings = new int[n];

            for (int i = 0; i < n; i++) {
                buildings[i] = sc.nextInt();
            }

            int viewCount = 0;

            for (int i = 2; i < n - 2; i++) {
                int maxAround = Math.max(
                    Math.max(buildings[i - 2], buildings[i - 1]),
                    Math.max(buildings[i + 1], buildings[i + 2])
                );

                if (buildings[i] > maxAround) {
                    viewCount += buildings[i] - maxAround;
                }
            }

            System.out.println("#" + test_case + " " + viewCount);
        }
    }
}
```