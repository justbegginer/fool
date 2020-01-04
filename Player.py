from Card import Card


class Player:
    name: str
    his_deck: Card

    def __init__(self, name, his_deck):
        self.name = name
        self.deck = his_deck
