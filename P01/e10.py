from Seq0 import *
from Seq1 import *
i = seq_read_fasta("ADA.txt")
i2 = seq_read_fasta("FRAT1.txt")
i3 = seq_read_fasta(("FXN.txt"))
i4 = seq_read_fasta("U5.txt")
s1 = Seq()
s2 = Seq(i)
s3 = Seq()
s4 = Seq(i2)
s5 = Seq(i3)
s6 = Seq(i3)
list_of_objects = [s1, s2, s3, s4, s5, s6]
list_of_files = ["", "ADA.txt", "", "FRAT1.txt", "FXN.txt", "U5.txt"]
index = 0
for e in list_of_objects:
    e.most_common(list_of_files[index])
    index += 1
