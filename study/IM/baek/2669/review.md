# 코드

- 문제 풀이 포인트 🤞
    1. 1 x 1 칸이기에 1칸의 넓이는 1이다.
    2. 전체 칸수의 요소를 모은 arr 배열을 만든 후 set을 사용해서 중복요소(겹치는곳) 제거해준다.
- 앗 나의 실수 😢
    1. 
    2. 

```python
#1.
 arr = [] # 겹치는 배열을 알기 위한 정리.
    for i in range(4):
        left_x, left_y, right_x, right_y = map(int, input().split())
        for y in range(right_y, left_y, -1):  # right y부터 left y까지 순회하기.
            for x in range(left_x, right_x, 1): #left_x부터 right_x까지 1씩증가
                arr.append([x,y])




    for_check_len = [tuple(x) for x in arr]
    print(len(set(for_check_len)))
```