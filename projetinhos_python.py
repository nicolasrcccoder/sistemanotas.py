lista_funcionario = []
def cadastrar_funcionario():
    nome_funcionario = str(input('qual o nome : '))
    cargo_funcionario = str(input('qual o cargo : '))
    salario_funcionario = int(input('qual o salário (1000 - 20000): '))
    if salario_funcionario < 999 or salario_funcionario > 20000: 
          print('apenas salários entre (1000 - 20000)')   
          return
    
    else:
       setor_funcionario = str(input('qual o setor : '))
       dicionario_funcionario = {'nome' : nome_funcionario , 
                              'cargo' : cargo_funcionario ,
                              'salario' : salario_funcionario , 
                              'setor' : setor_funcionario} 
       lista_funcionario.append(dicionario_funcionario)
       print('adicionado!')
       
    

def mostrar_funcionario():
    if not lista_funcionario:
        print('não há funcionarios por enquanto...')
    else:
        for dicionario_funcionario in lista_funcionario:
            print(f'{dicionario_funcionario["nome"]} | {dicionario_funcionario["cargo"]} | {dicionario_funcionario["salario"]} | {dicionario_funcionario["setor"]}')
        
def analisar_funcionario():
  while True:  
    media_salarial = 0
    maior_salario = 1
    menor_salario = 20000
    soma_salario = 0
    funcionario_maior_salario = None
    funcionario_menor_salario = None
    print('----- SISTEMA DE SALÁRIO DA EMPRESA -----')
    print(' -- 1 - mostrar quem ganha menos que 10000 --|-- 2 - mostrar quem ganha mais de 10000 ')
    print(' -- 3 - mostrar a média salárial da empresa -- |-- 4 - mostrar o menor salário -- |-- 5 - mostrar o maior salário')
    print(' -- 6 - SAIR -- ' )
    analisar_opcao = input('o que deseja :')
    if analisar_opcao == '1':
        if not lista_funcionario:
            print('não há funcionarios ainda...')
        else:
            for dicionario_funcionario in lista_funcionario:
                if dicionario_funcionario['salario'] < 10000:
                    print(f' o Funcionario {dicionario_funcionario["nome"]} com {dicionario_funcionario["salario"]}')
            

    elif analisar_opcao == '2':
        if not lista_funcionario:
            print('não há funcionarios ainda...')
        else:
             for dicionario_funcionario in lista_funcionario:
                 if dicionario_funcionario['salario'] >= 10000:
                   print(f' o Funcionario {dicionario_funcionario["nome"]} com {dicionario_funcionario["salario"]}') 
             
    
    elif analisar_opcao == '3':
        if not lista_funcionario:
             print('não há funcionarios ainda...')
        else:
            for dicionario_funcionario in lista_funcionario:
               soma_salario += (dicionario_funcionario['salario']) 
            media_salarial = soma_salario / len(lista_funcionario)
            print(f'a média de salario de todos os funcionarios é de {media_salarial} ')
            
    
    elif analisar_opcao == '4':
        if not lista_funcionario:
            print('não há funcionarios ainda...')
        else:
            for dicionario_funcionario in lista_funcionario:
                if dicionario_funcionario['salario'] < menor_salario:
                    menor_salario = dicionario_funcionario['salario']
                    funcionario_menor_salario = dicionario_funcionario
            print(f'o {funcionario_menor_salario["nome"]} é o funcionario com o menor salário . Salário : {funcionario_menor_salario["salario"]} ')
            

    elif analisar_opcao == '5':
        if not lista_funcionario:
            print('não há funcionarios ainda...')
        else:
            for dicionario_funcionario in lista_funcionario:
                if dicionario_funcionario['salario'] > maior_salario :
                    maior_salario = dicionario_funcionario['salario']
                    funcionario_maior_salario = dicionario_funcionario
            print(f'o {funcionario_maior_salario["nome"]} é o funcionario com o maior salário . Salário : {funcionario_maior_salario["salario"]}') 
                 

    elif analisar_opcao == '6':
        print('saindo...')
        break             
    else:
        print('apenas as opções acima!')
      
def remover_funcionario():  
    if not lista_funcionario:
        print('não há funcionarios aqui!')
        return   
    else:
          funcionario_remover = input('qual o funcionario que deseja remover : ')
          encontrado = False  
          for dicionario_funcionario in lista_funcionario:
            if funcionario_remover == dicionario_funcionario['nome']:
                lista_funcionario.remove(dicionario_funcionario)
                print(f'o funcionario {funcionario_remover} foi removido com sucesso!')
                encontrado = True              
          if not encontrado:
             print('funcionario inexistente!')
        
            
             

def menu():
    while True:
        print('---FUNCIONARIOS DA EMPRESA---')
        print(' 1 - cadastrar funcionarios\n 2 - mostrar funcionarios\n 3 - analisar funcionarios\n 4 - remover funcionario\n 5 - SAIR')
        opcao = input('o que deseja : ')
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            mostrar_funcionario()
        elif opcao == '3':
            analisar_funcionario()
        elif opcao == '4':
            remover_funcionario()
        elif opcao == '5':
            break 
        else:
            print('apenas as opções acima!')
      
menu()
      

