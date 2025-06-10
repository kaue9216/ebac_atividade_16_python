pedido = []
estoque = {}
continuar = 1

def menu():
    print("Olá, eu sou seu assistente de estoque.")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade de produto")
    print("5 - Sair do programa")
    # print(selecionar)

def adicionar():
    item = input("O que deseja adicionar? ")
    pedido.append(item)
    # print(pedido)
    quantidade = float(input("Qual a Quantidade? "))
    valor = float(input("Qual o valor? "))
    for i in pedido:
        if i not in estoque:
            estoque[i] = {quantidade: valor}
        else:
            print("Item já adicionado")

    for chave in estoque:
        print("----------------")
        print("Item: ", chave)
        for chave, valor in estoque[i].items():
            print("Quantidade: ", chave)
            print("Preço: R$", valor)
        print("----------------")

def listar():
    for chave in sorted(estoque):
        print("----------------")
        print("Item: ", chave)
        for i in estoque:
            for chave, valor in estoque[i].items():
                print("Quantidade: ", chave)
                print("Preço: R$", valor)

def remover(estoque):
    listar()
    remover = input("Qual item deseja remover? ").strip()
    if remover in estoque:
        del estoque[remover]
        print(f"Item '{remover}' removido com sucesso!")
    else:
        print(f"Item '{remover}' não encontrado no estoque.")

def atualizar():
    listar()
    atualizar = input("Qual item deseja atualizar? ")
    if atualizar in estoque:
        nova_qauntidade = float(input("Digite a nova quantidade: "))
        novo_valor = float(input("Digite o novo valor: "))
        estoque[atualizar] = {nova_qauntidade: novo_valor}
        listar()
    else:
        print(f"Item '{atualizar}' não encontrado no estoque.")



while continuar == 1:
    menu()
    selecionar = float(input(" Selecione a opção desejada:" ))
    if selecionar == 1:
        adicionar()
    elif selecionar == 2:
        listar()
    elif selecionar == 3:
        remover(estoque)
    elif selecionar == 4:
        atualizar()
    else:
        continuar = 0
        break
    print("Deseja realizar outra operação?")
    print("1 - Sim")
    print("2 - Não")
    continuar = float(input("Digite a opção desejada: "))
