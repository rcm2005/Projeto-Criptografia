import math


def codificar():

    print('************************************')
    print('Seja bem vindo ao disco de césar MK4')
    print('************************************')
    
    palavra = input("Digite a mensagem: ")
    chave = int(input('digite a chave do codigo (sem espaços, maximo 4 digitos): '))
    espaco = (int(input("deseja mostrar espaços entre as palavras criptografadas ? :\n 1 - sim \n 2 - não\n")))
    
    cemk = chave // 100000
    restocemk = chave % 100000
    dezk = restocemk // 10000
    restodezk = restocemk % 10000
    milhar = restodezk//1000
    restom = restodezk %1000
    centena = restom//100
    restoc = restom%100
    dezena = restoc // 10
    unidade = restoc %10

    chaveiro = [cemk, dezk, milhar, centena, dezena, unidade]


    mensagem = list(palavra) 

    if espaco == 2:
        element = " "
        while element in mensagem:
    
            mensagem.remove(element)


    
    palavracrypto = []

    alfabeto = ['A', 'a', 'B', '0', 'b', 'C', '1', 'c', 'D', '2', 'd', 'E', '3', 'e', 'F', '4', 'f', 'G', '5', 'g', 'H', '6', 'h', 'I', '7', 'i', 'J', '8', 'j', 'K', '9', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ç', 'ç', ',', '.', '*', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ã', 'ã', 'Õ', 'õ', 'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û', 'À', 'à']  
    print(len(alfabeto))
    c = 0
    
    
    andamento = 0 #definindo variavel que indica quantas casas nós giramos no disco
    for o in range(len(mensagem)):
        convert = mensagem[o]  #a letra que vai ser convertida agora
        posicaocyp = 0 #armazenar a posição da nossa letra traduzida na cifra
        posicaoori = 0 #armazenar a posição origina da nossa letra no alfabeto
        
        lenghtchaveiro = len(chaveiro)
    
            
        casas = chaveiro [c] #definindo quantas casas serão andadas
        
        
        
        if espaco == 1:
            if mensagem[o] == ' ':
                    palavracrypto.append(' ')

        for i in range(len(alfabeto)):#definindo a letra i como as posições do alfabeto
            if mensagem[o] == alfabeto[i]:#encontrando a posição da nossa letra dentro do alfabeto
                    andamento += casas % len(alfabeto)
                    posicaocyp = (i + andamento) % len(alfabeto) #definindo a posição da letra convertida dentro da cifra
                    posicaoori = i #apenas para orientar onde estaria a letra sem converter no alfabeto normal
                    converted = alfabeto[posicaocyp]#definindo a letra convertida dentro da cifra
                    palavracrypto.append(converted) #adicionando a letra a lista de letras que compõe a palavra criptografada
                    c = (c + 1) % len(chaveiro)
                    if c == 0:
                        andamento = 0
                    break
    
    frasecrypto = "" #adicionando variável que armazenará a frase concatenada após a encodificação
        
    for p in range(len(palavracrypto)):
        frasecrypto += palavracrypto[p]
        
    

    return frasecrypto

resultado = codificar()
print(resultado)

    
    