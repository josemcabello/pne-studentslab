def fibosum(n):
    i = 0
    list = [0, 1]
    while i < (n - 1):
        new_value = list[-1] + list[-2]
        list.append(new_value)
        i += 1
    result = 0
    for e in list:
        result += e
    print("Sum of the first " + str(n) + "terms of the fibonacci series: " + str(result))

fibosum(10)