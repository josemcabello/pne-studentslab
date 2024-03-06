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



# -- Create a Null sequence
s = Seq()
s1 = s.read_fasta("U5.txt")
# -- Initialize the null seq with the given file in fasta format
#s1 = Seq(s.read_fasta("U5.txt"))
seq_list = [s]
print_seqs((seq_list))
