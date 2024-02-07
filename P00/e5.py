from Seq0 import *

list_of_files = ["ADA.txt", "FRAT1.txt", "FXN.txt", "U5.txt"]
list_of_seq = []
a1 = 0
for e in list_of_files:
    seq = ""
    file_contents = Path(e).read_text()
    list_contents = file_contents.split("\n")
    list_contents.pop(0)
    for i in list_contents:
        seq += i
    list_of_seq.append(seq)
    dict = seq_count(seq)
    print("Gene", list_of_files[a1], ":", dict)
    a1 += 1