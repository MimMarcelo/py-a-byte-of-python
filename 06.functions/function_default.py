def say(message, times = 1):
    print(message * times)

say("Hello")
say("Hello ", 5)

# Apenas os últimos parâmetros podem ter valores padrão,
# Não é possível ter parâmetros com valores padrão precedendo
# parâmetros que não possuam valor padrão