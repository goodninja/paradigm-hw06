# Ваша задача
# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


from typing import List


def binary(arr: List[int], target: int) -> int:
    """ Бинарный поиск элемента в целочисленном массиве """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary(arr, target)
print(f"Целочисленный массив: {arr}")
print(f"Искомый элемент: {target}")
if result == -1:
    print("Искомый элемент в массиве отсутствует")
else:
    print(f"Искомый элемент найден, индекс элемента -> {result}")
