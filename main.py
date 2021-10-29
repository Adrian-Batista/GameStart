import random

opcao = "SIM"

class Pessoa:
    def __init__(self, nome, pontuacao, tentativas):
        self.nome = nome
        self.pontuacao = tentativas
        self.tentativas = tentativas

user1 = Pessoa(str(input('Digite seu nome: ')), 10, 3)
valor = random.randint(1,10)

while opcao == "SIM":
    print(f"Seja Bem Vindo(a), {user1.nome}.!")
    print("------------------------------------------ \n")
    print(f" - Selecione um número de 1 a 10, você tem {user1.tentativas} tentativas: ")
    aux = False

    def reinicio(aux = ''):
        aux = str(input("\n - Se desejar começar novamente digite ( SIM ), se deseja sair pressione ENTER : "))
        aux = aux.upper()
        user1.pontuacao = 10
        user1.tentativas = 3
        valor = random.randint(1,10)
        return aux

    def impressao():
        print("\n ----------------------------------------- \n\n")
        print(f" - Usuário: {user1.nome}\n - Pontuação até o momento: {user1.pontuacao}\n - tentativas : {user1.tentativas}")
        print("\n\n ----------------------------------------- \n")

    while (aux == False):
        escolha = input(" - Digite: ")

        try:
            escolha = int(escolha)
            if escolha > 0 and escolha < 11:
                aux = True
            else:
                print("O valor está fora do intervalo definido tente novamente!")
                aux = False

        except ValueError:
            print("O Valor digitado não é um número, por favor repita a operação!")
            aux = False

    #print(f"- O Valor escolhido foi {escolha}, a resposta é {valor}.!\n")
    
    if(escolha == valor):
        print(" - Parabéns você acerto!")
        impressao()
        opcao = reinicio(opcao)

    elif(user1.tentativas == 3):
        user1.pontuacao = 5
        user1.tentativas -=1
        print(f" - Que pena, sua resposta foi incorreta, {user1.nome} você tem {user1.tentativas} tentativas restantes!")        

    elif(user1.tentativas == 2):
        user1.pontuacao = 2
        user1.tentativas -=1
        print(f" - Que pena, sua resposta foi incorreta, {user1.nome} você tem {user1.tentativas} tentativas restantes!")

    else:
        user1.pontuacao = 0
        print(" - Que pena, suas  tentativas esgotaram, reinicialize o game!")
        impressao()
        opcao = reinicio(opcao)
        
else:
    print("Volte Sempre!!")
