import math

def descripto():
    palavra = input("Digite a mensagem que gostaria de decodificar: ")
    chave = input("Digite a chave da codigo: ")

    chaveiro = list(chave)

    mapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 0,
        'K': 1, 'L': 2, 'M': 3, 'N': 4, 'O': 5, 'P': 6, 'Q': 7, 'R': 8, 'S': 9, 'T': 0,
        'U': 1, 'V': 2, 'W': 3, 'X': 4, 'Y': 5, 'Z': 6, 'Ç': 7, 'a': 8, 'b': 9, 'c': 0,
        'd': 1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 0,
        'n': 1, 'o': 2, 'p': 3, 'q': 4, 'r': 5, 's': 6, 't': 7, 'u': 8, 'v': 9, 'w': 0,
        'x': 1, 'y': 2, 'z': 3, 'Ç': 4, 'ç': 5, ',': 6, '.': 7, '*': 8, 'Á': 9, 'á': 0,
        'É': 1, 'é': 2, 'Í': 3, 'í': 4, 'Ó': 5, 'ó': 6, 'Ú': 7, 'ú': 8, 'Ã': 9, 'ã': 0,
        'Õ': 1, 'õ': 2, 'Â': 3, 'â': 4, 'Ê': 5, 'ê': 6, 'Î': 7, 'î': 8, 'Ô': 9, 'ô': 0,
        'Û': 1, 'û': 2, 'À': 3, 'à': 4
    }

    chaveiro = list(map(lambda x: mapping.get(x, x), chaveiro))
    
    element = ' '
    while element in chaveiro:
        chaveiro.remove(element)

    for s in range (len(chaveiro)):
        chaveiro[s] = int(chaveiro[s])

    
    mensagem = list(palavra) 

    
    palavradescrypto = []


    alfabeto = ['A', 'a', 'B', '0', 'b', 'C', '1', 'c', 'D', '2', 'd', 'E', '3', 'e', 'F', '4', 'f', 'G', '5', 'g', 'H', '6', 'h', 'I', '7', 'i', 'J', '8', 'j', 'K', '9', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ç', 'ç', ',', '.', '*', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ã', 'ã', 'Õ', 'õ', 'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û', 'À', 'à']  
    
    
    c = 0
    
    
    andamento = 0 #definindo variavel que indica quantas casas nós giramos no disco
    for o in range(len(mensagem)):
        deconvert = mensagem[o]  #a letra que vai ser convertida agora
        posicaocyp = 0 #armazenar a posição da nossa letra traduzida na cifra
        posicaoori = 0 #armazenar a posição origina da nossa letra no alfabeto
        
        lenghtchaveiro = len(chaveiro)
    
            
        casas = chaveiro [c] #definindo quantas casas serão voltadas
        
        if mensagem[o] == ' ':
            palavradescrypto.append(' ')
        
       

        for i in range(len(alfabeto)):#definindo a letra i como as posições do alfabeto
            if mensagem[o] == alfabeto[i]:#encontrando a posição da nossa letra dentro do alfabeto
                andamento += casas % len(alfabeto)
                posicaoori = (((i - andamento) + len(alfabeto))% len(alfabeto)) #definindo a posição da letra convertida dentro da cifra
                posicaocyp = i #apenas para orientar onde estaria a letra sem converter no alfabeto normal
                converted = alfabeto[posicaoori]#definindo a letra original dentro da cifra
                palavradescrypto.append(converted) #adicionando a letra a lista de letras que compõe a palavra criptografada
                c = (c + 1) % len(chaveiro)
                if c == 0:
                    andamento = 0
                break
    
    frasedecrypto = "" #adicionando variável que armazenará a frase concatenada após a encodificação
         
    for p in range(len(palavradescrypto)):
        frasedecrypto += palavradescrypto[p]
            
    chavetrans = sorted(chaveiro)
    
    

    print(frasedecrypto)
descripto()
