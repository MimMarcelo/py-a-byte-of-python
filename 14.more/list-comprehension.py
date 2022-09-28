# Usado para derivar uma lista de outra já existente

# Por exemplo: Obter uma lista com os números multiplicados
# por 2 somente dos números que forem maiores que 3
list = [2, 3, 4, 5]

list_two = [2*i for i in list if i > 3]

print(list_two)