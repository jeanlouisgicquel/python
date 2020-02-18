
def table(nb, max=10):
    print('Affichage de la table de ', nb)
    i = 1
    while i <= max:
        res = nb * i
        print(nb, ' * ', i, ' = ', res)
        i += 1


if __name__ == "__main__":
    table(4)