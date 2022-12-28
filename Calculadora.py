import math

def Calculadora():

    op = input(
        '\033[1;33;34mQuel tipo de calculo você quer fazer?\
        \n Escolha entre: "+,  -,  *,  / :\033[m')

    a = int(input('\033[4;33;37mPrimeiro numero:\033[m '))
    b = int(input('\033[4;33;37mSegundo numero: \033[m'))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return '\033[1;33;31mErro:\033[m\
Nao use 0 no divisor, \
Obrigado pela atenção :) '
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "\033[1;33;31mErro:\033[1;33;30mescolha entre as opções que estão na pergunta,\
    \nObrigado pela atenção :)\033[m"

def main():  # Wrapper function

    print("""\033[1;33;31mCalculadora python\033[m""")
    choice = int(input('\033[1;33;32mDigite 1 para começar:\033[m'))

    if choice == 1:
        print(Calculadora())
    else:
        print('\033[4;33;33mO comando nao sera executado se nao digitar 1\033[m')


if __name__ == '__main__':
    main()
print('\n')
print('OBRIGADO POR USAR A CALCULADORA FEITA NO PYTHON')




