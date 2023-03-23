import random

# Set initial bet amounts and balances for User 1 and User 2
user1_bet = 5000
user1_balance = 1000000
user2_bet = 10000
user2_balance = 100000

# Set maximum number of rounds to play
max_rounds = 19

# Set win multipliers (e.g., 2x for Player or Banker bets)
win_multipliers = {'player': 2, 'banker': 2}

# Set initial number of consecutive losses for each user
user1_consecutive_losses = 0
user2_consecutive_losses = 0

# Loop through rounds
for round_num in range(max_rounds):
    
    # Check if either user's balance is zero
    if user1_balance == 0 or user2_balance == 0:
        print("User balance depleted. Exiting.")
        break
    
    # Generate random result (0 for Player, 1 for Banker, 2 for Tie)
    result = random.randint(0, 2)
    
    # If result is a Tie, refund bets to both users
    if result == 2:
        print("Round", round_num + 1, "result: Tie")
        user1_balance += user1_bet
        user2_balance += user2_bet
        user1_bet = 5000
        user2_bet = 10000
        user1_consecutive_losses = 0
        user2_consecutive_losses = 0
    # If result is a Player win, add winnings to User 1's balance and reset bets for both users
    elif result == 0:
        print("Round", round_num + 1, "result: Player win")
        user1_balance += user1_bet * win_multipliers['player']
        user1_bet = 5000
        user2_bet = 10000
        user1_consecutive_losses = 0
        user2_consecutive_losses = 0
    # If result is a Banker win, add winnings to User 2's balance and reset bets for both users
    else:
        print("Round", round_num + 1, "result: Banker win")
        user2_balance += user2_bet * win_multipliers['banker']
        user1_bet = 5000
        user2_bet = 10000
        user1_consecutive_losses = 0
        user2_consecutive_losses = 0
    
    # Update consecutive losses for each user
    if result == 0:
        user1_consecutive_losses += 1
        user2_consecutive_losses = 0
    elif result == 1:
        user2_consecutive_losses += 1
        user1_consecutive_losses = 0
    else:
        user1_consecutive_losses = 0
        user2_consecutive_losses = 0
        
    # Double bet amount for each user if they have had three consecutive losses
    if user1_consecutive_losses == 3:
        user1_bet *= 2
    if user2_consecutive_losses == 3:
        user2_bet *= 2
    
    # Print current balances and bet amounts for each user
    print("User 1 balance:", user1_balance, "User 1 bet:", user1_bet)
    print("User 2 balance:", user2_balance, "User 2 bet:", user2_bet)
