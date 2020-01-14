from Card import Card


class Player:
    _name: str
    _deck: list

    def __init__(self, name, his_deck):
        self._name = name
        self._deck = his_deck

    @property
    def get_deck(self):
        return self._deck

    @property
    def get_name(self):
        return self._name

    def remove_card(self, card):
        self._deck.remove(card)

    def append_card(self, card):
        self._deck.append(card)

    def pop_card(self, index):
        return self._deck.pop(index)

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return self._deck
