cont = 0

while True:
    n = int(input('quer ver a tabuada de qual valor? '))
    print('-' * 18)
    if n < 0:
        break
    for c in range(1, 11):
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    cont = 0
    print('-' * 18)
print('programa de tabuada encerrado. volte sempre!')
