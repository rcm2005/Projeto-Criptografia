using System;
using System.Text;

class Cifrador
{


    private string chave;

    //construtor que recebe a cahve da cifragem
    public Cifrador(string chave){
        this.chave = chave;
    }

    public string Cifrar(string mensagem){
        StringBuilder resultado = new StringBuilder();

        for (int i = 0; i < mensagem.Length; i++){
            //faz um deslocamento no caractere da chave

            char letra = (char)(mensagem[i] + chave.Length);

        }

        return resultado.ToString();
    }

    //Método para decifrar a mensagem
    public string Decifrar(string mensagemCifrada)
    {
        StringBuilder resultado = new StringBuilder();
        for (int i = 0; i < mensagemCifrada.Length; i++){
            //reverte o deslocamento do caractere
            char = letra = (char)(mensagemCifrada[i] - chave.Length);
            resultado.append(Letra);
        }
        return resultado.ToString();
    }
    
}

class Program{

    static void Main(){


        Console.WriteLine("-------------------------------------------")
        Console.WriteLine("------Bem vindo à Cifra de César MK10------")
        Console.WriteLine("-------------------------------------------")

        Console.Write("Digite a chave: ");
        string chave = Console.ReadlLine();



        Cifrador cifrador = new Cifrador(chave);

        Console.WriteLine("Digite a mensagem: ")

        String mensagem = Console.ReadlLine();

        string mensagemCifrada = cifrador.Cifrar(mensagem);
        console.WriteLine($"mensagem cifrada: {mensagemCifrada}");

        string mensagemDecifrada = cifrador.Decifrar(mensagemCifrada);
        console.writeline($"mensagem decifrada: {mensagemDecifrada}")





    }
}