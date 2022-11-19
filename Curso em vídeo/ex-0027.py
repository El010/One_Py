'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome 
speradamente 
ex: ana maria de sousa 
1- ana
2- sousa  
'''
nome = str(input('Digite seu nome completo: ')).strip()
firt = nome.split()
print('Seu primeiro nome é {}'.format(firt[0]))
print('Seu segundo nome é {}'.format(firt[len(firt)-1]))# len vai ler o nome e printar o ultimo nome que o usuario digitar