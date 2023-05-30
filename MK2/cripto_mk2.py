import math


def codificar():

    palavra = input("Digite a mensagem (não use acentos): ")
    chave = int(input('digite a chave do codigo (sem espaços, maximo 4 digitos): '))
    espaco = (int(input("deseja mostrar espaços entre as palavras criptografadas ? :\n 1 - sim \n 2 - não\n")))
    
    milhar = chave//1000
    restom = chave %1000
    centena = restom//100
    restoc = restom%100
    dezena = restoc // 10
    unidade = restoc %10

    chaveiro = [milhar, centena, dezena, unidade]

    letra = list(palavra) 

    if espaco == 2:
        element = " "
        while element in letra:
    
            letra.remove(element)


    
    palavracrypto = []


    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', ',', '.', '0', '1', '*']

    c = 0
    
    
    andamento = 0 #definindo variavel que indica quantas casas nós giramos no disco
    for o in range(len(letra)):
        convert = letra[o]  #a letra que vai ser convertida agora
        posicaocyp = 0 #armazenar a posição da nossa letra traduzida na cifra
        posicaoori = 0 #armazenar a posição origina da nossa letra no alfabeto
        
        lenghtchaveiro = len(chaveiro)
    
            
        casas = chaveiro [c] #definindo quantas casas serão andadas
        
        
        
        if espaco == 1:
            if letra[o] == ' ':
                    palavracrypto.append(' ')

        for i in range(len(alfabeto)):#definindo a letra i como as posições do alfabeto
            if letra[o] == alfabeto[i]:#encontrando a posição da nossa letra dentro do alfabeto
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

    
    