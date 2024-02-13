from Seq0 import *
filename = "U5.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split("\n")
list_contents.pop(0)
seq = ""
for i in list_contents:
    seq += str(i)
print("Gene U5:")
seq_complement(seq)