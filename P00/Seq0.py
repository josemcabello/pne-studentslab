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

def seq_reverse(seq, n):
    a_seq = seq[0:n]
    reverse = ""
    for i in a_seq:
        reverse = str(i) + reverse
    print("Fragment:", a_seq)
    print("Reverse:", reverse)

def seq_complement(seq):
    complement_seq = ""
    for e in seq:
        if e == "A":
            complement_seq += "T"
        elif e == "C":
            complement_seq += "G"
        elif e == "G":
            complement_seq += "C"
        elif e == "T":
            complement_seq += "A"
    print("Frag:", seq)
    print("Comp:", complement_seq)


def most_common(filename):
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
        x == a
    if x < c:
        x == c
    if x < g:
        x == g
    if x < t:
        x == t
    solution =
    print("Gene", str(filename), "Most frequent base:",)