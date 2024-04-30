from Seq0 import *
filename = "U5.txt"
i = seq_read_fasta(filename)
print("Dna file : " + filename)
print("First 20 bases are: " + "\n" + i[0:19])