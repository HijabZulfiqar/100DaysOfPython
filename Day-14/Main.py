import random
import art
import GameData

def get_random_account():
    """Get random account data from the dataset."""
    return random.choice(GameData.data)

def format_account_data(account):
    """Format the account data into a printable string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def compare_followers(guess, a_followers, b_followers):
    """Compare followers count based on user's guess."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Ensure different accounts are selected
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_account_data(account_a)}")
        print("VS")
        print(f"Compare B: {format_account_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = compare_followers(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print("Correct! Current score:", score)
            account_a = account_b  # Move account B to A for next round
            account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Incorrect. Final score: {score}")

game()
