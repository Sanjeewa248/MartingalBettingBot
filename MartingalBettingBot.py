import json
import time


# Define initial parameters
user1_balance = 1000000
user1_bet = 5000
user2_balance = 100000
user2_bet = 10000
round_num = 0
winning_results = ['player', 'banker', 'tie']

# Define the function to update the bet amount
def update_bet_amount(bet_amount):
    return bet_amount * 2

# Load the mock data from the JSON file
with open('baccarat_result.json', 'r') as f:
    mock_data = json.load(f)

# Iterate through the mock data
for result in mock_data:
    time.sleep(2)
    round_num += 1
    if result['winner'] == 'tie':
        # Refund bets for tie rounds
        user1_balance += user1_bet
        user2_balance += user2_bet
        print(f"Round {round_num}: Tie\n")
    elif result['winner'] == 'player':
        # User 1 wins, so User 2 loses
        user1_balance += user1_bet * 2
        user2_balance -= user2_bet
        user2_bet = update_bet_amount(user2_bet)
        print(f"Round {round_num}: User 1 wins\n")
    elif result['winner'] == 'banker':
        # User 2 wins, so User 1 loses
        user2_balance += user2_bet * 2
        user1_balance -= user1_bet
        user1_bet = update_bet_amount(user1_bet)
        print(f"Round {round_num}: User 2 wins\n")
    
    # Check if either user has lost all their money
    if user1_balance <= 0:
        print(f"User 1 is bankrupt after {round_num} rounds.")
        user1_balance = 0
        break
    elif user2_balance <= 0:
        print(f"User 2 is bankrupt after {round_num} rounds.")
        user2_balance = 0
        break
    
    # Ensure that balance doesn't go below zero
    user1_balance = max(user1_balance, 0)
    user2_balance = max(user2_balance, 0)
    
    # Print the updated balances for both users after each round
    print(f"User 1 balance: {user1_balance}")
    print(f"User 2 balance: {user2_balance}\n")

# Print the final balances for both users
print("Final balances:")
print(f"User 1 balance: {user1_balance}")
print(f"User 2 balance: {user2_balance}")
