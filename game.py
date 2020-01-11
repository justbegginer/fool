import random
from Card import Card
from Player import Player


def play(deck_size, count_of_players):
    deck = generate_deck(deck_size)
    players = generate_players(count_of_players, deck)
    while len(players) > 0:


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


def generate_players(count_of_players, deck):
    deck_size = len(deck) - 1  # because randint includes
    players = []
    for i in range(count_of_players):
        users_deck = []
        for _ in range(6):
            random_card = random.randint(0, deck_size)
            users_deck.append(deck[random_card])
            deck.pop(random_card)
            deck_size -= 1
        players.append(Player(input(f"Назовите имя {i + 1}"), users_deck))
    return players
