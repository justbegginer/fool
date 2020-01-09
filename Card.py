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
            self.name += "Черви"
        elif self.suit == "diamond":
            self.suit += "Буби"
        elif self.suit == "club":
            self.suit += "Крести"
        elif self.suit == "spade":
            self.suit += "Пики"

    @staticmethod
    def can_you_beat(this_card, your_card, main_suit):
        if your_card.suit == this_card and your_card.value > this_card.value:
            return True
        elif your_card.suit == main_suit:
            if this_card != main_suit or this_card.value < your_card.value:
                return True
        else:
            return False
