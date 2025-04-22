print ('\n')
print ('CALCULADORA EM PYTHON\n')
print (f'↓' * 20 + '\n')

print ('1- ADIÇÃO +')
print ('2- SUBRITAÇÃO -')
print ('3- MULTIPLICAÇÃO')
print ('4- DIVISÃO')
print ('5-RAIZ QUADRADA')
print ('6-POTENCIAÇÃO')
print ('7-PORCENTAGEM\n')

numero = int(input ('Digite o número da operação que deseja realizar e tecle enter:'))
print ('\n')

if numero == 1:
    print ('Você escolheu adição!\n')
    na1 = float(input('Digite o primeiro número da adição e tecle enter: '))
    na2 = float(input('Digite o segundo número da adição e tecle enter: '))
    soma = na1 + na2 
    print (f'{na1} + {na2} = {soma}')
elif numero == 2:
    print ('Você escolheu subtração!\n')
    ns1 = float(input('Digite o primeiro número da subtração e tecle enter: '))
    ns2 = float(input('Digite o segundo número da subtração e tecle enter: '))
    subtracao = ns1 - ns2
    print (f'{ns1} - {ns2} = {subtracao}')
elif numero == 3:
    print ('Você escolheu multiplicação!\n')
    nm1 = float(input('Digite o primeiro número da multiplicação e tecle enter: '))
    nm2 = float(input('Digite o segundo número da multiplicação e tecle enter: '))
    multiplicacao = nm1 * nm2 
    print (f'{nm1} X {nm2} = {multiplicacao}')
elif numero == 4:
    print ('Você escolheu divisão!\n')
    print ('1- Divisão real')
    print ('2- Divisão inteira')
    print ('3- Resto da divisão')
    print ('\n')
    tipo_divisao = int(input('Digite o número de qual divisão deseja fazer, e tecle enter: '))
    print ('\n')

    if tipo_divisao == 1:
        nd1 = float(input('Digite o primeiro número da divisão e tecle enter: '))
        nd2 = float(input('Digite o segundo número da divisão e tecle enter: '))
        resultado_nd = nd1 / nd2
        print (f'{nd1} / {nd2} = {resultado_nd}')

    if tipo_divisao == 2:
        nd1i = float(input('Digite o primeiro número da divisão e tecle enter: '))
        nd2i = float(input('Digite o segundo número da divisão e tecle enter: '))
        resultado_ndi = nd1i // nd2i
        print (f'{nd1i} // {nd2i} = {resultado_ndi}')

    
    if tipo_divisao == 3:
        nd1r = float(input('Digite o primeiro número da divisão e tecle enter: '))
        nd2r = float(input('Digite o segundo número da divisão e tecle enter: '))
        resultado_ndr = nd1r % nd2r
        print (f'{nd1r} % {nd2r} = {resultado_ndr}')
