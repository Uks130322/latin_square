def latin_square_three() -> str:
    """
    :return: Create latin square three*three
    """
    import random

    letters = ['A', 'B', 'C']
    random.shuffle(letters)
    square = list(letters) + ['\n']

    for i in range(2):
        letters = [letters[i - 1] for i in range(len(letters))]
        square.extend(letters + ['\n'])

    return "".join(square)


print(latin_square_three())