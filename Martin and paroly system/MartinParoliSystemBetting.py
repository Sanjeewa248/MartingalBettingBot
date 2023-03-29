import json
import time
import random

class User:
    def __init__(self, name='', balance=0, ori_bet=0, bet=0, bet_place='', strategy=''):
        self.name = name
        self.balance = balance
        self.ori_bet = ori_bet
        self.bet = bet
        self.bet_place = bet_place
        self.strategy = strategy
        self.win_cnt = 0
        self.lose_cnt = 0
        self.draw_cnt = 0
        self.streak = 0
        self.profit_loss = 0

    def betting(self):
        if self.balance - self.bet > 0:
            self.balance -= self.bet
        else:
            self.bet_place = 'bankrupt'

        return self.bet_place

    def martin(self, game_result=''):
        if game_result == 'win':
            self.bet = self.ori_bet
            self.win_cnt += 1
            self.streak += 1
        elif game_result == 'lose':
            self.bet = self.bet * 2
            self.lose_cnt += 1
            self.streak = 0
        elif game_result == 'draw':
            self.bet = self.bet
            self.draw_cnt += 1
            self.streak = 0

        print(f'name : {self.name} is {game_result}')

    def paroli(self, game_result=''):
        if game_result == 'win':
            self.bet = self.bet * 2
            self.win_cnt += 1
            self.streak += 1
        elif game_result == 'lose':
            self.bet = self.ori_bet
            self.lose_cnt += 1
            self.streak = 0
        elif game_result == 'draw':
            self.bet = self.bet
            self.draw_cnt += 1
            self.streak = 0

        print(f'name : {self.name} is {game_result}')

    def achieve(self, reward=0, result=''):
        self.balance += reward

        if self.strategy == 'martin':
            self.martin(result)
        elif self.strategy == 'paroli':
            self.paroli(result)

    def print_status(self):
        print(f'name : {self.name}, balance : {self.balance}, next bet_amount : {self.bet}')

    def print_cnt(self):
        print(f'name : {self.name}, win : {self.win_cnt}, lose : {self.lose_cnt}, draw : {self.draw_cnt}, streak : {self.streak}')

    def calculate_profit_loss(self):
        self.profit_loss = self.balance - self.ori_bet



user1 = User('Daniel', 1000000, 5000, 5000, 'player', 'paroli')
user2 = User('Jaina', 1000000, 5000, 5000, 'player', 'paroli')
user3 = User('John', 1000000, 5000, 5000, 'banker', 'martin')

users = [user1, user2, user3]
# users.append(user3)

round_num = 0
winning_results = ['player', 'banker', 'tie']
game_results = []

print('first user information:')
for user in users:
    user.print_status()
# play game for 19 rounds
for i in range(500):
    # time.sleep(2)
    round_num += 1
    result = {'round': round_num, 'winner': random.choice(winning_results)}
    game_results.append(result)

    print(f'\n round {round_num} result : {result}')

    for user in users:
        place = user.betting()

        if place == 'bankrupt':
            print(f"bankrupt : {user.name}")
        else:
            if place == result['winner']:
                user.achieve(user.bet * 2, 'win')
            elif 'tie' == result['winner']:
                user.achieve(user.bet, 'draw')
            else:
                user.achieve(0, 'lose')

    for user in users:
        user.print_status()

# save the game results to a JSON file
with open('game_results.json', 'w') as f:
    json.dump(game_results, f)

print("Final balances:")
for user in users:
    user.print_status()
    user.print_cnt()

# calculate profit/loss for each user and save to a JSON file
user_profits = []
for user in users:
    user.calculate_profit_loss()
    profit_loss = user.profit_loss
    profit_loss_type = 'profit' if profit_loss > 0 else 'loss'
    user_profit = {'name': user.name, 'balance': user.balance, 'profit_loss': profit_loss, 'type': profit_loss_type, 'strategy': user.strategy}
    user_profits.append(user_profit)

with open('result.json', 'w') as f:
    json.dump(user_profits, f)





for user in users:
    user.calculate_profit_loss()
    print(f"{user.name} {'profit' if user.profit_loss > 0 else 'loss'}: {user.profit_loss}")












