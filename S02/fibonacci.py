i = 0
list = [0,1]
while i < 9:
    new_value = list[-1] + list[-2]
    list.append(new_value)
    i += 1

print(list)