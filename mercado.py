import sqlite3
from cadastro import cadastrando_produtos
import os

conn = sqlite3.connect('dados.db')

c = conn.cursor()

# c.execute("""CREATE TABLE produtos (
#               nome text,
#               quantidade integer,
#               custo_unidade real
#                )""") #<<Essa foi a mesa criada, só mantive essa informação aqui
                       #para ser possível entender como funciona o armazenamento de dados.>>

def inserir_dados():
    produtos = cadastrando_produtos()
    for produto in produtos.items():
        c.execute("INSERT INTO produtos VALUES (?, ?, ?)", (produto[0], produto[1][0], produto[1][1]))  #<<função que insere os dados>>

def deletar_dados(nome):
    c.execute("DELETE from produtos where nome=?", (nome,))   #<<função que deleta um produto específico, leva um argumento, que é o nome do produto>>

def deletar_tudo():
    c.execute("DELETE from produtos") #<<função que deleta todos produto>>

def colocar_estoque():
    c.execute("SELECT * FROM produtos ")

    dados = c.fetchall()

    produtos_teste = {}

    for produto in dados:
        if produto[0] not in produtos_teste:
            produtos_teste[produto[0]] = [produto[1], produto[2]]

        else:
            custo_medio = (produtos_teste[produto[0]][0] * produtos_teste[produto[0]][1] + produto[1] * produto[2])/(produtos_teste[produto[0]][0] + produto[1])
            produtos_teste[produto[0]][0] = produtos_teste[produto[0]][0] + produto[1]
            produtos_teste[produto[0]][1] = custo_medio
    return produtos_teste #<coloca os produtos no estoque e faz os devidos cálculos>>

def mostrar_estoque():
    print('{:^80}'.format('SEU ESTOQUE ATUAL: '))
    print()
    print('{:<40} {:<20} {:<20}'.format('Nome do Produto', 'Quantidade', 'Custo médio'))
    for produto in produtos_cadastrados.items():
        print("""
{}
{:<40} {:<20} {:.2f}
""".format('-'*80,produto[0], produto[1][0], produto[1][1])) #<<Mostra o estoque>>

produtos_cadastrados = colocar_estoque()

while True:
    opcao = input("""
        Digite [1] para inserir produtos no seu estoque
        Digite [2] para deletar um produto do seu estoque
        Digite [3] para deletar TUDO do seu estoque
        Digite [4] para mostrar o seu estoque
        Digite [5] para mostrar um produto específico
        Digite [6] para sair

        Digite a opção: """)
    while opcao not in ('1', '2', '3', '4', '5', '6'):
        print('Escolha inválida! Escolha uma opção do menu.')
        opcao = input("""
        Digite [1] para inserir produtos no seu estoque
        Digite [2] para deletar um produto do seu estoque
        Digite [3] para deletar TUDO do seu estoque
        Digite [4] para mostrar o seu estoque
        Digite [5] para mostrar um produto específico
        Digite [6] para sair

        Digite a opção: """)

    if opcao == '1':
        os.system('cls')
        inserir_dados()
        produtos_cadastrados = colocar_estoque()

    elif opcao == '2':
        os.system('cls')
        nome = str(input('Digite o nome do produto que você quer deletar: ')).strip().upper()
        deletar_dados(nome)
        produtos_cadastrados = colocar_estoque()
        print('Produto deletado.')

    elif opcao == '3':
        os.system('cls')
        deletar_tudo()
        produtos_cadastrados = colocar_estoque()
        print('Estoque zerado!')

    elif opcao == '4':
        os.system('cls')
        mostrar_estoque()
        produtos_cadastrados = colocar_estoque()

    elif opcao == '5':
            os.system('cls')
            nome = str(input('Digite o nome do produto que você quer ver: ')).strip().upper()
            if nome not in produtos_cadastrados.keys():
                print('Este produto não está cadastrado.')
                print('Verifique se o nome está correto.')
                pass

            else:
                print('{:<40} {:<20} {:<20}'.format('Nome do Produto', 'Quantidade', 'Custo médio'))
                print('{:<40} {:<20} {:.2f}'.format(nome, produtos_cadastrados['{}'.format(nome)][0], produtos_cadastrados['{}'.format(nome)][1]))

    elif opcao == '6':
        os.system('cls')
        break

    else:
        pass

    conn.commit()

conn.commit()

conn.close()
