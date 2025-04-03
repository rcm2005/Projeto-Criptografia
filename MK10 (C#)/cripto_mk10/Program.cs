using System;
using System.Text;

class Cifrador
{
    private string chave;

    // Construtor que recebe a chave da cifragem
    public Cifrador(string chave)
    {
        this.chave = chave;
    }

    public string Cifrar(string mensagem)
    {
        StringBuilder resultado = new StringBuilder();

        for (int i = 0; i < mensagem.Length; i++)
        {
            
            // Faz um deslocamento no caractere baseado na chave
            char letra = (char)(mensagem[i] + chave[i % chave.Length]);
            resultado.Append(letra);
        }

        return resultado.ToString();
    }

    // Método para decifrar a mensagem
    public string Decifrar(string mensagemCifrada)
    {
        StringBuilder resultado = new StringBuilder();

        for (int i = 0; i < mensagemCifrada.Length; i++)
        {
            // Reverte o deslocamento do caractere
            char letra = (char)(mensagemCifrada[i] - chave[i % chave.Length]);
            resultado.Append(letra);
        }

        return resultado.ToString();
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("-------------------------------------------");
        Console.WriteLine("------Bem vindo à Cifra de César MK10------");
        Console.WriteLine("-------------------------------------------");

        Console.Write("Digite a chave: ");
        string chave = Console.ReadLine();

        Cifrador cifrador = new Cifrador(chave);

        Console.Write("Digite a mensagem: ");
        string mensagem = Console.ReadLine();

        string mensagemCifrada = cifrador.Cifrar(mensagem);
        Console.WriteLine($"Mensagem cifrada: {mensagemCifrada}");

        string mensagemDecifrada = cifrador.Decifrar(mensagemCifrada);
        Console.WriteLine($"Mensagem decifrada: {mensagemDecifrada}");
    }
}
