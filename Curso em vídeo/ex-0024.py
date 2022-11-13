''' crie um progrma que leia o nome de uma cidade e diga se ela começa ou não como nome SANTO''' 
ci=str(input('Qual cidade você nesceu \n')).strip().lower() # formata o valor sem espaço, e tranforma a resposta mesmo
a = 'santo' in ci                                   # mauncula em minúsculas 
print(a)


# resolução da aula 
cid = str(input('Qual cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')