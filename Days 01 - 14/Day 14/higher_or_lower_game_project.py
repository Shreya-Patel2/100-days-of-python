import random
import game_data

to_chose = []
follower_number = []
highest_followers = []
key_one = []
key_two = []
keys_numbers = []

for information in game_data.data:
    Name = information["name"]
    Follower_Count = information["follower_count"]
    Description = information["description"]
    Country = information["country"]
    statements = [f"{Name}, a {Description}, from {Country} {Follower_Count}"]
    to_chose.append(statements)
    follower_number.append(Follower_Count)


def get_keys_from_value(d, val1, val2):
    output1 = [k for k, v in d.items() if v == val1]
    output2 = [k for k, v in d.items() if v == val2]
    if output1 > output2:
        highest_followers.append(output1)
    else:
        highest_followers.append(output2)
    key_one.append(output1)
    key_two.append(output2)


num = len(game_data.data)
for i in range(1, num + 1):
    keys_numbers.append(i)

dictionary = dict(zip(follower_number, to_chose))

score = 0
playing_game = True
first_run = True

while playing_game:

    if first_run:
        first_comparator_function = random.choice(list(dictionary.values()))
    else:
        first_comparator_function = next_first

    first_comparator = ", ".join(first_comparator_function)
    second_comparator_function = random.choice(list(dictionary.values()))
    second_comparator = ", ".join(second_comparator_function)
    print(f"Compare A: {first_comparator}.\nAgainst B: {second_comparator}.")

    answer = input("Who has more followers? Type 'A' or 'B':").lower()
    get_keys_from_value(dictionary, first_comparator_function, second_comparator_function)

    if answer == "a":
        user_choice_highest_followers = key_one
    else:
        user_choice_highest_followers = key_two

    if user_choice_highest_followers == highest_followers:
        score += 1
        print(f"You're right! Current score: {score}\n")
        next_first = second_comparator_function
        key_one = []
        key_two = []
        highest_followers = []
        first_run = False

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        playing_game = False
