# Functions

def user():
    name = input("Informe o nome do usuário: ")
    data_nasc = input("Informe a data de nascimento: ")
    cpf = input("Informe o cpf (somente números): ").replace(".", "")
    rua = input("Informe a rua de endereço do usuário: ")
    num = input("Número do endereço: ")
    bair = input("Nome do bairro: ")
    cidade = input("Nome da cidade: ")
    uf = input("UF do Estado: ")

    return {"nome": name.title(), "data_de_nasc": data_nasc, "cpf": cpf, "endereco": f"{rua}, {num} - {bair} - {cidade}/{uf}"}

def account(acc, clients):
    ag = "0001"
    cli_acc = input("Qual cliente para vincular: ")

    for client in clients:
        if cli_acc in client['nome']:
            return {"agência": ag, "conta": acc, "cliente": cli_acc}
    
        else:
            print("Cliente não encontrado")
    else:
            print("Cliente não encontrado")
    

def sacar(budget, withdraw, extract, lim_budget, num_with, max_with):
    if num_with >= max_with:
        print('Limite máximo de saque atingido')
        return budget, extract
    
    if withdraw > lim_budget:
        print('Valor de saque superior ao limite')
        return budget, extract
    
    elif (budget - withdraw) < 0:
        print('Valor insuficiente de saldo')
        return budget, extract
    
    else:
        budget -= withdraw
        extract+= f'\n Valor sacado de {withdraw}'
        return budget, extract

def deposita(budget, deposit, extract):
    budget += deposit
    extract += f'\n Valor depositado de R${deposit}'
    print('Depositar')

    return budget, extract

def extrato(budget, extract):
    print(extract, f'\n\n Saldo em conta: R${budget:.2f}')

menu = """
[c] Cadastra Usuário
[a] Cadastra Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

budget = 0
lim_budget = 500
extract_hist = ""
num_with = 0
MAX_WITH = 3
clients = []
accounts = []

# Main
while True:

    opt = input(menu).lower()
    
    match opt:
        case 'a':
            account_f = account(len(accounts) + 1, clients)
            accounts.append(account_f) if account_f != None else None
            print(accounts)

        case 'c':
            clients.append(user())
            print(clients)
            
        case 'd':
            deposit = round(float(input('Informe o valor de depósito: ')),2)
            budget, extract_hist = deposita(budget=budget, deposit=deposit, extract=extract_hist)
        
        case 's':
            withdraw = round(float(input('Valor de saque: ')), 2)
            n_budget, n_extract =  sacar(budget=budget, withdraw=withdraw, extract=extract_hist, lim_budget=lim_budget, num_with=num_with, max_with=MAX_WITH)

            if (n_budget != budget):
                budget = n_budget
                extract_hist = n_extract
                num_with+=1

        case 'e':
            extrato(budget, extract=extract_hist)
    
        case 'q':
            break

        case _:
            print('Opção Inválida a se acrescentar')