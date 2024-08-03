def counting_sort(arr):
    """
    카운팅 정렬 함수
    :param arr: 정렬할 정수 리스트
    :return: 정렬된 정수 리스트
    """

    if not arr:
        return arr

    # 1. 배열의 최소값과 최대값을 찾습니다.
    min_val = min(arr)
    max_val = max(arr)

    # 2. 범위를 기반으로 카운트 배열을 생성합니다.
    count_range = max_val - min_val + 1
    count = [0] * count_range

    # 3. 입력 배열의 각 값을 카운트 배열에 개수를 기록합니다.
    for num in arr:
        count[num - min_val] += 1

    # 4. 카운트 배열을 기반으로 정렬된 결과 배열을 생성합니다.
    sorted_arr = []
    for i, cnt in enumerate(count):
        if cnt > 0:
            sorted_arr.extend([i + min_val] * cnt)

    return sorted_arr


# 사용 예시
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print("정렬된 배열:", sorted_array)
