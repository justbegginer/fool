from Card import Card


class Player:
    name: str
    deck: list

    def __init__(self, name, his_deck):
        self.name = name
        self.deck = his_deck

    def remove_card(self, card):
        self.deck.remove(card)

    def append_card(self , card):
        self.deck.append(card)

    def pop_card(self, index):
        return self.deck.pop(index)
