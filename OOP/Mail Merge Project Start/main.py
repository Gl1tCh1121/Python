
        


with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as data:
    text = data.read()
    print(text)

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

for name in names:
    name = name.strip()
    personalized_letter = text.replace("[name]", name)
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
        new_letter.write(personalized_letter)