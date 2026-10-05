arquivo = open("diario.txt", "r")
for numero, linha in enumerate(arquivo, 1):
    print(numero,linha.strip())
arquivo.close()
