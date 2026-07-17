# 프로그래머스 🔢 다음 큰 숫자 (Java)

## 풀이 방법
- 정수 n을 이진수로 바꾼뒤, 1의 개수를 샌다.
- 다음 번호를 하나씩 늘려가며 1의 개수가 같으면 그 값을 반환시킨다.

### 제출 코드

```java
class Solution {
    public int solution(int n) {
        String nBinary = Integer.toBinaryString(n);
        int nOneCount = 0;
        
        for(int i = 0 ; i<nBinary.length(); i++){
            if(nBinary.charAt(i)=='1'){
                nOneCount++;
            }
        }
        
        int nextNum = n+1;
        while(true){
            String nextNumBinary = Integer.toBinaryString(nextNum);
            int nextNumOneCount = 0;
            for(int i = 0 ; i<nextNumBinary.length(); i++){
                if(nextNumBinary.charAt(i)=='1'){
                    nextNumOneCount++;
                }
            }
            if(nextNumOneCount == nOneCount){
                break;
            }
            nextNum++;
        }
        return nextNum;
    }
}
```

---

## AI 개선 코드 : `Integer.bitCount()` 사용

```java
class Solution {
    public int solution(int n) {
        int nOneCount = Integer.bitCount(n);
        int nextNum = n + 1;

        while (Integer.bitCount(nextNum) != nOneCount) {
            nextNum++;
        }

        return nextNum;
    }
}
```