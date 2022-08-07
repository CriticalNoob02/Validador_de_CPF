import random

## Declarando Var fixas;
Menu = 0
Confirmação_1 = 1
Confirmação_2 = True
Confirmação_3 = True

try:

    ## Laço Menu;
    while Confirmação_1 == 1:
        Menu = 0
        Confirmação_2 = True
        Confirmação_3 = True
        print("")
        print("###################### Bem-Vindo ao Teste de CPF ########################\n")

        print("Aqui você pode escolher entre:")
        print("1- Verificar um CPF. ")
        print("2- Gerar um novo CPF. \n")

        Menu = int(input("Digite o NÚMERO referente ao que deseja fazer: "))


        if(Menu == 1):
            while Confirmação_2:
                while Confirmação_3:
                    cpf_1 = []
                    total = 0
                    n1 = 10
                    e = 0
                    igualdade = 0
                    cpf = input("Digite apenas os 11 números do CPF: ")

                    if(len(cpf) < 11 or len(cpf) > 11):
                        print("O que você digitou nem chega a ser um CPF!")

                    else:
                        ## Criando as Variavéis para a primeira conta;
                        total = 0
                        n1 = 10
                        e = 0

                        ## Adicionando CPF em Lista;
                        for i in cpf:
                            i = int(i)
                            cpf_1.append(i)

                        for i in cpf_1:
                            if(cpf_1.count(i) > 10):
                                igualdade = 1
                            else:
                                pass

                        ## 1º Multiplicação;
                        for i in range(2, 11):
                            total += (cpf_1[e]*n1)
                            n1 -= 1
                            e += 1
                            
                        ## Verificando o 1º Digito;
                        digito1 = (11- (total % 11))
                        if digito1 > 9:
                            digito1 = 0
                        
                        if (digito1 == cpf_1[-2]):
                            if (igualdade == 1):
                                print("CPF invalido!")
                            else:
                                Confirmação_3 = False

                        else:
                            print("CPF invalido!")

                ## Zerando as Variaveis;
                n1 = 11
                e = 0
                total = 0

                ## 2º Multiplicação;
                for i in range(2, 12):
                    total += (cpf_1[e]*n1)
                    n1 -= 1
                    e += 1

                ## Verificando o 2º Digito;    
                digito2 = (11- (total % 11))
                if digito2 > 9:
                    digito2 = 0

                if (digito2 == cpf_1[-1]):
                        Confirmação_2 = False  

                else:
                    print("CPF invalido!")        

            print(" ")
            print(f"Digito 1º {digito1}")
            print(f"Digito 2º {digito2}")
            print(" ")
            print("o CPF digitado está correto!")
            print(" ")

            Confirmação_1 = int(input("Deseja voltar ao Menu? (1- Sim / 2- Não) "))

        elif(Menu == 2):
            
            ## Declarando Variaveis Fixas
            verificação1 = True
            verificação2 = True
            contador = 0

            ## Loop da Verificação do Segundo Digito
            while verificação2:

                ## Zerando a Lista e permitindo a reentrada no primeiro Loop;
                cpf1 = []
                verificação1 = True

                ## Loop da Verificação do Primeiro Digito;
                while verificação1:

                    ## Zerando a Lista
                    cpf1 = []

                    ## Declaração de Variaveis;
                    n1 = 10
                    e = 0
                    total = 0

                    ## Criação de CPF;
                    for cpf in range (1,12):
                        cpf = random.randint(0,9)
                        cpf1.append(cpf) 
                        contador += 1 


                    ## 1º Multiplicação;
                    for i in range(2, 11):
                        total += (cpf1[e]*n1)
                        n1 -= 1
                        e += 1
                        
                    ## Verificando o 1º Digito;
                    digito1 = (11- (total % 11))
                    if digito1 > 9:
                        digito1 = 0

                    if (digito1 == cpf1[-2]):
                        verificação1 = False
                
                ## Zerando as Variaveis;
                n1 = 11
                e = 0
                total = 0

                ## 2º Multiplicação;
                for i in range(2, 12):
                    total += (cpf1[e]*n1)
                    n1 -= 1
                    e += 1

                ## Verificando o 2º Digito;    
                digito2 = (11- (total % 11))
                if digito2 > 9:
                    digito2 = 0

                if (digito2 == cpf1[-1]):
                        verificação2 = False

            print(" ")
            print(f"Foram feitas {contador} tentativas para criar um cpf válido.")
            print(" ")
            print(f"Digito 1º {digito1}")
            print(f"Digito 2º {digito2}")
            print(" ")
            print(f"Seu CPF é: {cpf1}") 
            print(" ")           

            Confirmação_1 = int(input("Deseja voltar ao Menu? (1- Sim / 2- Não) "))

except:
    print("ERROR")
    
## Desenho e mensagem de Fechamento;
print("\n \n \n \n \n \n")
print("⣿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠈⣿⣿⣿⣿")
print("⣿⠋⠉⠁⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠈⠉⠻⣿")
print("⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⠟⠁⣰⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⣿")
print("⣿⣦⣄⣀⣤⣶⣄⠀⠀⠀⠀⠙⢿⡿⠃⠀⡾⠃⣰⠟⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠈⢿⡀⠈⢿⡿⠋⠀⠀⠀⠀⣠⣶⣄⣀⣀⣴⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⢀⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣷⣶⣾⣿⡄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⣀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⣠⣴⣶⣦⣄⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣾⣿⣿⣿⣿⣿⣇⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢸⣿⣿⣿⣿⣿⣿⠇⠀⠀⠘⣿⣿⣿⣿⣿⣿⡿⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠻⠿⣿⣿⠿⠋⠀⠀⠀⠀⠘⠿⢿⣿⡿⠿⠃⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠐⢿⣿⠇⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠛⠲⠦⣤⣤⣤⣀⣀⣤⣤⣤⠴⠖⠛⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢸⢧⣀⠀⢰⡇⠀⠈⠉⡏⠉⠀⢸⠀⠀⢀⣼⡇⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣟⠀⠈⠉⣾⠳⠶⠤⣤⣧⠤⠴⢾⡗⠉⠉⠀⢇⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⡿⠋⠉⠙⠻⠛⠁⠀⠀⠀⢀⡏⠑⢶⣤⡟⠀⠀⠀⠀⡇⠀⠀⠀⣷⣠⡴⠖⢻⠀⠀⠀⠀⠈⠻⠟⠋⠉⠙⢿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⣾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣧⣀⣀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣾⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print(" ")
print("Muito obrigado por usar meu Testador!!")
