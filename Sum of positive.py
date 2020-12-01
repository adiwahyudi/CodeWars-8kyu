def positive_sum(arr):
    sum = 0
    i = 0
    while i < len(arr):
        if arr[i]>0:
            sum = sum + arr[i]
        i += 1
    return sum