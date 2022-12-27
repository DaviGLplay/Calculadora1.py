import math

def Calculadora():

    op = input(
        'Quel tipo de calculo você quer fazer?\
        \n Escolha entre: "+, -, *, /" : ')

    a = int(input('Primeiro numero: '))
    b = int(input('Segundo numero: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Erro, não use 0 na divisão'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Erro: O [0] nao pode ser dividido| Erro nao use [×] e [÷], use isso [*] para mutiplicação e isso [/'']Para divisão     "

def main():  # Wrapper function

    print("""Calculadora python""")
    choice = int(input('Digite 1 para começar: '))

    if choice == 1:
        print(Calculadora())
    else:
        print('O comando nao sera executado se nao digitar 1')


if __name__ == '__main__':
    main()
    
    
print('Obrigado por usar a calculadora feita no python :)')
