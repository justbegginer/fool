import random
import generators as gen
from Card import Card
from Player import Player


def play(deck_size, count_of_players):
    deck = gen.generate_deck(deck_size)
    players = gen.generate_players(count_of_players, deck)
    index_of_main_card = random.randint(0, len(deck) - 1)
    main_card = deck[index_of_main_card]
    deck.pop(index_of_main_card)
    del index_of_main_card


def who_first(players, main_suit):
    index = 0
    min = None
    for player in range(len(players)):
        for card in players[player].get_deck:
            if card.get_suit == main_suit:
                if min == None or card.get_value < min:
                    min = card.get_value
                    index = player
    return index


def take_card(players, deck):
    for i in range(len(players)):
        while len(players[i].deck) < 6 and deck:
            random_number = random.randint(0, len(deck) - 1)
            players[i].append(random_number)
            deck.pop(random_number)
