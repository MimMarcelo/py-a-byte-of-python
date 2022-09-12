# Operadores são símbolos que executam determinada funcionalidade
# + (mais)
print(3 + 5)
# - (menos)
print(50 - 24)
# * (multiplicação)
print(2 * 3)
# ** (potência)
print(3 ** 4)
# / (divisão)
print(13 / 3)
# // (divisão e piso)
print(13 // 3)
# % (resto > inglês: modulo)
print(13 % 3)
# < (menor que)
print( 2 < 3)
# > (maior que)
print( 3 > 3)
# <= (menor ou igual que)
print( 2 <= 3)
# >= (maior ou igual que)
print( 3 >= 3)
# == (igual a)
print( 2 == 3)
# != (é diferente de)
print( 2 != 3)
# not (não booleano)
print(not True)
# and (e booleano)
print(True and False)
# or (ou booleano)
print(True or False)
# << (move bits para esquerda > inglês: left shift)
# Realiza operação sobre o dado na base binária
# Ex. 2 é representado por 10 em binário, se mover o 10 para esquerda por dois dígitos temos
# 1000, o que significa o número 8 em decimal
print(2 << 2)
# >> (move bits para direita > inglês: right shift)
# Realiza operação sobre o dado na base binária
# Ex. 11 é representado por 1011 em binário, se mover o 1011 para esquerda por um dígito temos
# 101, o que significa o número 5 em decimal
print(11 >> 1)
# & (bit a bit e > inglês: bitwise and)
# Avalia dois números em base binária, comparando cada uma das suas posições para gerar um novo
# número
# 3 & 5 são representados por 0101 & 0011
# Comparando cada uma das posições dos dígitos binários e, se forem iguais 1,
# se forem diferentes 0, temos:
# 0101
# 0011
# 0001 Apenas a última posição é igual (1), os demais são zeros, resultando em 1 (base decimal)
print(5 & 3)
# | (bit a bit ou > inglês: bitwise or)
# Compara as posições das represerntações binárias dos números para gerar um novo número
# Se ambas as posições são zero, então zero, senão, então 1
# 5 | 3 são representados por 0101 | 0011
# 0101
# 0011
# 0111 Apenas a primeira posição tem zeros em ambos, os demais 1, portanto: 7 na base decimal
print(5 | 3)
# ^ (bit a bit ou exclusivo > inglês: bitwise xor)
# Compara as posições das representações binárias dos números para gerar um novo número
# Se ambas as posições forem iguais, então zero, senão, então 1
# 5 ^ 3 são representados por 0101 | 0011
# 0101
# 0011
# 0110 A primeira e última posições são diferentes, portanto: 6 na base decimal
print(5 ^ 3)
# ~ (inversor bit a bit > inglês: bitwise invert)
# É dado por -(x+1). Veja mais em: http://stackoverflow.com/a/11810203
print(~4)