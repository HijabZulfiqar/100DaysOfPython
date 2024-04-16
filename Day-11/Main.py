import art
import random


gameover = 0

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    # Random card generator from list cards

    def random_card():
        # Ace choice

        if random.choice(cards) == 11 and sum(user_cards) + 11 > 21:
            return 1
        # Return any other card
        return random.choice(cards)

    # User
    user_cards = [random_card(), random_card()]
    # Computer
    computer_cards = [random_card(), random_card()]

    # Ask user if they want to play, return answer
    def checker():
        if sum(computer_cards) > sum(user_cards):
            # Computer greater
            if sum(computer_cards) > 21:
                if sum(user_cards) > 21:
                    return 'draw'
                else:
                    return 'user wins'
            else:
                return 'computer wins'
        elif sum(computer_cards) == sum(user_cards):
            # Draw
            return 'draw'
        else:
            # User greater
            if sum(user_cards) > 21:
                if sum(computer_cards) > 21:
                    return 'draw'
                else:
                    return 'computer wins'
            else:
                return 'user wins'

    def display_final():
        print(
            f"    Your final cards: {user_cards}. Your final score: {sum(user_cards)}.\n"
        )
        print(
            f"    Computer's final cards: {computer_cards}. Computer's final score: {sum(computer_cards)}.\n"
        )

    play = input(
        "\nDo you want to play a game of blackjack? 'y' for yes or 'n' for no.\n"
    )
    if play == 'y':

        print(art.logo)

    # Game loop
    while play == 'y':

        # Dislpay user and computer card and score
        print(f"    Your cards: {user_cards}. Your score: {sum(user_cards)}.")

        print(f"    Computer's first card: {computer_cards[0]}.")
        # Ask to draw
        yes_no = input("Type 'y' to get another card, type 'n' to pass: ")
        if yes_no == 'y':
            # Add a random card to each card list
            user_cards.append(random_card())
            computer_cards.append(random_card())

            # Check if scores are below 21
            if sum(user_cards) > 21:
                print("Uh oh... Your score is above 21. You lose 😤")
                display_final()
                blackjack()

            # Blackjack scenarios
            if sum(computer_cards) == 21:
                if sum(user_cards) == 21:
                    # Computer and user get blackjack: draw
                    print(
                        "This is a rare draw. You and the computer have blackjack.\n"
                    )
                    display_final()
                    blackjack()

                else:
                    # Computer gets blackjack: computer wins
                    print(
                        f"The computer has blackjack you lose. 😱"
                    )
                    display_final()
                    blackjack()
            elif sum(user_cards) == 21:
                print("You got a blackjack, you win 🥳")
                display_final()
                blackjack()

        else:
            display_final()

            # print endgame status
            if checker() == 'user wins':
                print("You win 🤑")
            elif checker() == 'computer wins':
                print("You lose 😤")
            else:
                print("Tie 🎀")
            blackjack()

    print("👋 Goodbye 👋")


blackjack()
