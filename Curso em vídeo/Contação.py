# Faça um algoritmo que leia quantos a pessoa tem em real e veja quantos ela vai ter em dolares
a = float(input('Quantos você tem para viajar pelas americas\n '))
b = a * 5.16
c = a * 0.16
d = a * 1.41
e = a * 0.34
print('Você tem R${} convertido em dollars R${} na cotação do dia 23/10/2022\n'.format(a, b))
print('Real perante o peso bolivianon R${}\n'.format(c))
print('emirirados árabes R${}\n'.format(d))
print('Real diante do peso argentino R${}\n'.format(e, int(e)))
