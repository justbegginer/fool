import unittest
from Card import Card
from Player import Player
import game


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
        self.assertEqual(second_card.can_you_beat(first_card, main_suit), True, f"{second_card.get_suit}  {main_suit}")
        first_card = Card(10, "club")
        self.assertEqual(second_card.can_you_beat(first_card, main_suit), False,
                         f"{second_card.get_suit} + {second_card.get_value}    {first_card.get_suit} + {first_card.get_value}  {main_suit}")

    def test_who_first_func(self):
        first_player = Player("first", [Card(2, "diamond"), Card(6, "spade")])
        second_player = Player("second", [Card(4, "spade")])
        main_suit = "spade"
        self.assertEqual(game.who_first([first_player, second_player], main_suit), 1, "second player must move  first")


if __name__ == '__main__':
    unittest.main()
