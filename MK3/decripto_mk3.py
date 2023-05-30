import math

def descripto():
    palavra = input("Digite a mensagem que gostaria de decodificar: ")
    chave = int(input("Digite a chave da codigo: "))

    milhar = chave//1000
    restom = chave %1000
    centena = restom//100
    restoc = restom%100
    dezena = restoc // 10
    unidade = restoc %10

    chaveiro = [milhar, centena, dezena, unidade]

    letra = list(palavra) 

    
    palavradescrypto = []


    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', ',', '.', '0', '1', '*', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'î', 'ô', 'û', 'à']  
    
    
    c = 0
    
    
    andamento = 0 #definindo variavel que indica quantas casas nós giramos no disco
    for o in range(len(letra)):
        deconvert = letra[o]  #a letra que vai ser convertida agora
        posicaocyp = 0 #armazenar a posição da nossa letra traduzida na cifra
        posicaoori = 0 #armazenar a posição origina da nossa letra no alfabeto
        
        lenghtchaveiro = len(chaveiro)
    
            
        casas = chaveiro [c] #definindo quantas casas serão voltadas
        
        if letra[o] == ' ':
            palavradescrypto.append(' ')
        
       

        for i in range(len(alfabeto)):#definindo a letra i como as posições do alfabeto
            if letra[o] == alfabeto[i]:#encontrando a posição da nossa letra dentro do alfabeto
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
            
    print(frasedecrypto)
descripto()
