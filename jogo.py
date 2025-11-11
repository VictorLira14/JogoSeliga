import random

def exibir_titulo():
    print("=" * 45)
    print(" Bem-vindo ao Quiz do Conhecimento! ")
    print("=" * 45)

def carregar_perguntas():
    # Lista de tuplas: (pergunta, [alternativas], resposta_certa)
    perguntas = [
        ("Qual é a capital do Brasil?", ["a) Rio de Janeiro", "b) Brasília", "c) São Paulo", "d) Salvador"], "b"),
        ("Quem pintou a Mona Lisa?", ["a) Van Gogh", "b) Leonardo da Vinci", "c) Picasso", "d) Michelangelo"], "b"),
        ("Qual é o maior planeta do Sistema Solar?", ["a) Terra", "b) Júpiter", "c) Saturno", "d) Marte"], "b"),
        ("Em que continente fica o Egito?", ["a) África", "b) Ásia", "c) Europa", "d) América"], "a"),
        ("Qual a cor resultante da mistura de azul e amarelo?", ["a) Verde", "b) Roxo", "c) Laranja", "d) Marrom"], "a")
    ]
    return perguntas

def jogar():
    exibir_titulo()
    perguntas = carregar_perguntas()
    random.shuffle(perguntas) # embaralha as perguntas

    pontos = 0
    for i, (pergunta, opcoes, resposta_certa) in enumerate(perguntas, start=1):
        print(f"\nPergunta {i}: {pergunta}")
        for opcao in opcoes:
            print(opcao)
        
        resposta = input("Sua resposta (a/b/c/d): ").strip().lower()

        # Manipulação de string e condicionais
        if resposta == resposta_certa:
            print("✅ Correto! Você ganhou 10 pontos.")
            pontos += 10
        else:
            print(f" Errado! A resposta certa era '{resposta_certa}'.")
        print("-" * 40)

    print(f"\nJogo encerrado! Sua pontuação final foi: {pontos}")
    avaliar_desempenho(pontos)

def avaliar_desempenho(pontos):
    # Condicionais para avaliação final
    if pontos == 50:
        print("Excelente! Você acertou todas!")
    elif pontos >= 30:
        print("Muito bom! Você foi bem!")
    elif pontos >= 10:
        print(" Tá quase! Dá pra melhorar!")
    else:
        print("Estude um pouco mais e tente de novo!")

# Função principal
def main():
    while True:
        jogar()
        novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if novamente != 's':
            print(" Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    main()