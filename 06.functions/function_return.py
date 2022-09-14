from pprint import pp


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal"
    else:
        return y

print("Maximum:", maximum(2, 3))