from Seq1 import *

def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        sequence = seq
        print("Sequence", index + 1, ":", sequence)

s1 = Seq()
s2 = Seq("TATAC")

seq_list = [s1, s2]
print_seqs((seq_list))