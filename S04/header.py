from pathlib import Path

FILENAME = "sequences/U5.txt"


file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")

for i in range(0, len(list_contents)):
    print(list_contents[i])
