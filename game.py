import random
from Card import Card
from Player import Player


def play(deck_size, count_of_players):
    players = generate_players(count_of_players)
    deck = generate_deck(deck_size)
    while len(players) > 0:
        if deck:
            take_card()


def take_card(players, deck):
    for i in range(len(players)):
        while len(players[i].deck) < 6 and deck:
            random_number = random.randint(0, len(deck) - 1)
            players[i].append(random_number)
            deck.pop(random_number)


def generate_deck(deck_size):
    from_value = 6  # from value = 6 for default deck
    if deck_size == 52:
        from_value = 2
    deck = []
    for i in range(from_value, 15):
        deck.append(Card(i, "heart"))
        deck.append(Card(i, "diamond"))
        deck.append(Card(i, "club"))
        deck.append(Card(i, "spade"))
    return deck


def generate_players(count_of_players):
    players = []
    for _ in range(count_of_players):
        players.append(Player)
