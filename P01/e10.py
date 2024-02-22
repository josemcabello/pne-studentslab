from Seq1 import *
s1 = Seq()
s1.read_fasta("ADA.txt")
s2 = Seq()
s2.read_fasta("FRAT1.txt")
s3 = Seq()
s3.read_fasta("FXN.txt")
s4 = Seq()
s4.read_fasta("U5.txt")
list_of_objects = [s1, s2, s3, s4,]
list_of_files = ["ADA.txt", "FRAT1.txt", "FXN.txt", "U5.txt"]
index = 0
for e in list_of_objects:
    e.most_common(list_of_files[index])
    index += 1