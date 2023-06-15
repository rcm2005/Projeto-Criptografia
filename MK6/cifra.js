function cripto(){
    var palavra = document.getElementById('msg').value;
    var chave = document.getElementById('chave').value; //adicionando variaveis que vão receber os valores oriundos do codigo html
    var espaco = document.getElementById('espaco').value;

    if (espaco != '1' && espaco != '2' ){
        alert("Por favor preencha todos os campos spc");
    }// fazendo verificações para identificar se todos os campos estão preenchidos e com digitos válidos
    if (palavra === ''){
        alert("Por favor, digite uma mensagem msg");
    }
    if (chave === 0 || isNaN(chave)){
        alert("Por favor, digite uma chave válida");
    }

    var chaveiro = [];
//definindo uma variável chaveiro para armazenar os valores contidos na chave
    for (let i = 0; i < chave.length; i++){
        chaveiro.push(parseInt(chave.charAt(i)));        //varrendo todos os digitos da chave
    }

    // for(let u = 0; u < chaveiro.leng; u++){
    //     if (chaveiro.charAt(u) == "a" || "á" || "à" || "ã" || "â" || "A" || "Á" || "À" || "b" || "B" || "U" || "" ){

    //     }
    // }
    
    var mensagem = palavra.split('');

    // if (espaco == '2'){
    //     for (e = 0; e < mensagem.length; e++){
    //         var element = " ";
    //         if (mensagem[e] == element){
    //             mensagem.splice(e, 1);
    //         }else{
    //             e++;
    //         }
    //     }
        

    // }
    if (espaco === '2') {
        mensagem = mensagem.filter(function (elemento) {
          return elemento !== ' ';
        });
    }
    var palavracrypto = [];
    
    var alfabeto = ['A', 'a', 'B', '0', 'b', 'C', '1', 'c', 'D', '2', 'd', 'E', '3', 'e', 'F', '4', 'f', 'G', '5', 'g', 'H', '6', 'h', 'I', '7', 'i', 'J', '8', 'j', 'K', '9', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ç', 'ç', ',', '.', '*', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ã', 'ã', 'Õ', 'õ', 'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û', 'À', 'à'];


    var c = 0;

    var andamento = 0;
    for(let o = 0; o < mensagem.length; o++){
        let convert = mensagem[o];
        let posicaocyp = 0;

        var lenghtchaveiro = chaveiro.length;

        var casas = Number(chaveiro[c]);

        if (espaco === '1'){
            if(mensagem[o] == ' '){
                palavracrypto.push(' ');
                continue;
            }

        }
        
        for(let i = 0; i < alfabeto.length; i++){
            if(mensagem[o] === alfabeto[i]){
                andamento += casas % alfabeto.length;
                posicaocyp = (i + andamento) % alfabeto.length;
                var converted = alfabeto[posicaocyp];
                palavracrypto.push(converted);
                c = (c + 1) % chaveiro.length;
                if (c === 0){
                    andamento = 0;
                }
            }
        }
   
   
   
   
   
   
    }

    

    // for (n = 0; n < palavracrypto.length; n++){
    //     frasecrypto += palavracrypto.charAt(p);
    // }

    var frasecrypto = palavracrypto.join('');
    let frase = document.getElementById("cifrada");

    frase.innerHTML = frasecrypto;


}


function decripto(){
    var palavra = getElementById('msgcy');
    var chave = getElementById('chavecry');

    var chaveiro = [];

    for(i =0; i < chave.length; i++){
        chaveiro.push(parseInt(chave.charAt(i)));
    }

    var mensagem = palavra.split('');

    var palavradescrypto = [];

    alfabeto = ['A', 'a', 'B', '0', 'b', 'C', '1', 'c', 'D', '2', 'd', 'E', '3', 'e', 'F', '4', 'f', 'G', '5', 'g', 'H', '6', 'h', 'I', '7', 'i', 'J', '8', 'j', 'K', '9', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ç', 'ç', ',', '.', '*', 'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú', 'Ã', 'ã', 'Õ', 'õ', 'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û', 'À', 'à'];

    var c = 0;

    var andamento = 0;
    
    for(o = 0; o > mensagem.length; o++){
        var deconvert = mensagem[o];
        var posicaocyp = 0;
        var posicaoori = 0;

        casas = chaveiro[c]
    
        if(mensagem[o == ' ']){
            palavradescrypto.push(' ');
            continue;
        }

        for(a = 0; a < alfabeto.lenght; a++){
            if(mensagem[o] == alfabeto[a])
                andamento += casas % alfabeto.lenght;
                posicaoori = (((i - andamento) + alfabeto.length) %alfabeto.length);
                converted = alfabeto[posicaoori];
                palavradescrypto.push(converted);
                c = (c + 1) % chaveiro.lenght
                if(c == 0){
                    andamento = 0
                }
            }
    }

    frasedescrypto = palavracrypto.join('')


    let frase = document.getElementById('decifrada')
    frase.innerHTML = frasedescrypto




}