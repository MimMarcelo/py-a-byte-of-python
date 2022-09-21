poem = """\
Programming is fum
When the work is done
if you wanna make your work also fun:
    use Python!
"""
# Os modos possíveis de abrir um arquivo em Python são:
# - r ler
# - w escrever
# - a adicionar

# Abre o arquivo para escrita (w)
f = open("poem.txt", "w")
# Escreve o texto no arquivo
f.write(poem)
# Fecha o arquivo
f.close()

# Se nenhum modo for especificado,
# O modo de leitura (r) é o padrão
f = open("poem.txt")
while True:
    line = f.readline()
    # Zero indica o fim do arquivo (EOF)
    if len(line) == 0:
        break
    # A variável line já tem uma nova linha
    # Ao final de cada linha
    # Desde que ele esteja lendo de um arquivo
    print(line, end="")

# Fecha o arquivo
f.close()