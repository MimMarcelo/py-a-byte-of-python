def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return clear_text(text) == clear_text(reverse(text))

def clear_text(text):
    """Remove caracteres especiais do texto"""
    allowed = ("abcdefghijklmnopqrstuvwxyz")
    aux = ""
    for letter in text.lower():
        if letter in allowed:
            aux += letter
    return aux


something = input("Enter your text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")