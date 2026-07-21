# 프로그래머스 🟫 카펫 (Java)

## 코드 리뷰
- width * height == brown + yellow
- (width - 2) * (height - 2) == yellow
- % 연산을 통해 약수를 구해서 풀기

### 제출 코드

```java
class Solution {
    public int[] solution(int brown, int yellow) {
        int height = 1;
        int size = brown + yellow;
        int width;
        
        while(true){
            if(size % height == 0){
                if((height-2) * (size / height -2) == yellow){
                    width = size / height;
                    break;
                }
            }
            height++;
        }
        
        return new int[]{width,height};
    }
}
```


---

## 아쉬운 점

### 1. `height = 1`부터 시작하면 의미 없는 후보도 검사함

카펫은 테두리 갈색이 있어야 하므로 최소 높이는 3 이상이어야 한다.

예를 들어 높이가 1이나 2면 안쪽 노란색 영역이 제대로 존재할 수 없다.

```text
height = 1 → height - 2 = -1
height = 2 → height - 2 = 0
```

그래서 더 자연스럽게는 `height = 3`부터 시작해도 된다.

```java
int height = 3;
```

다만 현재 코드도 정답을 찾는 데 문제는 없다.

---

### 2. `width`를 미리 계산하면 코드가 더 읽기 좋음

현재 코드:

```java
if((height-2) * (size / height -2) == yellow){
    width = size / height;
    break;
}
```

`size / height`가 반복해서 나오기 때문에, 약수일 때 `width`를 먼저 구하면 더 명확하다.

```java
int width = size / height;

if ((width - 2) * (height - 2) == yellow) {
    return new int[]{width, height};
}
```

---

### 3. `while(true)`보다 범위 있는 반복문이 더 안전함

현재 문제에서는 반드시 답이 존재하므로 `while(true)`도 가능하다.

하지만 일반적으로는 범위를 정한 `for`문이 더 안전하고 읽기 좋다.

```java
for (int height = 3; height <= size; height++) {
    ...
}
```

더 최적화하면 세로는 전체 넓이의 제곱근까지만 확인해도 된다.

---

## AI 개선 코드

```java
class Solution {
    public int[] solution(int brown, int yellow) {
        int size = brown + yellow;

        for (int height = 3; height <= size; height++) {
            if (size % height != 0) {
                continue;
            }

            int width = size / height;

            if ((width - 2) * (height - 2) == yellow) {
                return new int[]{width, height};
            }
        }

        return new int[0];
    }
}
```

---

## 더 깔끔한 개선 코드

가로가 세로보다 크거나 같으므로, `height <= width`인 경우까지만 보면 된다.

```java
class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;

        for (int height = 3; height <= Math.sqrt(total); height++) {
            if (total % height != 0) {
                continue;
            }

            int width = total / height;

            if ((width - 2) * (height - 2) == yellow) {
                return new int[]{width, height};
            }
        }

        return new int[0];
    }
}
```