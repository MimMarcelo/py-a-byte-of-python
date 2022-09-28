# É possível receber tuplas, dicionários ou um número variável de argumentos em funções

# Um « * » permite receber uma tupla
# Usar dois « ** » permite receber um dicionário
def powersum(power, *args):
    ''' Retorna a soma das potências dos números informados'''
    total = 0
    for i in args:
        total += pow(i, power)

    return total

print(powersum(2, 2, 2))

# É o equivalente à powersum(2, (2, 3, 4, 5)))
print(powersum(2, 2, 3, 4, 5))
