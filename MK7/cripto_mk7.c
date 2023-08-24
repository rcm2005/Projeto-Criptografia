#include <stdio.h>
#include <string.h>


int contaDigitos(int numero) {
    int contador = 0;
    while (numero != 0) {
        numero /= 10;
        contador++;
    }
    return contador;}

int addigits(int numero, int array){
    int controle = 0;
    while (numero != 0){
        numero /= 10;
        
    }

}

typedef struct {
    char key;
    int value;
} KeyValuePair;

// Array de estruturas contendo os pares chave-valor
KeyValuePair mapping[] = {
    {'A', 1}, {'B', 2}, {'C', 3}, {'D', 4}, {'E', 5}, {'F', 6}, {'G', 7}, {'H', 8}, {'I', 9}, {'J', 0},
    {'K', 1}, {'L', 2}, {'M', 3}, {'N', 4}, {'O', 5}, {'P', 6}, {'Q', 7}, {'R', 8}, {'S', 9}, {'T', 0},
    {'U', 1}, {'V', 2}, {'W', 3}, {'X', 4}, {'Y', 5}, {'Z', 6}, {'�', 7}, {'a', 8}, {'b', 9}, {'c', 0},
    {'d', 1}, {'e', 2}, {'f', 3}, {'g', 4}, {'h', 5}, {'i', 6}, {'j', 7}, {'k', 8}, {'l', 9}, {'m', 0},
    {'n', 1}, {'o', 2}, {'p', 3}, {'q', 4}, {'r', 5}, {'s', 6}, {'t', 7}, {'u', 8}, {'v', 9}, {'w', 0},
    {'x', 1}, {'y', 2}, {'z', 3}, {'�', 4}, {'�', 5}, {',', 6}, {'.', 7}, {'*', 8}, {'�', 9}, {'�', 0},
    {'�', 1}, {'�', 2}, {'�', 3}, {'�', 4}, {'�', 5}, {'�', 6}, {'�', 7}, {'�', 8}, {'�', 9}, {'�', 0},
    {'�', 1}, {'�', 2}, {'�', 3}, {'�', 4}, {'�', 5}, {'�', 6}, {'�', 7}, {'�', 8}, {'�', 9}, {'�', 0},
    {'�', 1}, {'�', 2}, {'�', 3}, {'�', 4}
};

// Fun��o para procurar o caractere no array de estruturas e retornar o valor associado
int find_value(char key) {
    for (int i = 0; i < sizeof(mapping) / sizeof(mapping[0]); i++) {
        if (mapping[i].key == key) {
            return mapping[i].value;
        }
    }
    return -1; // Valor padr�o se a chave n�o for encontrada
}

int main() {
    //char input = 'A';
    //int value = find_value(input);
    //if (value != -1) {
    //    printf("Valor associado ao caractere '%c': %d\n", input, value);
    //}
    //else {
    //    printf("Caractere n�o encontrado no mapeamento.\n");
    //}

    printf("************************************\n");
    printf("Seja bem vindo ao disco de c�sar MK7\n");
    printf("************************************\n");

    char palavra;                                                                                                                               
    int chave;
    int espaco;

    printf("Digite a mensagem: \n");
    scanf("%s", &palavra);
    printf("Digite a chave do codigo(numeros e letras: \n");
    scanf("%d", &chave);
    printf("Deseja inserir espa�os entre as palavras criptografadas ?: \n");
    scanf("%d", &espaco);

    int tamanholista = strlen(palavra);

    char arrayletras[tamanholista + 1]; //adicionando um numero adicional para agregar o caractere nulo do fim do array \0

    strcpy(arrayletras, palavra);


    char alfabeto[64] = "Aa,BbC.c/Dd*Ee/Ff0Gg1Hh2Ii3Jj4Kk5LlMmNnOoPpQqRrSsTtUuVvWwXxYyZz";


    
    int lenchave = contaDigitos(chave);




    // strcpy(chaveiro, chave);

    int andamento = 0;
    int c = 0;

    for(int i = 0; i > tamanholista; i++){
        char convert = arrayletras[i];
        int positioncyp = 0;

        int lenchaveiro = 
        
    }

    return 0;
}