def binary_search(arr, target):
    count, low = 0, 0
    high = len(arr) - 1
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        count += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value >= target:
            upper_bound = mid_value
            high = mid - 1

    return count, upper_bound


sorted_array = [0.5, 1.7, 3.2, 4.8, 6.1, 7.3, 8.9, 10.3, 12.6, 14.4,
                15.9, 17.2, 19.0, 20.5, 22.1, 23.7, 25.0, 27.8, 29.3, 30.6]
target_value = 19.11

iterations, upper_bound = binary_search(sorted_array, target_value)

if upper_bound is not None:
    print(
        f"Елемент {target_value} знайдено за {iterations} ітерацій. Верхня межа: {upper_bound}")
else:
    print(f"Елемент {target_value} не знайдено у масиві.")
