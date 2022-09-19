# Listas são definidas por colchetes e seus itens são separados po ","
# Listas são tratadas como objetos em Python
shoplist = ["apple", "mango", "carrot", "banana"]

print("I have", len(shoplist), "itens to purchase.")

# end=" " previne a quebra de linhas padrão do print()
print("These itens are:", end=" ")
for item in shoplist:
    print(f"{item},", end=" ")

print("\nI also have to buy rice.")
shoplist.append("rice")

print("My shopping list is now", shoplist)

print("I will sort my list now")
shoplist.sort()
print("Sorted shopping list is", shoplist)

print("The first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0] # Deleta o item da lista, também serve para deletar variáveis...
print("I bought the", olditem)
print("My shopping list is now", shoplist)
print("The first item I will buy now is", shoplist[0])