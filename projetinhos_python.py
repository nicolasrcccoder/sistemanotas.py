notaArquivo = 'notas.txt'

def add_nota():
  while True:  
    try: 
     nome_adicionar = str(input('digite o nome do aluno (aperte s para sair) : '))
     if nome_adicionar.lower() == 's':
         print('saindo...')
         break
     nota_adicionar = float(input('digite a nota do aluno(0 - 10) :')) 
     if nota_adicionar > 10 or nota_adicionar < 0:
       print('apenas números de 0 a 10! ')
     else:
        with open('notas.txt' , 'a') as notaArquivo:
            notaArquivo.write(f'{nome_adicionar} - {nota_adicionar}\n')
    except ValueError:
      print('apenas números , isto é para adicionar uma nota!')         


def mostrar_notas():
   with open ('notas.txt' , 'r') as notaArquivo:
    try:
        mostrando_notas = notaArquivo.readlines()
        if not mostrando_notas:
           print('não há nada aqui ainda')       
        else:
           for i , nota in enumerate(mostrando_notas , 1 ):
              print(f' {i} - {nota.strip()}')
    except FileNotFoundError:
      print('arquivo não encontrado!')


def atualizar_notas():
   buscando_nome = str(input('procure o nome:'))
   try:
       with open('notas.txt' , 'r') as notaArquivo:
          procurando_linhas = notaArquivo.readlines()

       atualizado = False   
       with open('notas.txt' , 'w') as notaArquivo:
          for linha in procurando_linhas:
             nome , nota = linha.strip().split(' - ')
             #aqui a "linha.strip" faz com que tire a "\n" do console
             # e o ".split(-)" faz com que a o nome - nota fique valores diferente como nome , nota
             if nome.lower() == buscando_nome:
                nova_nota = float(input(f'digite a nova nota para o {nome} : '))
                notaArquivo.write(f'{nome} - {nova_nota}\n') 
                atualizado = True            
             else:
                notaArquivo.write(f'{linha}')
       if atualizado:
          print(f'a nota de {buscando_nome} atualizada com sucesso!')
       else:
          print('aluno não encontrado')

   except FileNotFoundError:
      print('arquivo não encontrado!') 

def menu():
   print('---PROGRAMA DE NOTAS DOS ALUNOS---')
   print(' 1 - adicionar nota')
   print(' 2 - mostrar notas')
   print(' 3 - atualizar notas') 
   print(' 4 - SAIR') 

def main():
  while True: 
   menu()
   opcao = (input('qual opcao :'))
   if opcao == '1':
      add_nota()
   elif opcao == '2':
      mostrar_notas()
   elif opcao == '3':
      atualizar_notas()    
   elif opcao == '4':
      print('encerrando o programa...')
      break
   else:
      print('opção invalida!') 

main() 


