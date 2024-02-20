from Seq1 import *

def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        sequence = seq
        print("Sequence", index + 1, ":", sequence)

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("Invalid sequence")

seq_list = [s1, s2, s3]
print_seqs((seq_list))