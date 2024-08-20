def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 배열을 두 개로 분할
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 두 개의 분할된 배열을 병합
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 두 배열을 하나로 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남아 있는 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
