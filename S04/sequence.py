from pathlib import Path

FILENAME = "ADA.txt"


file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
seq = ""
i = 1
while i < len(list_contents):
    seq += list_contents[i]
    i += 1
print("Total number of bases of the ADA.txt file:")
letters = ["A", "C", "G", "T"]
count1 = [seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")]
porc = [str(100 * seq.count("A") / len(seq)) + " %", str(100 * seq.count("C") / len(seq)) + " %",
        str(100 * seq.count("G") / len(seq)) + " %", str(100 * seq.count("T") / len(seq)) + " %"]
print(len(seq))
i = 0
response = "Sequence: " + seq + "\n" + "Total length:" + str(len(seq)) + "\n"
while i < 4:
    a = str(letters[i]) + " : " + str(count1[i]) + " (" + str(porc[i]) + ")" + "\n"
    print(a)
    response += a
    i += 1
print(response)