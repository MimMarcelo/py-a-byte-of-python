import sys
# A funcão << dir() >> retorna a lista dos nomes definidos em um objeto
# Se esse objeto é um módulo, listará suas funções, classes e variáveis
print("Nomes acessíveis do módulo << sys >>")
print(dir(sys))

# Se não for informado nenhum argumento, será retornada a lista de nomes
# do módulo atual
print("\n\nNomes acessíveis do módulo atual")
print(dir())

# Nomes da classe << str >> (String)
print("\n\nNomes acessíveis da classe str")
print(dir(str))