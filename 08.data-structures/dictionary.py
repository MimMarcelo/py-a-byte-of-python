# Um dicionário é especificado entre {} e contém pares de
# chave: valor
# Um dicionário não pode ser ordenado de qualquer maneira
# Se é desejada uma ordenação específica, faça-a antes de
# Criar o dicionário

# Um dicionário é uma instância de dict

# ab é uma sigla para Address Book
ab = {
    "Marcelo": "marcelo@gmail.com",
    "Ana": "carol@gmail.com",
    "Rebeca": "rebeca@gmail.com",
    "Gabriel": "gabriel@gmail.com"
}

print("Marcelo's e-mail:", ab["Marcelo"])

# Deletando uma chave
del ab["Rebeca"]

print("\nThere are {} contacts in the address-book\n".format(len(ab)))

for name, address in ab.items():
    print(f"Contact {name} at {address}")

# Adicionando uma nova chave
ab["Cecília"] = "cecilia@gmail.com"

if "Cecília" in ab:
    print(f"\nCecília's address is {ab['Cecília']}")