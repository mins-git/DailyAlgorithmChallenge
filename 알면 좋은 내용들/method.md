
# 람다
- lambda arguments: expression
`lambda 변수 : 표현식`
  
```python
# 가장 최대값 y찾기
for i in range(len(arr)):
    if arr[i][1] > max_arr_num:
        max_arr_num = arr[i][1]

# 위 내용을 아래와 같이 간단하게 풀 수 있다.
max_arr_num = max(arr, key=lambda x: x[1])[1]

# 아래와 같이 표현하면 index도 같이 뽑기 가능.
max_index, max_arr_num = max(enumerate(arr), key=lambda x: x[1][1]) #2번째 기준으로 최대값 뽑아오기.

# sorted하는 법 0번을 기준으로 
sorted_array = sorted(array, key=lambda x: x[0])

```

- 
# enumerate
- enumerate(start = )
    - `start 지정가능` 인덱스와 값을 함께 뽑아 낼 수 있음.
  

# 역순 변환하기
- arr[:][::-1]
  - 리스트 슬라이싱을 한 이후에 [::-1]을 통해서 역순으로 뒤집은 리스트를 반환함
  
```python
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[:][::-1]
print(reversed_arr)  # 출력: [5, 4, 3, 2, 1]

```