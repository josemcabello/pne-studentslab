
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
        return self.strbases


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases


def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        lenght = seq.len()
        sequence = seq
        print("Sequence", index, ": (Lenght:", index, ")", sequence)


def generate_seqs(pattern, number):
    list = []
    for i in range(1, number + 1):
        list.append(Seq(pattern * i))
    return list



seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print("List 2:")
print_seqs(seq_list2)
