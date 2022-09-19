# Set é uma coleção simples de objetos.
# Com Set é possível verificar relacionamentos e
# operações de conjuntos
countries = set(["Brazil", "France", "Peru"])
if "France" in countries:
    print("France is in the set")

if "USA" in countries:
    print("USA is in the set")
else:
    print("USA is not in the set")

# Cria uma cópia sem apontar para a mesma referência
countries2 = countries.copy()
countries2.add("USA")
if countries2.issuperset(countries):
    print("It is")

countries.remove("Peru")
print(countries2 & countries) # Interseção