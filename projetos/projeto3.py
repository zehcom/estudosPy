from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from datetime import datetime
# Functions

class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_Fisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.name = nome
        self.data_nasc = data_nascimento
        self.cpf = cpf

   ''' def __str__(self):
        return f"nome: {self.name.title()}, data_de_nasc: {self.data_nasc}, cpf: {self.cpf}, endereco: {self.rua}, {self.num} - {self.bair} - {self.cidade}/{self.uf}"
    '''
class Account:
    def __init__(self, numero, cliente):
        super().__init__()
        self._ag = "0001"
        self._numero = numero
        self._budget = 0
        self._cliente = cliente
        self.hist = Historico()

    @classmethod
    def nova_conta(cls, client, numero):
        return cls(numero, client)
    
    @property
    def saldo(self):
        return self._budget
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._ag
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico 

    def sacar(self, withdraw):
        pass_budget = withdraw > self.saldo

        if pass_budget:
            print('Valor insuficiente de saldo')
        
        elif valor > 0:
            self._budget -= withdraw
            print(f'\n Valor sacado de {withdraw}')

        else:
            print('Valor informado foi inválido')

    def depositar(self, deposit):
        if deposit > 0:
            self.budget += deposit
            print(f'\n Valor depositado de R${deposit}')
            #extract += f'\n Valor depositado de R${deposit}'
        else:
            print('Valor informado foi inválido')

class C_Account(Account):
    
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.lim_budget = limite
        self.max_with = limite_saque
    
    def sacar(self, valor):
        num_saque = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        pass_lim = valor > self.lim_budget
        pass_with = num_saque >= self.max_with

        if pass_lim:
            print('Operação Falhou! O valor supera o limite')
        
        elif pass_with:
            print('Operação Falhou! Número max de saques excedido')

        else:
            return super().sacar(valor)
    
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transaction(ABC):
    @abstractproperty
    @abstractmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transaction):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
menu = """
[c] Cadastra Usuário
[a] Cadastra Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

# Main
while True:

    opt = input(menu).lower()
    
    match opt:
        case 'a':
            new_user = Client()
            #accounts.append(new_user) if new_user != None else None
            print(new_user)
            print(new_user.name)
            #print(accounts)

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