import sh
import color, game


class Card:
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


class Player:
    def __init__(self, name, his_deck):
        self.name = name
        self.deck = his_deck

def generate_deck(deck_size):
    from_value = 6# from value = 6 for default deck
    if deck_size == 52:
        from_value = 2
    deck = []
    for i in range(from_value , 15):
        deck.append(Card(i , "heart"))
        deck.append(Card(i , "diamond"))
        deck.append(Card(i , "club"))
        deck.append(Card(i, "spade"))
    return deck

def generate_players(count_of_players):
    players = []
    for _ in range(count_of_players):
        players.append(Player)


print("давай сыграем")
deck_size = 0
while True:
    print("выберите колоду в 36 или 52 карты")
    try:
        deck_size = int(input())
        assert deck_size == 36 or deck_size
    except AssertionError:
        print()
print("назовите число игроков")
persons = 0
while True:
    try:
        persons = int(input())
        assert (persons <= 6 and deck_size == 36) or \
               (persons <= 8 and deck_size == 52)
    except ValueError:
        color.red("вы ввели не число,попробуйте снова")
    except AssertionError:
        color.red("слишком много игроков для колоды")


