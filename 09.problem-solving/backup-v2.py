import os
import time

# Os arquivos e pastas são mantidos em uma lista
source = ["/home/marcelo/Projects/python"]

# Determinar o diretório que deve armazenar o backup
target_dir = "/home/marcelo/Backup"

# Cria o diretório de destino caso ainda não exista
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# Os arquivos serão armazenados em um arquivo .zip
# que serão armazenados em um subdiretório com a data do dia
today = target_dir + os.sep + time.strftime("%Y%m%d")

# Cria o diretório de destino caso ainda não exista
if not os.path.exists(today):
    os.mkdir(today)

# O nome do arquivo será a hora atual
now = time.strftime("%H%M%S")

# O nome do arquivo .zip com seus subdiretórios
target = today + os.sep + now + ".zip"

# Usa o comando zip para compactar os arquivos
zip_command = "zip -r {0} {1}".format(target,' '.join(source))

# Executa o backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup failed")