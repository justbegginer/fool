class Card:
    value: int
    suit: str
    name: str

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.__give_name()

    def __give_name(self):
        # записываем значение карты
        if self.value < 11:
            self.name = str(self.value)
        elif self.value == 11:
            self.name = "Валет"
        elif self.value == 12:
            self.name = "Дама"
        elif self.value == 13:
            self.name = "Король"
        elif self.value == 14:
            self.name = "Туз"
        # записываем масть
        # переменная отвечающая за масть именуеться на английском , а в имени - на русском
        if self.suit == "heart":
            self.name += " Черви"
        elif self.suit == "diamond":
            self.name += " Буби"
        elif self.suit == "club":
            self.name += " Крести"
        elif self.suit == "spade":
            self.name += " Пики"

    def can_you_beat(self, this_card, main_suit):
        if self.suit == this_card.suit:
            if self.value > this_card.value:
                return True
            else:
                return False
        elif self.suit == main_suit:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name
