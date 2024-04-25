from Seq1 import *


def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        sequence = seq
        print("Sequence", index + 1, ":(Length:",str(sequence), ")", sequence)

seq_list = [Seq("ACTGA")]
print_seqs((seq_list))