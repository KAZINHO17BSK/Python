import os
import time

class Pergunta:
    def __init__(self, prompt, resposta):
        self.prompt = prompt
        self.resposta = resposta

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def perguntar_numero():
    while True:
        try:
            num_perguntas = int(input("Quantas perguntas você deseja responder? (entre 1 e 20) "))
            if 1 <= num_perguntas <= 20:
                return num_perguntas
            else:
                print("Por favor, insira um numero entre 1 e 20.")
        except ValueError:
            print("Por favor, insira um número válido.")

def run_quiz(perguntas, num_perguntas):
    pontuacao = 0

    for pergunta in perguntas[:num_perguntas]:
        clear_terminal()
        print(pergunta.prompt)
        resposta = input()

        clear_terminal()

        if resposta.lower() == pergunta.resposta.lower():
            pontuacao += 1
            print("\033[92mResposta correta!\033[0m")
        else:
            print("\033[91mResposta errada. A resposta correta era:\033[0m", pergunta.resposta)

        time.sleep(1)

    print("Você acertou " + str(pontuacao) + " de " + str(num_perguntas) + " perguntas!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        print("Saindo do código!")
    else:
        run_quiz(perguntas, perguntar_numero())

perguntas = [
    Pergunta("1) Qual é a capital do Brasil?\n(a) Rio de Janeiro\n(b) São Paulo\n(c) Brasília", "c"),
        
    Pergunta("2) Qual é o maior planeta do sistema solar?\n(a) Terra\n(b) Júpiter\n(c) Marte", "b"),
        
    Pergunta("3) Quem pintou o quadro 'Mona Lisa'?\n(a) Vincent van Gogh\n(b) Leonardo da Vinci\n(c) Pablo Picasso", "b"),   
     
    Pergunta("4) Qual é a capital do Canadá?\n(a) Toronto\n(b) Vancouver\n(c) Ottawa","c"), 
       
    Pergunta("5) Quem foi o primeiro presidente dos Estados Unidos?\n(a) Thomas Jefferson\n(b) George Washington\n(c) Abraham Lincoln","b"),
       
    Pergunta("6) Qual é a camada mais externa da atmosfera terrestre?\n(a) Estratosfera\n(b) Mesosfera\n(c) Exosfera","c"),
       
    Pergunta("7) Qual é o instrumento utilizado para medir terremotos?\n(a) Barômetro\n(b)  Sismógrafo\n(c) Higrômetro","b"), 
       
    Pergunta("8) Em que ano a União Europeia foi oficialmente estabelecida?\n(a) 1957\n(b) 1973\n(c) 1992","a"),    
    
    Pergunta("9) Quem é o criador da empresa Microsoft?\n(a) Steve Jobs\n(b) Bill Gates\n(c) Mark Zuckerberg","b"), 
       
    Pergunta("10) Qual é o nome do maior desfiladeiro do mundo?\n(a) Grand Canyon\n(b) Barranca del Cobre\n(c) Desfiladeiro do Colca","a"),  
     
    Pergunta("11) Qual é o segundo planeta mais próximo do Sol?\n(a) Vênus\n(b) Marte\n(c) Júpiter","a"),    
    
    Pergunta("12) Quem escreveu O Pequeno Príncipe?\n(a) Antoine de Saint-Exupéry\n(b) J.K. Rowling\n(c) Roald Dahl","a"),    
    
    Pergunta("13) Qual é o nome da maior cordilheira do mundo?\n(a) Everest\n(b) Cordilheira dos Andes\n(c) ordilheira do Himalaia","b"),  
      
    Pergunta("14) Qual é o elemento mais abundante na crosta terrestre?\n(a) Ferro\n(b) Silício\n(c) Oxigênio","c"),    
    
    Pergunta("15) Quem foi o primeiro homem a completar uma viagem ao redor da Terra?\n(a) Yuri Gagarin\n(b) Neil Armstrong\n(c) Ferdinand Magellan","c"),    
    
    Pergunta("16) Em que ano a Organização das Nações Unidas (ONU) foi fundada?\n(a) 1945\n(b) 1955\n(c) 1965","a"),    
    
    Pergunta("17) Qual é o maior deserto do mundo?\n(a) Saara\n(b) Antártida\n(c) Atacama","b"),    
    
    Pergunta("18) Qual é o país conhecido como Terra do Sol Nascente?\n(a) Coreia do Sul\n(b) Japão\n(c) China","b"),    
    
    Pergunta("19) Quem é considerado o pai da psicanálise?\n(a) Sigmund Freud\n(b) Carl Jung\n(c) Alfred Adler","b"),
    
    Pergunta("20) Em que continente está localizado o Egito?\n(a) África\n(b) Ásia\n(c) Europa","a"),
]

num_perguntas = perguntar_numero()
run_quiz(perguntas, num_perguntas)
