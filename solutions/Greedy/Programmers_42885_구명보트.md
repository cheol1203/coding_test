# 프로그래머스 🚤 구명보트 (Java)

## 코드 리뷰
- 처음에는 문제의 조건인 보트에 탈 수 있는 사람이 최대 2명인줄 모르고 풀었다.
- 정렬 후 가장 무거운 사람과 가장 가벼운 사람을 각각 투 포인터로 잡고, 가장 무거운 사람이 가장 가벼운 사람과 같이 탈 수 있는지 없는지를 구하면서 풀면 된다.
- 즉 , 가장 무거운 사람은 항상 이번 보트에 태우고, 같이 탈 수 있으면 가장 가벼운 사람도 함께 태우는 방식이다.

## 처음 오답 코드

```java
import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 1;
        int remain = limit;
        Arrays.sort(people);
        for(int i : people){
            if(i <= remain){
                remain-=i;
            }else{
                answer++;
                remain = limit;
                remain-=i;
            }
        }
        
        return answer;
    }
}
```

## AI 답안 참고
```java
import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int right = people.length-1;
        int left = 0;
        
        while(left <= right){
            if(people[right] + people[left] <= limit){
                left++;
            }
            right--;
            answer++;
        }
        
        return answer;
    }
}
```