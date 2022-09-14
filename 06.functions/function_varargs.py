def total(a = 5, *numbers, **phonebooks):
    print("a =", a)

    # Percorre todos os valores em *numbers
    for single_item in numbers:
        print("Single item: ", single_item)

    # Percorre todos os valores em **phonebooks
    for first, second in phonebooks.items():
        print(first, second)

total(10, 1, 2, 3, 5, Jack = 1123, John = 2231, Inge = 1560)