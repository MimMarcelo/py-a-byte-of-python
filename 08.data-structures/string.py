# This is a string object
name = "Marcelo"

if name.startswith("Mar"):
    print("Yes, the string starts with 'Mar'")

if 'a' in name:
    print("Yes, it contains the string 'a'")

if name.find("rce") != -1:
    print("Yes, it contains the string 'rce'")

delimiter = "_&_"
countries = ["Brazil", "France", "Peru", "Japan", "Canada"]
print(delimiter.join(countries))