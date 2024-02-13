from Seq0 import *
filename = "U5.txt"
file_contents = Path(filename).read_text()
list_contents = file_contents.split("\n")
list_contents.pop(0)
seq = ""
print("Gene U5:")
for i in list_contents:
    seq += str(i)
seq_reverse(seq, 20)