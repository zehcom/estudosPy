menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

budget = 0
lim_budget = 500
extract = ""
num_with = 0
MAX_WITH = 3

while True:

    opt = input(menu).lower()

    match opt:
        
        case 'd':
            deposit = round(float(input('Informe o valor de depósito: ')),2)
            budget += deposit
            extract += f'\n Valor depositado de {deposit}'
            print('Depositar')
        
        case 's':
            if num_with >= MAX_WITH:
                print('Limite máximo de saque atingido')
            else:
                withdraw = round(float(input('Valor de saque: ')), 2)
                if withdraw > lim_budget:
                    print('Valor de saque superior ao limite')
                elif (budget - withdraw) < 0:
                    print('Valor insuficiente de saldo')
                else:
                    budget -= withdraw
                    extract+= f'\n Valor sacado de {withdraw}'
                    num_with+=1
        
        case 'e':
            print(extract, f'\n\n Saldo em conta: R${budget:.2f}')
    
        case 'q':
            break

        case _:
            print('Opção Inválida')