
def counting_sort(data, temp):
    # data는 정렬해야할 배열
    # temp는 임시 저장값
    # k는 최대값이 될것임.
    k = max(data)
    counts = [0] * (k + 1)

    # counts에 data의 실제값을 counts인덱스에 넣어줌으로써 숫자 세기.
    for num in data:
        counts[num] += 1

    # counts의 인덱스값을 더해줌
    # 더해줌으로써 너는 최소 4번째 위치에는 있겠네. 라고 알 수 있게됨.
    # 예를들어 counts = [0, 1, 2, 2, 1, 0, 0, 0, 1] 이런배열이
    # counts = [0, 1, 3, 5, 6, 6, 6, 6, 7] 이렇게 바뀌게됨.
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_arr = [0] * len(data)

    # for num in range(len(data) - 1, -1, -1):  # 실제로는 0까지 반복되겠네, 1개씩 감소하면서.
    for num in reversed(data):
        counts[num] -= 1
        sorted_arr[counts[num]] = num

    return sorted_arr



# def counting_sort(arr):
#     """
#     카운팅 정렬 함수
#     :param arr: 정렬할 정수 리스트
#     :return: 정렬된 정수 리스트
#     """

#     if not arr:
#         return arr

#     # 1. 배열의 최소값과 최대값을 찾습니다.
#     min_val = min(arr)
#     max_val = max(arr)

#     # 2. 범위를 기반으로 카운트 배열을 생성합니다.
#     count_range = max_val - min_val + 1
#     count = [0] * count_range

#     # 3. 입력 배열의 각 값을 카운트 배열에 개수를 기록합니다.
#     for num in arr:
#         count[num - min_val] += 1

#     # 4. 카운트 배열을 기반으로 정렬된 결과 배열을 생성합니다.
#     sorted_arr = []
#     for i, cnt in enumerate(count):
#         if cnt > 0:
#             sorted_arr.extend([i + min_val] * cnt)

#     return sorted_arr


# # 사용 예시
# input_array = [4, 2, 2, 8, 3, 3, 1]
# sorted_array = counting_sort(input_array)
# print("정렬된 배열:", sorted_array)
