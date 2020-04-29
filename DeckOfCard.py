import math
import numpy as np

suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"}

n = len(suits) * len(ranks)
deck = []
for i in range(len(ranks)):
    for j in range(len(suits)):
        deck[len(suits) * i + j] = ranks[i] + suits[j]

for i in range(n):
    r = i + (int)(math.random() * (n - i))
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

for i in range(4):
    for j in range(9):
        print(deck[i])
