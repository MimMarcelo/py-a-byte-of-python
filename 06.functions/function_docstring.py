def print_max(x, y):
    '''Imprime o maior dos valores informados.

    Compara os valores e imprime o maior.
    '''
    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")

print_max(3, 5)
print(print_max.__doc__)
help(print_max)