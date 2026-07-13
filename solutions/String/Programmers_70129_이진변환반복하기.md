# 프로그래머스 🔁 이진 변환 반복하기 (Java)

## 코드 흐름

```text
0의 개수 → 제거한 0의 개수에 누적
1의 개수 → 0 제거 후 남은 문자열의 길이
그 길이를 이진수로 변환
```

## 새로 배운 것
- int 정수를 Integer.toBinaryString 함수를 사용하면 문자열형태의 이진수를 얻을 수 있다

### 제출 코드

```java
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while(!s.equals("1")){
            int oneCount=0;
            for(int i = 0; i< s.length(); i++){
                if(s.charAt(i)=='0'){
                    answer[1]++;
                }else{
                    oneCount++;
                }
            }
            StringBuilder sb = new StringBuilder();
            for(int i = 0 ; i<oneCount; i++){
                sb.append('1');
            }
            String a = sb.toString();
            s = Integer.toBinaryString(a.length());
            answer[0]++;
        }
        
        
        return answer;
    }
}
```
---

## 개선할점
- StringBuilder로 1을 다시 만들 필요가 없음

## 개선 코드

```java
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];

        while (!s.equals("1")) {
            int oneCount = 0;

            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    answer[1]++;
                } else {
                    oneCount++;
                }
            }

            s = Integer.toBinaryString(oneCount);
            answer[0]++;
        }

        return answer;
    }
}
```