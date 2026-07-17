# 프로그래머스 🔢 숫자의 표현 (Java)

## 풀이 방법
- i=1,2,3... 늘어나면서 n까지 더해서 sum==n이 되는 경우의 수를 찾음
- 시간복잡도가 O(n^2)이다. 투 포인터를 사용하면 O(n)으로 풀 수 있다.

### 제출 코드

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i = 1; i<=n; i++){
            int sum = 0;
            for(int j = i; j<=n; j++){
                sum += j;
                if(sum == n){
                    answer++;
                    break;
                }else if(sum > n){
                    break;
                }
            }
        }
        return answer;
    }
}
```

---

## 아쉬운 점

### 범위를 조금 줄일 수 있음

사실 `i`가 `n`일 때는 무조건 자기 자신 하나로 표현 가능하다.

그리고 `i`가 `n / 2`보다 커지면, `i + (i + 1)`은 이미 `n`을 넘는다.

그래서 최적화하려면 `i <= n / 2`까지만 확인하고, 마지막에 자기 자신 경우를 미리 하나 세도 된다.

---

## AI 개선 코드 : 투 포인터 풀이

연속된 자연수의 합 문제라서 투 포인터로도 풀 수 있다.

```java
class Solution {
    public int solution(int n) {
        int answer = 0;
        int start = 1;
        int end = 1;
        int sum = 1;

        while (start <= n) {
            if (sum == n) {
                answer++;
                sum -= start;
                start++;
            } else if (sum < n) {
                end++;
                sum += end;
            } else {
                sum -= start;
                start++;
            }
        }

        return answer;
    }
}
```