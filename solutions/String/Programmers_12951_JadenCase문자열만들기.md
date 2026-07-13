# 프로그래머스 🔤 JadenCase 문자열 만들기 (Java)

## 새롭게 배운점
- Character.toUpperCase() 함수로 String의 일부분만 대 or 소문자로 바꿀 수 있다.
- 문자열을 char 배열로 바꿀때는 toCharArray(), char 배열을 문자열로 바꿀때는 String.valueOf();
- 문자열을 쪼갤때는 s.split(), 다시 합칠때는 String.join(parameter, 배열)

### 첫 제출 코드(오답)

```java
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        for(int i = 0 ; i<arr.length; i++){
            char[] arr2 = arr[i].toCharArray();
            for(int j = 0; j<arr2.length; j++){
                if(j==0){
                    arr2[j]=Character.toUpperCase(arr2[j]);
                }else{
                    arr2[j]=Character.toLowerCase(arr2[j]);
                }
            }
            arr[i] = String.valueOf(arr2);
        }
        answer = String.join(" ", arr);
        return answer;
    }
}
```
---
## 개선할 점
- 첫 코드의 split은 공백이 여러번 걸쳐 나올때 제대로 처리하지 못한다.
- split은 마지막 공백을 그냥 삭제해버린다
- 따라서, split을 사용하기보다 전체 문자열을 차례대로 하나씩 보면서 정답에 추가하는 방식이 더 효율적이다.

---

## AI 개선 코드

```java
class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        boolean isFirst = true;

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (current == ' ') {
                answer.append(current);
                isFirst = true;
            } else {
                if (isFirst) {
                    answer.append(Character.toUpperCase(current));
                    isFirst = false;
                } else {
                    answer.append(Character.toLowerCase(current));
                }
            }
        }

        return answer.toString();
    }
}
```

---

## 개선 코드 흐름

```text
1. 문자열을 앞에서부터 한 글자씩 확인한다
2. 공백이면 그대로 추가한다
3. 공백 다음 문자는 단어의 첫 글자이므로 isFirst를 true로 바꾼다
4. 공백이 아닌 문자가 나왔을 때 isFirst가 true면 대문자로 바꾼다
5. isFirst가 false면 소문자로 바꾼다
6. 모든 문자를 처리한 뒤 결과 문자열을 반환한다
```