import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict(data=({'nome':['banana'], 'preco':[1.92], 'qtd':[2]}))
df.to_csv('projetos/produtos_estudo1.csv', sep=';', index=False)

# Classes
class Produto:
    
    def __init__(self, nome, preco, qtd):
        self._nome = nome
        self._preco = preco
        self._qtd = qtd
    
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property   
    def quantidade(self):
        return self._qtd
    
    def add_estoque(self, qtd):
        self.qtd += qtd
    
    def remove_estoque(self, qtd):
        self.qtd -= qtd

    def att_estoque(self):
        df = pd.read_csv('projetos/produtos_estudo1.csv', sep=';')
        df[df['nome'] == self.nome]['qtd'] = self.quantidade

    def calc_valor_total(self):
        print('Valor total é de: ',(self.qtd*self.preco))

class Carrinho:
    
    def __init__(self, carrinho=[], total=0):
        self._carrinho = carrinho
        self._total = total
    
    @property
    def preco_total(self):
        return self._total
    
    @property
    def carrinho(self):
        return self._carrinho
    
    def add_produto(self, produto):
        df = pd.read_csv('projetos/produtos_estudo1.csv', sep=';')

        if produto.nome in df['nome'].to_list():
            self._carrinho.append([produto.nome, produto.quantidade])
            self._total += produto.quantidade * produto.preco
            print(f'Produto {produto.nome} adicionado ao carrinho')

        else:
            print('Produto não encontrado na lista')
        
    def remove_produto(self, produto):
        if produto.nome in self._carrinho:
            self._carrinho.remove([produto.nome, produto.quantidade])
            self._total = self._total - (produto.quantidade * produto.preco)
            print(f'Produto {produto.nome} removido do carrinho')

        else:
            print('Produto não encontrado no carrinho')
    
class Cliente:
    
    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
    
    def realizar_compra(self, carrinho):
        df=pd.read_csv('projetos/produtos_estudo1.csv', sep=';')
        for produto in carrinho.carrinho:
            if str(produto[0]) in df['nome'].to_list():
                df.loc[df['nome'].str.contains('banana'), 'qtd'] -= produto[1]
            else:
                print('Produto não encontrado')
        df.to_csv('projetos/produtos_estudo1.csv', sep=';', index=False)

# Functions
def cadastra_produto(nome, valor, qtd, df):
    df.loc[len(df)] = [nome, valor, qtd]
    df.to_csv('projetos/produtos_estudo1.csv', sep=';', index=False)
    print(f'\nProduto {nome} cadastrado com sucesso')

MENU = """
[a] Cadastra Produto
[b] Adiciona Produto no Carrinho
[c] Remover Produto do Carrinho
[d] Calcula Valor total da Compra
[e] Realiza Compra
[q] Sai do programa\n
"""
carrinho = Carrinho()
cliente = Cliente('gabs', '11543251722', 'Rua golf')
df = pd.read_csv('projetos/produtos_estudo1.csv', sep=';')

print(int(df[df['nome'] == 'banana'].qtd))
while True:

    opt = input(MENU).lower()

    match opt:
        case 'a':
            nome_produto = input('Qual o nome do produto? ')
            if nome_produto in df['nome'].to_list():
                print('Produto já cadastrado')
            else:
                preco_produto = input('Qual o preco do produto? ')
                qtd_produto = input('Qual a quantidade do produto? ')
                cadastra_produto(nome_produto, preco_produto, qtd_produto, df)

        case 'b':
            select = input(f'Lista dos produtos disponíveis: \n {df}\n').lower()
            produto = Produto(select, df[df['nome'] == select]['preco'], int(df[df['nome'] == select].qtd))
            carrinho.add_produto(produto)

        case 'c':
            select = input(f'Lista dos produtos no carrinho: \n {carrinho.carrinho}\n').lower()
            produto = Produto(select, df[df['nome'] == select]['preco'], int(df[df['nome'] == select].qtd))
            carrinho.remove_produto(produto)

        case 'd':
            print('Valor total do Carrinho R$ ', carrinho.preco_total)

        case 'e':
            cliente.realizar_compra(carrinho)
            print('Compra finalizada')
        case 'q':
            break

        case _:
            print('Opção inválida')
