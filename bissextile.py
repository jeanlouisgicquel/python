def is_bissextile(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


while True:
    annee = input("Quelle année ? (s pour stop) ")
    if annee == 's':
        break

    annee = int(annee)
    if is_bissextile(annee):
        print(annee, 'est bissextile !')
    else:
        print(annee, "n'est pas bissextile")
