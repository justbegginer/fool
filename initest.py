import unittest
from Card import Card
from Player import Player


class MyTestCase(unittest.TestCase):

    def test_Players_deck_func(self):
        first_card = Card(10, "diamond")
        second_card = Card(10, "diamond")
        self.assertEqual(first_card, second_card, "Cards don't equal")
        second_card = Card(11, "diamond")
        test_deck = [first_card, second_card]
        player = Player("?", test_deck)
        self.assertEqual(first_card, player.pop_card(0))
        self.assertEqual(len(player), 1)
        player.remove_card(second_card)
        self.assertEqual(len(player), 0)

    def test_Card_func(self):
        first_card = Card(10, "diamond")
        second_card = Card(11, "diamond")
        main_suit = "diamond"
        self.assertEqual(second_card.can_you_beat(first_card, main_suit), True)
        second_card = Card(6, "club")
        main_suit = "club"
        self.assertEqual(second_card.can_you_beat(first_card, main_suit), True, f"{second_card.suit}  {main_suit}")
        first_card = Card(10, "club")
        self.assertEqual(second_card.can_you_beat(first_card, main_suit), False,
                         f"{second_card.suit} + {second_card.value}    {first_card.suit} + {first_card.value}  {main_suit}")


if __name__ == '__main__':
    unittest.main()
