def linear_search(arr, target):
    return next((i for i, val in enumerate(arr) if val == target), -1)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        low, high = (mid + 1, high) if arr[mid] < target else (low, mid - 1)
    return -1

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left); merge_sort(right)
        arr[:] = sorted(left + right)

def quick_sort(arr):
    return arr if len(arr) <= 1 else quick_sort([x for x in arr if x < arr[len(arr) // 2]]) + [x for x in arr if x == arr[len(arr) // 2]] + quick_sort([x for x in arr if x > arr[len(arr) // 2]])

# Example usage:

arr_linear_search = [4, 2, 7, 1, 9, 5]
target_linear_search = 7
print(f"Element {target_linear_search} found at index {linear_search(arr_linear_search, target_linear_search)}")

arr_binary_search = [1, 2, 4, 5, 7, 9]
target_binary_search = 7
print(f"Element {target_binary_search} found at index {binary_search(arr_binary_search, target_binary_search)}")

arr_selection_sort = [64, 25, 12, 22, 11]
selection_sort(arr_selection_sort)
print("Sorted array (Selection Sort):", arr_selection_sort)

arr_merge_sort = [64, 25, 12, 22, 11]
merge_sort(arr_merge_sort)
print("Sorted array (Merge Sort):", arr_merge_sort)

arr_quick_sort = [64, 25, 12, 22, 11]
print("Sorted array (Quick Sort):", quick_sort(arr_quick_sort))
