def insert_sort(array: list) -> list:
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i>= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


if __name__ == "__main__":
    a1 = [5, 2, 1, 3, 10]
    insert_result = insert_sort(a1)
    print(insert_result)
