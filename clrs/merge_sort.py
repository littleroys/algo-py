def merge_sort(array: list) -> list:
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left_half = merge_sort(left)
    right_half = merge_sort(right)

    return merge(left_half, right_half)


def merge_sort_2(array: list) -> list:
    def merge(arr, left, right):
        i = j = 0
        left.append(float("inf"))
        right.append(float("inf"))
        for k in range(len(left) + len(right) - 2):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort_2(left_half)
        merge_sort_2(right_half)

        merge(array, left_half, right_half)


if __name__ == "__main__":
    a1 = [5, 2, 4, 7, 6, 1, 3]
    result = merge_sort(a1)
    print(result)
    merge_sort_2(a1)
    print(a1)
