import pickle
"""Armazena objetos em arquivos"""
# O nome do arquivo que armazenará o objeto
shoplistfile = "shoplist.data"

# Lista de coisas para comprar
#shoplist = ["Apple", "Mango", "Carrot"]
shoplist = ["Maçã", "Manga", "Melão"]

# Escreve no arquivo
f = open(shoplistfile, "wb")
# Lança os objetos no arquivo
pickle.dump(shoplist, f, -1)
f.close()

# Destroi a variável shoplist
del shoplist

# Lê os dados armazenados
f = open(shoplistfile, "rb")
# Carrega os dados do arquivo para a variável
storedlist = pickle.load(f)
print(storedlist)
f.close()