import random


def play(deck, players):
    while len(players) > 0:

        if deck:
            take_card()


def take_card(players, deck):
    for i in range(len(players)):
        while len(players[i].deck) < 6 and deck:
            random_number = random.randint(0, len(deck) - 1)
            players[i].append(random_number)
            deck.pop(random_number)
