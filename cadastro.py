def cadastrando_produtos():
    produtos = {}
    while True:
        if produtos == {}:
            resposta = str(input("Gostaria de cadastrar algum produto no seu estoque [S/N]? ")).strip().upper()[0]
        else:
            resposta = str(input("Gostaria de cadastrar mais algum produto no seu estoque [S/N]? ")).strip().upper()[0]
        while resposta not in ("SN"):
            resposta = str(input("Gostaria de cadastrar ou não? ")).strip().upper()[0]
        if resposta == "S":
            nome = str(input("Diga o nome do Produto que você vai cadastrar: ")).upper().strip()
            if nome not in produtos:
                quantidade = int(input("Digite quantas unidades você irá cadastrar: "))
                preco = float(input("Digite o valor da unidade do produto: "))
                custo_medio = (preco * quantidade) / quantidade
                print("Você cadastrou {} unidades de {}".format(quantidade, nome))
                print("Cada unidade tem o valor de R${:.2f}.".format(preco))
                produtos[nome] = [quantidade,custo_medio]
            else:
                quantidade = int(input("Digite quantas novas unidades você irá cadastrar: "))
                preco = float(input("Digite o valor da unidade do produto: "))
                print("Você cadastrou {} unidades de {}.".format(quantidade, nome))
                print("Cada unidade tem o valor de R${:.2f}.".format(preco))
                custo_medio = (produtos[nome][0] * produtos[nome][1] + quantidade * preco)/(produtos[nome][0] + quantidade)
                produtos[nome][0] = produtos[nome][0] + quantidade
                produtos[nome][1] = custo_medio
                print("O Produto foi atualizado.")
            print('Estoque atualizado.')
        else:
            break

    return produtos
