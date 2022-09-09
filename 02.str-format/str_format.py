# Cria variáveis
age = 33
name = "Marcelo Júnior"

# Imprime na tela sobrescrevendo as {chaves} por seus respectivos argumentos da função format()
print("{0} tinha {1} anos quando começou a estudar Python.".format(name, age))
print("Porque {0} está aprendendo Python?".format(name))

# Também é possível suprimir os números dos argumento contanto que sejam solicitados na mesma ordem (e quantidade) listada em format()
print("Aos {} anos, {} quer se qualificar e se tornar mais versátil no mundo da programação.".format(age, name))

# Também é possível nomear os parâmetros de format()
print("Tudo muda aos {number} anos".format(number=age))

# A partir do Python 3.6 também é possível utilizar as chamadas f-strings
print(f"{name} quer ser um professor melhor!") # Repare o 'f' no início da string

# Determinando a quantidade de casas decimais
print(f"Eu queria R$ {age:.2f}")

# A função print(), por padrão, termina com uma quebra de linha, para previnir isso, substitua o parâmetro end da função
print("M", end="")
print("a", end="")
print("r", end="")
print("c", end="")
print("e", end="")
print("l", end="")
print("o")