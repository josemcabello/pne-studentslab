from pathlib import Path

FILENAME = "RNU6_269P"


file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
print("Body of the U5.txt file:")
i = 1
while i < len(list_contents):
    print(list_contents[i])
    i += 1