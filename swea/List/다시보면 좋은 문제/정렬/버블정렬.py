def bubble_sort(arr):
    n = len(arr)  # 배열의 길이를 구합니다.

    # 모든 요소를 확인하는 외부 루프입니다.
    for i in range(n):
        # 교환이 이루어졌는지를 추적할 플래그입니다.
        swapped = False

        # 내부 루프는 정렬된 요소를 제외하고 요소를 비교합니다.
        # n-i-1은 이미 정렬된 부분을 건너뜁니다.
        for j in range(0, n - i - 1):
            # 인접한 두 요소를 비교합니다.
            if arr[j] > arr[j + 1]:
                # 두 요소를 교환합니다.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # 교환이 이루어졌으므로 플래그를 True로 설정합니다.
                swapped = True

        # 이번 패스에서 교환이 없었다면 배열이 정렬되었으므로 종료합니다.
        if not swapped:
            break


# 예제 배열
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("정렬된 배열은:", arr)
