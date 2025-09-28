# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp


list_of_names = []
with open("Input/Names/invited_names.txt", "r") as invited_names:
    each_name = invited_names.readlines()
    for name in each_name:
        list_of_names.append(name)

line_1 = []
letters = []
with open("Input/Letters/starting_letter.txt", "r+") as starting_letter:
    list_of_lines = starting_letter.readlines()
    first_line = list_of_lines[0]
    for person_name in list_of_names:
        customised = first_line.replace("[name],", person_name)
        customised = customised.strip()
        line_1.append(customised)
    for number in range(0, 8):
        new_list = list_of_lines.copy()
        letters.append(new_list)

two_line = []
three_line = []
four_line = []
for item in letters:
    line_2 = item[1]
    two_line.append(line_2)
    line_3 = item[2]
    three_line.append(line_3)
    line_4 = item[3]
    four_line.append(line_4)

C = []
for i in range(len(line_1)):
    new = line_1[i] + '\n' + two_line[i] + three_line[i] + four_line[i]
    C.append(new)

titles = []
for element in C:
    new = [element]
    newer = element.split("\n")[0]
    titles.append(newer)

start = 0
for _ in titles:
    with open(f"Output/ReadyToSend/{_}.txt", "w") as saved_name:
        saved_name.write(C[start])
        start += 1