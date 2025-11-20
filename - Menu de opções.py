from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('=-' * 15)
    opção = int(input('>>>>> Qual é a sua opção: '))
    print('=-' * 15)
    sleep(1)
    if opção == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é igual a {}!'.format(v1, v2, soma))
        print('=-' * 15)
        sleep(1)
    elif opção == 2:
        multiplicar = v1 * v2
        print('A multiplicação entre {} e {} é igual a {}!'.format(v1, v2, multiplicar))
        print('=-' * 15)
        sleep(1)
    elif opção == 3:
        maior = max(v1, v2)
        print('Entre {} e {} o maior valor é {}!'.format(v1, v2, maior))
        print('=-' * 15)
        sleep(1)
    elif opção == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
        print('=-' * 15)
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos números')
        print('[ 5 ] sair do programa')
        print('=-' * 15)
        opção = int(input('>>>>> Qual é a sua opção: '))
        print('=-' * 15)
        sleep(1)
    elif opção == 5:
        sair = True
        print('Finalizando...')
        sleep(1)
        print('Fim do programa, volte sempre!')
    else:
        print('Opção inválida. Tente novamente.')
        print('=-' * 15)
        sleep(1)