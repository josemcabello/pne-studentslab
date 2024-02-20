class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases=None):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
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
                self.strbases = "Error"
                print("Invalid sequence!")

    def len(self):
        if self.strbases == "NULL" or self.strbases == "Error":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def seq_count(self, strbases):
        if self.strbases == "NULL" or self.strbases == "Error":
            seq = ""
        else:
            seq = self.strbases
        dict = {}
        a = seq.count("A")
        c = seq.count("C")
        g = seq.count("G")
        t = seq.count("T")
        dict["A"] = a
        dict["C"] = c
        dict["G"] = g
        dict["T"] = t
        return dict

    def reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "Error":
            reverse = "Error"
        else:
            a_seq = self.strbases[0:]
            reverse = ""
            for i in a_seq:
                reverse = str(i) + reverse
        return reverse
    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases
