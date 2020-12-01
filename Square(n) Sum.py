def square_sum(numbers):
    sum,a= 0,0
    for i in range(len(numbers)):
        a = numbers[i]**2
        sum += a
    return sum
    
square_sum([1,2])