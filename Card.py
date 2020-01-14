class Card:
    _value: int
    _suit: str
    name: str

    def __init__(self, value, suit):
        self._value = value
        self._suit = suit
        self.__check_suit()
        self.__give_name()

    @property
    def get_value(self):
        return self._value

    @property
    def get_suit(self):
        return self._suit

    def __check_suit(self):
        if not (self.get_suit == "diamond" or self.get_suit == "club" or
                self.get_suit == "spade" or self.get_suit == "heart"):
            raise ValueError

    def __give_name(self):
        # записываем значение карты
        if self.get_value < 11:
            self.name = str(self.get_value)
        elif self.get_value == 11:
            self.name = "Валет"
        elif self.get_value == 12:
            self.name = "Дама"
        elif self.get_value == 13:
            self.name = "Король"
        elif self.get_value == 14:
            self.name = "Туз"
        # записываем масть
        # переменная отвечающая за масть именуеться на английском , а в имени - на русском
        if self.get_suit == "heart":
            self.name += " Черви"
        elif self.get_suit == "diamond":
            self.name += " Буби"
        elif self.get_suit == "club":
            self.name += " Крести"
        elif self.get_suit == "spade":
            self.name += " Пики"

    def can_you_beat(self, this_card, main_suit):
        if self.get_suit == this_card.get_suit:
            if self.get_value > this_card.get_value:
                return True
            else:
                return False
        elif self.get_suit == main_suit:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name
