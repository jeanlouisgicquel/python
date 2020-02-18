def ask_number(question, min=0, max=100):
    try:
        res = int(input(question + ' '))
        if res < min:
            error = str(res) + " doit être supérieur ou égal à " + str(min)
            raise ValueError(error)
        if res > max:
            error = str(res) + " doit être inférieur ou égal à " + str(max)
            raise ValueError(error)
        return res

    except ValueError as e:
        raise e


if __name__ == "__main__":
    number = ask_number('ask_number', 0, 49)
    print(number)
