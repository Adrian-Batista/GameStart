import random

opcao = "SIM"

username = input('Digite seu nome: ')
print(f"Seja Bem Vindo(a), {username}.!")

while opcao == "SIM":
    valor = random.randint(1,10)

    pontuacao = 10
    tentativas = 3

    
    print("------------------------------------------ \n")
    print(f" - Selecione um número de 1 a 10, você tem {tentativas} tentativas: ")
    aux = False

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

    print(f"- O Valor escolhido foi {escolha}, a resposta é {valor}.!")
        




    opcao = str(input("Se desejar começar novamente digite ( SIM ), se deseja sair pressione ENTER : "))
    opcao = opcao.upper()
else:
    print("Volte Sempre!!")