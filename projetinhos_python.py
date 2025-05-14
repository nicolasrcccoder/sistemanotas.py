print('1 - adicionar contato')
print('2 - ver todos os contatos')
print('3 - buscar contato')
print('4 - remover contato')
print('5 - sair')
contatos = []

try:
 while True:
   opcao = int(input('digite sua opcao :'))
   if opcao == 5:
     print('você apertou sair, encerrando o programa...')
     break
   elif opcao == 1 :
     contatos.append(input('adicione um contato:'))
     print(f'você adicionou este contato na sua lista')
   elif opcao == 2 :
     print(f'seus contatos abaixo :\n{contatos}')  
   elif opcao == 3 :
     buscando_contato = input('digite o nome do contato para ligar:')
     if buscando_contato in contatos:
      ligar_ou_nao = input(f'você quer ligar para {buscando_contato}? (sim/não):')
      if ligar_ou_nao == 'sim':
           print('chamando...')
           print('ligação encerrada!')    
      else:
           print('você saiu')
     else:
        print('você não tem este contato!')        
   
   elif opcao == 4:
       contatos.remove(input('digite um contato para excluir:'))
       print(f'você removeu este contato!')


except ValueError:
  print('usuario inexistente ou apenas numeros!')