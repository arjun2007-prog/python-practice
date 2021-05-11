with open("/mail-merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/mail-merge/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    print(letter)

for name in names:
    name = name.strip("\n")
    with open(f"/mail-merge/Output/ReadyToSend/letter_to_{name}.txt", mode="w") as invitaion:
        new_letter = letter.replace("[name]", name)
        invitaion.write(new_letter)

