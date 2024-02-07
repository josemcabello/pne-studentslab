from Seq0 import *

list_of_files = ["ADA.txt", "FRAT1.txt", "FXN.txt", "U5.txt"]
list_of_seq = []
for e in list_of_files:
    seq_to_add = ""
    file_contents = Path(e).read_text()
    list_contents = file_contents.split("\n")
    list_contents.pop(0)
    for i in list_contents:
        seq_to_add += i
    list_of_seq.append(seq_to_add)
a1 = 0
for a in list_of_seq:
    b = seq_len(a)
    print("Gene " + list_of_files[a1][:-4] + " -> Length: " + str(b))
    a1 += 1
