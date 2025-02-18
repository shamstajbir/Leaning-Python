def sum_of_elements_less_than_median(arr):
    arr.sort()
    n = len(arr)

    if n == 0:
        return 0


    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = arr[(n // 2) - 1]


    sum_less_than_median = sum(x for x in arr if x < median)

    return sum_less_than_median


size = int(input())
arr = list(map(int, input().split()))

print(sum_of_elements_less_than_median(arr))
