def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                # exchange
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


if __name__ == "__main__":
    a1 = [5, 2, 4, 7, 6, 1, 3]
    bubble_sort(a1)
    print(a1)
