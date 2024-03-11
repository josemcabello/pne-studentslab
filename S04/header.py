from pathlib import Path

FILENAME = "RNU6_269P"


file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
print("First line of the RNU6_269P.txt file:")
print(list_contents[0])
