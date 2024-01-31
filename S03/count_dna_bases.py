sequence = input("Enter a valid sequence")
l = len(sequence)
dict = {"A": 0, "C": 0, "G": 0, "T": 0}
for e in sequence:
    if e in dict:
        dict[e] += 1
print("Total length: " + str(l))
for k, v in dict.items():
    print(str(k) + ": " + str(v))