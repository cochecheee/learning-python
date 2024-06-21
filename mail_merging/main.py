LETTER_FILE_PATH = "./inputs/letters/letter_form.txt"
NAME_FILE_PATH = "./inputs/names/list_names.txt"

def wrire_file(filename,letter):
    with open(f"./outputs/{filename}", mode="w") as file:
        file.write(letter)

def read_file(filepath):
    with open(filepath) as file:
        content = file.read()
    return content

# fetch sample mail
LETTER = read_file(LETTER_FILE_PATH)

# fetch list of names
list_of_names = read_file(NAME_FILE_PATH).split()

# generate letter for each name
for name in list_of_names:
    letter = LETTER.replace("[name]",name)
    # save to ouput folder
    filename = "letter_for_" + name
    wrire_file(filename=filename,letter=letter)
