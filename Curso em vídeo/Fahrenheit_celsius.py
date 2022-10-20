num1=float(input('Valor em fahrenheit\n'))
tem= num1-32 * (5/9)
print('ºf {} convertido para ºC {:.3}'.format(num1, tem))
print('='*40)
num2=float(input('Valor em celcius\n'))
tem1= num2 * (9/5) + 32
print('ºF{} convertido pra ºC é {}'.format(num2, tem1))