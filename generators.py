from Card import Card
from Player import Player
import random


def generate_deck(deck_size ):
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
    deck_size = len(deck) - 1  # because randint includes second number
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
