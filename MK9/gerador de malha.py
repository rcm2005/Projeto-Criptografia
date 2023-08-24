alfabeto = ['A', 'a', 'B', '0', 'b', 'C', '1', 'c', 'D', '2', 'd', 'E', '3', 'e', 'F', '4', 'f', 'G', '5', 'g', 'H', '6', 'h', 'I', '7', 'i', 'J', '8', 'j', 'K', '9', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ç', 'ç', ',', '.', '*', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ã', 'ã', 'Õ', 'õ', 'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û', 'À', 'à']

linhas = len(alfabeto)
colunas = len(alfabeto)

for linha in range(linhas):
    for coluna in range(colunas):
        index = (linha + coluna) % colunas
        print(alfabeto[index], end=' ')
    print('\n')