import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
print("Total people in database:", str(len(person)))
for i1, dict in enumerate(person):
    # Print the information on the console, in colors
    termcolor.cprint("Name: ", 'green', end="")
    print(dict['Firstname'], dict['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(dict['age'])

    # Get the phoneNumber list
    phoneNumbers = dict['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
    print()