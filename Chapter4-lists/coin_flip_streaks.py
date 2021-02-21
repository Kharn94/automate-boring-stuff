import random

numberOfStreaks = 0
heads_row = ['heads', 'heads', 'heads', 'heads', 'heads', 'heads']
tails_row = ['tails', 'tails', 'tails', 'tails', 'tails', 'tails']

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    l_coin = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            l_coin.append('heads')
        else:
            l_coin.append('tails')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(100):
        if l_coin[j:j+6] == heads_row or l_coin[j:j+6] == tails_row:
            numberOfStreaks += 1

print('The number of streaks is :', numberOfStreaks)
print("Chance of streak: %s%%" % (numberOfStreaks / (100*10000)))
