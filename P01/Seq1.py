from pathlib import Path
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
    def read_fasta(self, filename):

        self.strbases = ""
        file_contents = Path(filename).read_text()
        list_contents = file_contents.split("\n")
        list_contents.pop(0)

        for i in list_contents:
            for e in i:
                self.strbases += e
        return self.strbases
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
            reverse = "ERROR"
        else:
            a_seq = self.strbases
            reverse = ""
            for i in a_seq:
                reverse = str(i) + reverse
        return reverse

    def complement(self):
        if self.strbases == "NULL":
            complement = "NULL"
        elif self.strbases == "Error":
            complement = "ERROR"
        else:
            seq = self.strbases
            complement = ""
            for e in seq:
                if e == "A":
                    complement += "T"
                elif e == "C":
                    complement += "G"
                elif e == "G":
                    complement += "C"
                elif e == "T":
                    complement += "A"
        return complement

    def most_common(self, filename):
        if self.strbases == "NULL":
             print("NULL")
        elif self.strbases == "Error":
            print("ERROR")
        else:
            file_contents = Path(filename).read_text()
            list_contents = file_contents.split("\n")
            list_contents.pop(0)
            seq = ""
            for i in list_contents:
                seq += str(i)
            a = 0
            c = 0
            g = 0
            t = 0
            for e in seq:
                if e == "A":
                    a += 1
                elif e == "C":
                    c += 1
                elif e == "G":
                    g += 1
                elif e == "T":
                    t += 1
            x = 0
            if x < a:
                x = a
            if x < c:
                x = c
            if x < g:
                x = g
            if x < t:
                x = t

            if x == a:
                solution = "A"
            elif x == c:
                solution = "C"
            elif x == g:
                solution = "G"
            elif x == t:
                solution = "T"
            print("Gene", str(filename), "Most frequent base:", solution)



    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases
