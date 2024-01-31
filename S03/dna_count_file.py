def dna_count_file(filename):
    with open(filename) as e:
        l = 0
        dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for line in e:
            l += len(line)
            for i in line:
                if i in dict:
                    dict[i] += 1
    print("Total length: " + str(l))
    for k, v in dict.items():
        print(str(k) + ": " + str(v))

dna_count_file("dna")