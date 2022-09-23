class ShortInputException(Exception):
    """Uma classe de exceção criada pelo usuário"""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input("Enter something: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Why did you do an EOF on me?")
except ShortInputException as ex:
    print(f"ShortInputException: The input was \
{ex.length} long, expected at least {ex.atleast}")
else:
    print("No exception was raised")