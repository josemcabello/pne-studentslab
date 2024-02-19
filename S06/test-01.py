from Seq0 import *

seq1 = "ATTCCCGGGG"
l = len(seq1)
print("Seq:", seq1)
print("Rev :",  seq_reverse(seq1, l))
print("Comp:", seq_complement(seq1))
print("Length:", seq_len(seq1))
print("A:", seq_count_base(seq1, 'A'))
print("T:", seq_count_base(seq1, 'T'))
print("C:", seq_count_base(seq1, 'C'))
print("G:", seq_count_base(seq1, 'G'))
