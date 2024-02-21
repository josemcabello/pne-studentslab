from Seq1 import *
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

FILENAME = "U5.txt"
s = Seq()
i = s.read_fasta("U5.txt")
s1 = Seq(i)
seq_list = [s1]
print_seqs((seq_list))

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format

seq_list = [s1]
print_seqs((seq_list))
