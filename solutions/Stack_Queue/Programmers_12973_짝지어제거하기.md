# 프로그래머스 🧹 짝지어 제거하기 (Java)

## 코드 리뷰
- 올바른 괄호 문제와 거의 똑같은 문제

### 제출 코드

```java
import java.util.Deque;
import java.util.ArrayDeque;

class Solution
{
    public int solution(String s)
    {
        Deque<Character> deque = new ArrayDeque<>();
        char[] arr = s.toCharArray();
        for(int i = 0 ; i<arr.length; i++){
            if(deque.isEmpty() || deque.peek() != arr[i]){
                deque.push(arr[i]);
            }else{
                deque.pop();
            }
        }
        
        if(deque.isEmpty()){
            return 1;
        }else{
            return 0;
        }
    }
}
```
---

## 개선할 점

- 마지막 return은 삼항 연산자로 줄일 수 있음

- `toCharArray()` 없이 `charAt()`을 써도 됨

---

## AI 개선 코드

```java
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (!stack.isEmpty() && stack.peek() == current) {
                stack.pop();
            } else {
                stack.push(current);
            }
        }

        return stack.isEmpty() ? 1 : 0;
    }
}
```