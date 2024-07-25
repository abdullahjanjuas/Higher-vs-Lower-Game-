#importing modules
from Game_data import data
from Game_art import logo, vs
import random

def format(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_ans(guess, followers_a, followers_b):
    """Checks if the user is correct or not"""
    print(f"Checking answer: guess = {guess}, followers_a = {followers_a}, followers_b = {followers_b}")
    if followers_a > followers_b:
        return guess == "A"
    else:
        return guess == "B"

# UI
print(logo)
score = 0

# Generate a random account from game data
account_a = random.choice(data)

# Loop to keep the game running until the user makes a wrong guess
game_should_continue = True
while game_should_continue:
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Compare B: {format(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Check if user is correct
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_ans(guess, a_followers, b_followers)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
        # The account with more followers becomes the new account_a
        account_a = account_b if b_followers > a_followers else account_a
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
