# 프로그래머스 🔢 최솟값 만들기 (Java)
## 풀이 흐름
- A배열과 B배열을 정렬 후 가장 작은 값은 가장 큰 값과, 두번째로 작은값은 두번째로 큰 값과 곱한다.

## 실수한 점
- 처음에 DFS로 접근을 시도하였으나 너무 복잡하다
- Collections.reverseOrder()의 대상 배열은 int[]가 아닌 Integer[]이어야 한다.
- 역정렬을 사용하지 않고 그냥 인덱스 끝에서부터 접근하여 해결할 수도 있다.

## 제출 코드

```java
import java.util.Arrays;
import java.util.Collections;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        Integer[] arr = new Integer[B.length];
        for(int i = 0; i<B.length; i++){
            arr[i] = Integer.valueOf(B[i]);
        }
        Arrays.sort(A);
        Arrays.sort(arr,Collections.reverseOrder());
        
        for(int i = 0 ; i<A.length ; i++){
            answer += A[i] * arr[i];
        }

        return answer;
    }
}
```

---

## AI 개선 코드

```java
import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;

        Arrays.sort(A);
        Arrays.sort(B);

        for (int i = 0; i < A.length; i++) {
            answer += A[i] * B[B.length - 1 - i];
        }

        return answer;
    }
}
```