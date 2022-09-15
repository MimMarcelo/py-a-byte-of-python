import sys

# argv é uma lista de argumentos que são passados ao
# chamar a execução do arquivo, experimente executar:
# python3 07.modules/using_sys.py we are arguments

print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is", sys.path)