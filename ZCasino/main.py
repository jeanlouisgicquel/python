from ask import ask_number
from random import randrange


def ask_mise(money):
    while True:
        try:
            mise = ask_number('Quelle est votre mise ?', 0, money)
            return mise
        except ValueError as e:
            print(e)
            pass


def ask_numero():
    while True:
        try:
            num = ask_number(
                'Sur quel numéro allez-vous miser (entre 0 et 49) ?', 0, 49)
            return num
        except ValueError as e:
            print(e)
            pass


def color(nb):
    if nb % 2 == 0:
        return 'noir'
    else:
        return 'rouge'


def play(money):
    '''
    Miser et lancer la roulette

    @return montant perdu ou gagné
    '''
    print('Vous disposez de', money, '€')
    mise = ask_mise(money)
    print('Votre mise est de ', mise, '€')
    num = ask_numero()
    print('Votre numéro est le ', num)
    num_color = color(num)
    print('il serait de couleur', num_color)
    print('La roulette tourne...')
    winner = randrange(0, 49)
    winner_color = color(winner)
    print('Le numéro gagnant est le', winner, 'de couleur', winner_color)
    if num == winner:
        print('Vous avez gagné !!!')
        return mise * 3
    elif num_color == winner_color:
        print('Vous avez la bonne couleur')
        return mise * 0.5
    else:
        print('Désolé, vous avez perdu')
        return -mise


if __name__ == "__main__":
    money = 600
    while True:
        money += play(money)
        print('money', money, '€ restant')
        if money == 0:
            print('Vous avez perdu, vous ne pouvez plus miser')
            break
        res = input('Voulez rejouer ? (tapez "n" pour arreter) ')
        if res == 'n' or res == 'non':
            break
    print("Merci d'avoir joué")
    print("Vous avez terminé la partie, il vous reste", money, '€')
