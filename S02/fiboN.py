def fibonacci(n):
    i = 0
    list = [0, 1]
    while i < (n - 1):
        new_value = list[-1] + list[-2]
        list.append(new_value)
        i += 1

    print(str(n) + "th Fibonacci term is: " + str(list[-1]))


fibonacci(15)