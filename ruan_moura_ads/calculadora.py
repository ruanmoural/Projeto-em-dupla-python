import math
import time

print('\n')
print('CALCULADORA EM PYTHON\n')
print(f'↓' * 20 + '\n')

while True:
    print('1- ADIÇÃO +')
    print('2- SUBTRAÇÃO -')
    print('3- MULTIPLICAÇÃO')
    print('4- DIVISÃO')
    print('5- RAIZ QUADRADA')
    print('6- POTENCIAÇÃO')
    print('7- PORCENTAGEM')
    print('8- TRIPLO')
    print('9- INVERSO')
    print('10- PAR OU ÍMPAR')
    print('11- SAIR')

    numero = int(input('Digite o número da operação que deseja realizar e tecle enter: '))
    print('\n')

    if numero == 1:
        print('Você escolheu adição!\n')
        time.sleep(2)
        na1 = float(input('Digite o primeiro número e tecle enter: '))
        na2 = float(input('Digite o segundo número e tecle enter: '))
        soma = na1 + na2
        print(f'{na1} + {na2} = {soma:.2f}')

    elif numero == 2:
        print('Você escolheu subtração!\n')
        time.sleep(2)
        ns1 = float(input('Digite o primeiro número e tecle enter: '))
        ns2 = float(input('Digite o segundo número e tecle enter: '))
        subtracao = ns1 - ns2
        print(f'{ns1} - {ns2} = {subtracao:.2f}')

    elif numero == 3:
        print('Você escolheu multiplicação!\n')
        time.sleep(2)
        nm1 = float(input('Digite o primeiro número e tecle enter: '))
        nm2 = float(input('Digite o segundo número e tecle enter: '))
        multiplicacao = nm1 * nm2
        print(f'{nm1} X {nm2} = {multiplicacao:.2f}')

    elif numero == 4:
        print('Você escolheu divisão!\n')
        time.sleep(2)
        print('1- Divisão real (/)')
        print('2- Divisão inteira (//)')
        print('3- Resto da divisão (%)\n')

        tipo_divisao = int(input('Digite o número do tipo de divisão e tecle enter: '))

        nd1 = float(input('Digite o primeiro número e tecle enter: '))
        nd2 = float(input('Digite o segundo número e tecle enter: '))

        if nd2 == 0:
            print('Erro: Divisão por zero não é permitida.')
        else:
            if tipo_divisao == 1:
                divisao_real = nd1 / nd2
                print(f'{nd1} / {nd2} = {divisao_real:.2f}')
            elif tipo_divisao == 2:
                divisao_inteira = nd1 // nd2
                print(f'{nd1} // {nd2} = {divisao_inteira}')
            elif tipo_divisao == 3:
                resto = nd1 % nd2
                print(f'{nd1} % {nd2} = {resto}')
            else:
                print('Opção inválida.')

    elif numero == 5:
        print('Você escolheu raiz quadrada!\n')
        time.sleep(2)
        nr1 = float(input('Digite um número para calcular a raiz quadrada: '))
        if nr1 < 0:
            print('Erro: não é possível calcular a raiz quadrada de número negativo.')
        else:
            resultado_raiz = math.sqrt(nr1)
            print(f'A raiz quadrada de {nr1} é {resultado_raiz:.2f}')

    elif numero == 6:
        print('Você escolheu Potenciação!\n')
        time.sleep(2)
        np1 = float(input('Digite um número para calcular a potência: '))
        np2 = float(input('Digite o número que deseja elevar: '))
        resultado_potencia = np1 ** np2
        print(f'{np1} elevado a {np2} é {resultado_potencia:.2f}')

    elif numero == 7:
        print('Você escolheu Porcentagem!\n')
        time.sleep(2)
        print('1 - Adicionar porcentagem ao valor (+)')
        print('2 - Subtrair porcentagem do valor (-)\n')

        tipo_porcentagem = int(input('Digite a opção desejada: '))
        valor = float(input('Digite o valor base: '))
        percentual = float(input('Digite a porcentagem: '))

        if tipo_porcentagem == 1:
            resultado_porcentagem_mais = valor + (valor * percentual / 100)
            print(f'{percentual}% adicionado a {valor} = {resultado_porcentagem_mais:.2f}')
        elif tipo_porcentagem == 2:
            resultado_porcentagem_menos = valor - (valor * percentual / 100)
            print(f'{percentual}% subtraído de {valor} = {resultado_porcentagem_menos:.2f}')
        else:
            print('Opção inválida. Retornando ao menu principal.')

    elif numero == 8:
        print('Você escolheu Triplo!\n')
        time.sleep(2)
        t = float(input('Digite um número: '))
        triplo = t * 3
        print(f'O triplo de {t} é {triplo:.2f}')

    elif numero == 9:
        print('Você escolheu Inverso!\n')
        time.sleep(2)
        i = float(input('Digite um número: '))
        if i == 0:
            print('Erro: não é possível calcular o inverso de zero.')
        else:
            inverso = 1 / i
            print(f'O inverso de {i} é {inverso:.4f}')

    elif numero == 10:
        print('Você escolheu Par ou Ímpar!\n')
        time.sleep(2)
        pi = int(input('Digite um número inteiro: '))
        if pi % 2 == 0:
            print(f'{pi} é PAR.')
        else:
            print(f'{pi} é ÍMPAR.')

    elif numero == 11:
        print('Saindo da calculadora... Até a próxima!')
        break

    else:
        print('Opção inválida. Tente novamente.')

    print('\n' + '-' * 40 + '\n')
    time.sleep(3)
