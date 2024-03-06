from Seq1 import *
def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        dict = seq.seq_count(seq)
        sequence = seq
        reverse = seq.reverse()
        print("Sequence", index + 1, ": (Lenght:", length, "):", sequence)
        print("Bases: ", dict)
        print("Rev:", reverse)

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("Invalid sequence")

seq_list = [s1, s2, s3]
print_seqs((seq_list))