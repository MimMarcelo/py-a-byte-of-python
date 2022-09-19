# Recomenda-se sempre o uso de parênteses para definir uma tupla
# Mesmo que o uso dos parênteses seja opcional
# Explícito é melhor que implícito
zoo = ("Python", "Elefante", "Penguin")
print("Number of animals in the zoo is", len(zoo))

# Tuplas são imutáveis e não são tão versáteis quanto as listas
# São indicadas em casos onde se pode assumir com segurança
# que a coleção de valores não mudará

new_zoo = ("Monkey", "Camel", zoo)
print("Number of cages in the new zoo is", len(new_zoo))
print("All animals in new zoo are", new_zoo)
print("Animals brought from old zoo are", new_zoo[2])
print("Last animal brought fron old zoo is", new_zoo[2][2])
print("Number of animal in the new zoo is", (len(new_zoo)-1+len(new_zoo[2])))