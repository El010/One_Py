'''
Crie um progrma que leia uma frase pelo teclado e mostre:
1- Quantas vezes aparece a letra A.
2- Em que posição ela aparece a primeira vez. 
3- Em que posição ela aparece na ultima vez.
'''
nome=str(input('Qual seu nome: \n')).strip()#Anula os espaços no começo e no final da entrada do usúario
print('Seu nome tem {} letras A '.format(nome.count('a')))#Conta quantas vezes aparece a letra A na variavel
print('A primeira letra A está no posição {} do seu nome'.format(nome.find('a')+1))#Mostra em qual posição dentro da memoria esta a letra que eu pedi, no caso A
print('a ultima posição que a letra A aparece é {}'.format(nome.rfind('a')+1))#vai pesquisar o nome da direita para a esquerda 