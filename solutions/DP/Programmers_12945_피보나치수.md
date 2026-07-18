# 프로그래머스 🔢 피보나치 수 (Java)

## 정리
- DP는 점화식을 세우는게 중요하다!
- 피보나치 수는 수가 매우 커질 수 있으므로 마지막에 한번만 나누는게 아닌 나눈 값을 arr[i]에 저장해야한다.

### 제출 코드 (오답)

```java
class Solution {
    public int solution(int n) {
        
        int [] arr = new int[n+1];
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 2; i<=n; i++){
            arr[i] = arr[i-1] + arr[i-2];
        }
        return arr[n] % 1234567;
    }
}
```

---

## 수정 코드

```java
class Solution {
    public int solution(int n) {
        int[] arr = new int[n + 1];

        arr[0] = 0;
        arr[1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
        }

        return arr[n];
    }
}
```