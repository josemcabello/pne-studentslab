
import termcolor
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

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return self.strbases


def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        sequence = seq
        termcolor.cprint(("Sequence" + str(index) + ": (Length:" + str(length) + ")" + str(sequence)), color)


def generate_seqs(pattern, number):
    list = []
    for i in range(1, number + 1):
        list.append(Seq(pattern * i))
    return list



seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
