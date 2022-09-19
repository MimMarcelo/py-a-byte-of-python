# Listas, tuplas e strings são sequências
shoplist = ["apple", "mango", "carrot", "banana", "grape"]
name = "Marcelo"

# Obtendo o valor através dos índices
print("Item 0 is", shoplist[0])
print("Item 1 is", shoplist[1])
print("Item 2 is", shoplist[2])
print("Item 3 is", shoplist[3])
print("Character 0 is", name[0])

# Informar um índice negativo obtém o valor a partir do final da sequência
# [-1] obtém o último valor da sequência
# [-2] obtém o penúltimo valor da sequência e assim sucessivamente
# Não é circular, também acontece IndexOutOfBoundException para índices negativos
print("Item -1 is", shoplist[-1])
print("Item -2 is", shoplist[-2])

# Partindo uma lista
# Indica a partir de que posição (inclusive) até que posição (não inclusive)
print("Items 1 to 3 are", shoplist[1:3])
print("Items 2 to end are", shoplist[2:])
print("Items 1 to -1 are", shoplist[1:-1])
print("Items start to end are", shoplist[:])

# Partindo uma string
print("Characters 1 to 3 are", name[1:3])
print("Characters 2 to end are", name[2:])
print("Characters 1 to -1 are", name[1:-1])
print("Characters start to end are", name[:])

# Também é possível passar um terceiro parâmetro,
# que indica o 'step' da subsequência
print(shoplist[::2]) # obtém as posições 0, 2, 4...