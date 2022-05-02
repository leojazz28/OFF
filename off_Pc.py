# módulo de inportado para desligar o pc 
import os
import time 

user = "leo"
senhaUser = "1234"

# fução verificar senha
def senha_root():
    print("Insira sua senha de adm")
    print("Digite sua senha numerica, somente numeros!")

    for i in range(4):

        verificar_senha = str(input("senha: "))
        
        if senhaUser == verificar_senha:
            print("ok!")
            break
            
        elif senhaUser != verificar_senha:
            print("senha incorreta ou incompleta!")
           
        else:
            print()

        if i == 3 :
            print("Tetativas exedida!")
            exit()
        else:
            print()
            



#função de loggin
def entrada():
    import time 
    contador = 1

    while (contador <= 3):
        print('digite seu nome de user Root')
        print()
        nome = input("User: ").lower() #letra minúsculas 
        
        if nome != user:
            print("usuario Incorreto ")
            print("verifique seu nome! ")
            print()
            exit()
            

            if contador == 3:
                print("Tentativas exedidas.")
                print("Usuario sem premição.")
                print('exit')
                time.sleep(3)
                exit()
            
        
        elif nome == user  :
            print(f"Seja bem vindo {user}, aguarde enquanto efetumaos sua ação.")
           
        break
             

        contador = contador + 1

# função módulo data de hora 
from datetime import datetime
data = datetime.today().strftime('Date %d-%m-%y') 
hora = datetime.today().strftime('%H:%M')

#função de saldação 
def saldation():
    if hora <= '12:00' :
        print("Bom Dia!")

    elif hora <= "18:00" :
        print("Boa tarde!")
    
    elif hora >= "18:00":
        print("Boa noite!")
    
    else:
        print('#')

#entrda
print()
print("Ola, seja bem vindo ao seu gestor de tarefas")
print()
print(data)
print(hora)
print()

s = saldation()

nome = input("Informe seu nome:")
print()
print(s, nome)
print("Escolha uma Opção!")
print(""" 
        [1] => Vscode 
        [2] => Atom
        [3] => Vim
        [4] => Reiniciar sistema 
        [5] => desligar sistema
""")
print()
options = str(input("Digite a uma Opção ")) #um switch case seria bom agora!
if options == "1":
    entrada()
    vscode = os.system('code')

elif options == "2":
    entrada()
    atom = os.system('atom')
    
elif options == "3":
    entrada()
    vim = os.system('gvim')

elif options == "4":
    entrada()
    senha_root()
    time.sleep(3)
    reboot = os.system('reboot')

elif options == "5":
    entrada()
    senha_root()
    time.sleep(5)
    powerof = os.system('poweroff')

else: 
    print("opeção invalida, saindo em 3 segundos! ")











