# 프로그래머스 ✅ 올바른 괄호 (Java)

## 느낀점
>
- `'('`이 나오면 push `')'`이 나오면 검증 후 pop, deque가 비어있으면 true, 비어있지 않다면 false

---

## 흐름

1. 문자열을 앞에서부터 한 글자씩 확인한다
2. `'('`가 나오면 스택에 넣는다
3. `')'`가 나오면 스택에서 `'('` 하나를 제거한다
4. 만약 `')'`가 나왔는데 스택이 비어 있다면 올바른 괄호가 아니므로 `false`
5. 모든 문자를 확인한 뒤 스택이 비어 있으면 `true`
6. 스택에 `'('`가 남아 있으면 `false`

---

## 코드

```java
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Deque<Character> deque = new ArrayDeque<>();
        char[] arr = s.toCharArray();
        
        for(int i = 0 ; i < arr.length ; i++){
            if(arr[i] == '('){
                deque.push(arr[i]);
            } else {
                if(deque.isEmpty() || deque.peek() == ')'){
                    deque.push(arr[i]);
                } else if(deque.peek() == '('){
                    deque.pop();
                }
            }
        }

        return deque.isEmpty();
    }
}
```

---

## 질문 & 실수 정리

### 실수했던 부분

- `')'`를 스택에 넣는 방식으로 풀어서 코드가 조금 복잡해졌다
- `deque.peek() == ')'` 조건은 이 문제에서는 굳이 필요하지 않다
- `')'`가 나왔는데 스택이 비어 있다면 그 순간 바로 `false`를 반환해도 된다

---

## AI 코드 리뷰

### 개선할 점

1. `')'`는 스택에 넣지 않아도 된다

- 현재 코드는 짝이 맞지 않는 `')'`도 스택에 넣는다. 하지만 보통은 `')'`가 나왔는데 스택이 비어 있으면 바로 `false`를 반환한다.


2. 스택에는 `'('`만 저장하는 방식이 더 깔끔하다

---

## AI 개선 코드

```java
import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (current == '(') {
                stack.push(current);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }

                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}
```