def cadastro():
    nome.append(input('digite seu nome '))

def listar():
    if len(nome) == 0:
        print('lista de nomes vazia')
    else:
        print('lista de nomes')
        for n in nome:
            print(n)

def remover():
    nome.remove(input('digite seu nome de remoção '))

nome={}

while True:
    print('opção 1 para cadastrar nome')
    print('opção 2 ver nomes')
    print('opção 3 remover nome')
    print('opção 4 sair do programa')

    opcao = input('digite sua escolha ')

    if opcao=='1':
        cadastro()

    elif opcao=='2':
        listar()

    elif opcao=='3':
        remover()

    elif opcao=='4':
        print('sair do programa')
        break

    else:
         print('opção invalida')