# 프로그래머스 🍊 귤 고르기

## 풀이 흐름
- 크기별 개수를 세고 가장 개수가 많은 크기부터 골라서 k에서 빼간다.

## 1차 제출 코드(오답)

```java
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int[] countArray = new int[10000001];
        for(int i : tangerine){
            countArray[i]++;
        }

        while(true){
            int max = -1;
            for(int i : countArray){
                max = Math.max(max, i);
            }
            k -= max;
            answer++;
            if(k <= 0){
                break;
            }
        }

        return answer;
    }
}
```

### 문제점
- 가장 큰 값을 찾은 뒤 0으로 초기화하지 않음
- 매번 10,000,001칸을 탐색함 (시간 초과)

## 2차 제출 코드(오답)

```java
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int[] countArray = new int[10000001];
        for(int i : tangerine){
            countArray[i]++;
        }
        
        while(true){
            int maxIndex = 0;
            int max = countArray[0];
            for(int i = 0 ; i< countArray.length; i++){
                if(countArray[i] > max){
                    max = countArray[i];
                    maxIndex = i;
                }
            }
            countArray[maxIndex] = 0;
            k -= max;
            answer++;
            if(k <= 0){
                break;
            }
        }
        
        return answer;
    }
}
```

### 문제점
- 여전히 시간 초과 문제는 해결하지 못함


## 3차 제출 코드

```java
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Integer[] countArray = new Integer[10000001];
        Arrays.fill(countArray,0);
        for(int i : tangerine){
            countArray[i]++;
        }
        Arrays.sort(countArray, Collections.reverseOrder());
        
        
        for(int i : countArray){
            k-=i;
            answer++;
            if(k <= 0){
                break;
            }
        }
        
        return answer;
    }
}
```

### 실수한 부분
- 굳이 배열전체를 탐색하며 최대값을 찾지 말고 정렬을 사용해 앞 부분만 탐색하고 반복문을 나가면 시간 초과가 나지 않는다.
- Collections.reverseOrder()를 사용하려면 배열이 int형이 아닌 Integer형 이어야 한다.
- Integer 배열은 0이 아닌 null로 기본값을 초기화함으로 Arrays.fill()로 0으로 채워야한다.
- HashMap을 이용하면 더 효율적으로 할 수 있다.


## 4차 AI 개선 코드
```java
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i : tangerine){
            map.put(i, map.getOrDefault(i,0) + 1);
        }
        List<Integer> list = new ArrayList<>(map.values());
        
        list.sort(Collections.reverseOrder());
        
        for(int i : list){
            k -= i;
            answer++;
            if(k <= 0){
                break;
            }
        }
        
        return answer;
    }
}
```

- Map 을 사용하면 크기 10000001 배열을 선언하지 않아도 최소한의 크기로 문제를 풀 수 있다.