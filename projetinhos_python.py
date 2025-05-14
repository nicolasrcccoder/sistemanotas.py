global_id = 0
lista_livro = []


def cadastrar_livro():
    global global_id
    nome_livro = input('qual o nome?')
    autor = input('qual o autor?')
    editora = input('qual a editora?')
    livro = {'id': global_id, 'nome': nome_livro, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    global_id += 1
    print('livro cadastrado com sucesso!')


def consultar_livro():
    while True:
        print('MENU CONSULTA')
        print(' 1 - Consultar Todos\n 2 - Consultar por Id\n 3 - Consultar por Autor\n 4 - Retornar ao menu): ')
        opcao_consultar = input('digite a opcao de consulta que você deseja:')
        if opcao_consultar == '4':
            print('voltando ao menu...')
            break
        elif opcao_consultar == '1':
            print('consultando os livros...')
            for livro in lista_livro:
                print(livro)
        elif opcao_consultar == '2':
            id_desejado = int(input('digite o seu ID:'))
            for livro in lista_livro:
                if livro['id'] == id_desejado:
                    print(livro)
                else:
                    print('ID não encontrado')
        elif opcao_consultar == '3':
            autor_desejado = input('digite o nome do autor:')
            for livro in lista_livro[:]:
                if livro['autor'] == autor_desejado:
                    print(livro)
        else:
            print('opcao invalida , digite apenas as opções acima!')


def remover_livro():
        id_remover = int(input('digite qual ID remover: '))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')

            else:
                print('Livro não encontrado!')


# programa principal
while True:
    print('bem vindo a livraria de nicolas regert')
    print('MENU PRINCIPAL')
    print('ESCOLHA A OPÇÃO DESEJADA :')
    print(f' 1 - cadastrar livro\n 2 - consultar livro(s)\n 3 - remover livro\n 4 - Sair ')
    opcao = input('qual a opção que você deseja?')
    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print('você saiu... encerrando o programa...')
    else:
        print('apenas digite as opcoes acima...')