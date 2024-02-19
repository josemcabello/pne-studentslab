class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        for i in self.strbases:
            if i == "A" or i == "C" or i == "G" or i == "T":
                solution = True
            else:
                solution = False
                break
        if solution:
            print("New sequence created!")
        else:
            print("Error")
    def len(self):
        return len(self.strbases)


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases


def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        sequence = seq
        print("Sequence", index, ": (Lenght:", length, ")", sequence)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs((seq_list))