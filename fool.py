import sh
import color, \
    colorama
import game

print("давай сыграем")
deck_size = 0
while True:
    try:
        deck_size = int(input("выберите колоду в 36 или 52 карты \n"))
        assert deck_size == 36 or deck_size == 52
    except AssertionError:
        color.red("колода должна содержать 36 или 52 карты")
    else:
        break
persons = 0
while True:
    try:
        persons = int(input("назовите число игроков \n"))
        assert (persons <= 6 and deck_size == 36) or \
               (persons <= 8 and deck_size == 52)
    except ValueError:
        color.red("вы ввели не число,попробуйте снова")
    except AssertionError:
        color.red("слишком много игроков для колоды")
    else:
        break

game.play(deck_size , persons)