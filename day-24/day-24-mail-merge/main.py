# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


# Function to generate letter
def write_letter(template: str, name: str):
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(template.replace(PLACEHOLDER, name))


# Read letter template
with open("./Input/Letters/starting_letter.txt", mode="r") as template:
    letter_template = template.read()

# Read names file and generate letter from template for each name
with open("./Input/Names/invited_names.txt", mode="r") as names:
    for name in names:
        write_letter(letter_template, name.strip())
