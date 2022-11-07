'''crie um progra que leia o nome colpleto de uma pessoa e mostre:
1- O nome com toda as letras maiúsculas 
2- O nome o nome com todas as letras menusculas
3- Quantas letras ao todo sem considera os epaços
4- Quantas letras tem o primeiro nome '''
    
              ##logica##
''''
01- pedir nome
02- colocar atributo 01 ao nome e printar
03- adicionar todos os atributos ao nome e printando um a um.
'''
'''a = str(input('Digite seu nome completo: '))
nome = a.upper()
num =  a.lower()
nu = len(a)
print(nome, num, nu)'''
       #Resolução da aula 
first=str(input('Nome completo: ')).strip()# vai puxar o nome e faze a contagens sem espaços 
print('Analisando seu nome...')
print('Seu nome de forma maiuscula é {}'.format(first.upper()))
print('DE forma minuscula é {}'.format(first.lower()))
print('Seu nome possue {} letras'.format(len(first)- first.count(' ')))# Ele vai ler as linhas e tirar os espaços me dando o valor
# Sem os espaços 
print('Seu primeiro nome tem {} letras'.format(first.find(' '))) # 'Find' vai encontrar o primeiro espaço e tudo que estiver antes do
# espaço a funçao ira me retornar...
recebe = first.split()
print('Seu primeiro nome é {} ele tem {} letras'.format(recebe[0], len(recebe[0])))
# Da segunda forma e criado mas uma variavel, dentro dela vai o split (que vai criar uma lista)
# já na formataçao, 'recebe' eu pesso o paramentro 0 da lista, no caso o primeiro nome 
# depois eu 'len'vai ler o nome é, vai me passar quantas letras tem no parameteo 0, todos os nomes que tem dentro. 

