class Card:
    _value: int
    _suit: str
    name: str

    def __init__(self, value, suit):
        self._value = value
        self._suit = suit
        self.__give_name()

    def get_value(self):
        return self._value

    def get_suit(self):
        return self._suit

    def __give_name(self):
        # записываем значение карты
        if self._value < 11:
            self.name = str(self._value)
        elif self._value == 11:
            self.name = "Валет"
        elif self._value == 12:
            self.name = "Дама"
        elif self._value == 13:
            self.name = "Король"
        elif self._value == 14:
            self.name = "Туз"
        # записываем масть
        # переменная отвечающая за масть именуеться на английском , а в имени - на русском
        if self._suit == "heart":
            self.name += " Черви"
        elif self._suit == "diamond":
            self.name += " Буби"
        elif self._suit == "club":
            self.name += " Крести"
        elif self._suit == "spade":
            self.name += " Пики"

    def can_you_beat(self, this_card, main_suit):
        if self._suit == this_card.suit:
            if self._value > this_card.value:
                return True
            else:
                return False
        elif self._suit == main_suit:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name
