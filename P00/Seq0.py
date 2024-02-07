def seq_ping():       # en este fichero vamos a guardar las funciones que usaremos en otros ficheros de python
    print("OK")

from pathlib import Path
def seq_read_fasta(filename):

    first_20 = ""
    file_contents = Path(filename).read_text()
    list_contents = file_contents.split("\n")
    list_contents.pop(0)

    for i in list_contents:
        for e in i:
            if len(first_20) == 20:
                break
            elif len(first_20) < 21:
                first_20 += e
    return first_20


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    a = seq.count(base)
    print(base + ": " + str(a))

def seq_count(seq):
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
