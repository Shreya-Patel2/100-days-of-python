import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
running_game = True
if play_game == "n":
    print("No game")
    running_game = False

while running_game:
    if play_game == "y":
        player_cards = random.choices(cards, k=2)
        computer_cards = random.choices(cards, k=2)

        num1_player = player_cards[0]
        num2_player = player_cards[1]
        total_player = num1_player + num2_player

        num1_computer = computer_cards[0]
        num2_computer = computer_cards[1]
        total_computer = num1_computer + num2_computer

        if total_computer < 17:
            computer_next_card = random.choice(cards)
            total_computer += computer_next_card
            computer_cards.insert(len(computer_cards), computer_next_card)

        print(f"Your cards: {player_cards}, current score: {total_player}")
        print(f"Computer's first card: {num1_computer}")

        if total_player == 21:
            print(f"Your final hand: {player_cards}, final score: {total_player}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
            print("Win with a Blackjack 😎")
            play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
            if play_game == "y":
                running_game = True
            else:
                running_game = False
        elif total_player > 21:
            print(f"Your final hand: {player_cards}, final score: {total_player}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
            print("You went over. You lose 😭")
            play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
            if play_game == "y":
                running_game = True
            else:
                running_game = False
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
            player_keep_drawing = True
            while player_keep_drawing == True:
                if another_card == "y":
                    player_next_card = random.choice(cards)
                    total_player += player_next_card
                    player_cards.insert(len(player_cards), player_next_card)
                    if total_player > 21:
                        player_keep_drawing = False
                        print(f"Your final hand: {player_cards}, final score: {total_player}")
                        print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                        print("You went over. You lose 😭")
                        play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                        if play_game == "y":
                            running_game = True
                        else:
                            running_game = False
                    elif total_player == 21:
                        player_keep_drawing = False
                        print(f"Your final hand: {player_cards}, final score: {total_player}")
                        print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                        print("Win with a Blackjack 😎")
                        play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                        if play_game == "y":
                            running_game = True
                        else:
                            running_game = False
                    else:
                        print(f"Your cards: {player_cards}, current score: {total_player}")
                        print(f"Computer's first card: {num1_computer}")
                        another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()

                        if another_card == "n":
                            player_keep_drawing = False
                            print(f"Your final hand: {player_cards}, final score: {total_player}")
                            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                            if total_computer == total_player:
                                print("It's a draw")
                                play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                                if play_game == "y":
                                    running_game = True
                                else:
                                    running_game = False
                            elif total_computer > 21:
                                print("You win!")
                                play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                                if play_game == "y":
                                    running_game = True
                                else:
                                    running_game = False
                            elif total_player == 20 and total_computer != 20:
                                print("You win!")
                                play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                                if play_game == "y":
                                    running_game = True
                                else:
                                    running_game = False
                            elif total_computer > total_player and total_computer <= 21:
                                print("Computer wins:(")
                                play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                                if play_game == "y":
                                    running_game = True
                                else:
                                    running_game = False
                            else:
                                print("You win!")
                            play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                            if play_game == "y":
                                running_game = True
                            else:
                                running_game = False
                else:
                    print(f"Your final hand: {player_cards}, final score: {total_player}")
                    print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")
                    if total_computer > total_player:
                        print("Computer wins:(")
                        player_keep_drawing = False
                        play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                        if play_game == "y":
                            running_game = True
                        else:
                            running_game = False
                    elif total_computer == total_player:
                        print("It's a draw")
                        player_keep_drawing = False
                        play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                        if play_game == "y":
                            running_game = True
                        else:
                            running_game = False
                    else:
                        print("You win!")
                    player_keep_drawing = False
                    play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':").lower()
                    if play_game == "y":
                        running_game = True
                    else:
                        running_game = False
