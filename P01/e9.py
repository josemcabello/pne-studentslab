from Seq1 import *
from Seq0 import *
def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        dict = seq.seq_count(seq)
        sequence = seq
        reverse = seq.reverse()
        complement = seq.complement()
        print("Sequence", index + 1, ": (Lenght:", length, "):", sequence)
        print("Bases: ", dict)
        print("Rev:", reverse)
        print("Comp:", complement)



i = seq_read_fasta("U5.txt")
s1 = Seq(i)
seq_list = [s1]
print_seqs((seq_list))
