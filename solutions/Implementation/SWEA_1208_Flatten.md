# SWEA 1208 📦 Flatten (Java)

## 느낀점
>
- 1회 오답
- max, min 굳이 구하지 않고 인덱스 값만 구해도 된다.

---

## 흐름
1. 테스트케이스는 총 10개이므로 10번 반복
2. dump 횟수 입력
3. 상자 높이 100개 입력
4. dump 횟수만큼 반복
5. 매번 배열 전체를 돌면서 최댓값 위치와 최솟값 위치 찾기
6. 최댓값 위치의 높이는 1 감소
7. 최솟값 위치의 높이는 1 증가
8. 모든 dump가 끝난 뒤 최댓값과 최솟값을 다시 찾기
9. `최댓값 - 최솟값` 출력

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
            int dump = sc.nextInt();
            int[] arr = new int[100];

            for(int i = 0; i < arr.length; i++) {
                arr[i] = sc.nextInt();
            }

            for(int i = 1; i <= dump; i++) {
                int max = 0;
                int min = 101;
                int maxIndex = -1;
                int minIndex = -1;

                for(int j = 0; j < arr.length; j++) {
                    if(arr[j] > max) {
                        max = arr[j];
                        maxIndex = j;
                    }

                    if(arr[j] < min) {
                        min = arr[j];
                        minIndex = j;
                    }
                }

                arr[maxIndex] -= 1;
                arr[minIndex] += 1;
            }

            int max = 0;
            int min = 101;

            for(int i = 0; i < arr.length; i++) {
                if(arr[i] > max) {
                    max = arr[i];
                }

                if(arr[i] < min) {
                    min = arr[i];
                }
            }

            int heightDiff = max - min;

            System.out.println("#" + test_case + " " + heightDiff);
        }
    }
}
```
## 질문 & 실수 정리


### 실수했던 부분

- 마지막 dump에서 사용한 `maxIndex`, `minIndex`로 바로 높이 차이를 계산했다
  - 하지만 이 인덱스는 dump 하기 전의 최댓값/최솟값 위치다
  - dump 이후에는 다른 위치가 최댓값이나 최솟값이 될 수 있다
- `heightDiff = arr[maxIndex] - arr[minIndex]` 방식은 최종 상태의 진짜 최댓값/최솟값 차이가 아닐 수 있다
- 따라서 dump가 모두 끝난 뒤 배열을 다시 순회하면서 최댓값과 최솟값을 구해야 한다

---

## AI 코드 리뷰


### 개선할 점

1. 최종 차이 계산 위치 수정
   - dump 도중 마지막 인덱스로 계산하지 말고, dump가 끝난 뒤 다시 최댓값과 최솟값을 구해야 한다

2. 변수명 개선
   - `arr` → `boxes`
   - `dump` → `dumpCount`
   - `heightDiff` → `answer`
   - `maxIndex`, `minIndex`는 의미가 명확해서 좋다

3. 중복 로직 함수화 가능
   - 최댓값 인덱스 찾기와 최솟값 인덱스 찾기를 메서드로 분리하면 가독성이 좋아진다

4. 조기 종료 가능
   - 최댓값과 최솟값의 차이가 `0` 또는 `1`이면 더 이상 평탄화해도 차이가 줄어들지 않으므로 멈출 수 있다

---

## AI 개선 코드

```java
import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int test_case = 1; test_case <= 10; test_case++) {
            int dumpCount = sc.nextInt();
            int[] boxes = new int[100];

            for (int i = 0; i < boxes.length; i++) {
                boxes[i] = sc.nextInt();
            }

            for (int i = 0; i < dumpCount; i++) {
                int maxIndex = findMaxIndex(boxes);
                int minIndex = findMinIndex(boxes);

                if (boxes[maxIndex] - boxes[minIndex] <= 1) {
                    break;
                }

                boxes[maxIndex]--;
                boxes[minIndex]++;
            }

            int maxIndex = findMaxIndex(boxes);
            int minIndex = findMinIndex(boxes);
            int answer = boxes[maxIndex] - boxes[minIndex];

            System.out.println("#" + test_case + " " + answer);
        }
    }

    static int findMaxIndex(int[] boxes) {
        int maxIndex = 0;

        for (int i = 1; i < boxes.length; i++) {
            if (boxes[i] > boxes[maxIndex]) {
                maxIndex = i;
            }
        }

        return maxIndex;
    }

    static int findMinIndex(int[] boxes) {
        int minIndex = 0;

        for (int i = 1; i < boxes.length; i++) {
            if (boxes[i] < boxes[minIndex]) {
                minIndex = i;
            }
        }

        return minIndex;
    }
}
```
