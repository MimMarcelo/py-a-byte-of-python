# Em Python é possível passar dois ou mais valores no retorno de uma função
# Basta realizar o retorno como uma tupla

def get_error():
    return (3, "Details")

# Recebe os valores na mesma ordem que o especificado no retorno da função
errnum, errmsg = get_error()

print(f"Error Code: {errnum}")
print(f"Error Message: {errmsg}")