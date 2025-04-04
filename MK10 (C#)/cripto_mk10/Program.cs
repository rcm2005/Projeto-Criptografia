using System;
using System.Text;
using System.Collections.Generic;

class Cifrador
{
    private string chave;

    public Cifrador(string chave)
    {
        this.chave = chave;
    }

    public string Cifrar(string mensagem)
    {
        StringBuilder resultado = new StringBuilder();
        List<int> cifra_num = new List<int>();

        for (int l = 0; l < chave.Length; l++)
        {
            cifra_num.Add((int)chave[l]);
        }

        int deslocamento = 0;
        int contador_chave = 0;

        for (int i = 0; i < mensagem.Length; i++)
        {
            char letraCifrada = (char)(mensagem[i] + cifra_num[contador_chave] + deslocamento);
            resultado.Append(letraCifrada);

            deslocamento += cifra_num[contador_chave];
            contador_chave = (contador_chave + 1) % chave.Length;
        }

        return resultado.ToString();
    }

    public string Decifrar(string mensagemCifrada)
    {
        StringBuilder resultado = new StringBuilder();
        List<int> cifra_num = new List<int>();

        for (int l = 0; l < chave.Length; l++)
        {
            cifra_num.Add((int)chave[l]);
        }

        int deslocamento = 0;
        int contador_posic_chave = 0;

        for (int i = 0; i < mensagemCifrada.Length; i++)
        {
            char letracifrada = (char)((int)mensagemCifrada[i] - deslocamento - cifra_num[contador_posic_chave]);
            resultado.Append(letracifrada);

            deslocamento += cifra_num[contador_posic_chave];
            contador_posic_chave = (contador_posic_chave + 1) % chave.Length;
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
