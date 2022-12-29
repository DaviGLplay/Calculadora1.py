import math
import sys,time,os

message="\nOlá, meu nome e Davi Rios, eu criei esse projeto como exemplo do que o\
\npython pode fazer, sou iniciante ainda, e algumas programações mais avançadas eu\
\npeguei e juntei com a minha, e com o passar do tempo fui aprendendo o que cada\
\ncoisa fazia, espero que gostem do projeto inicial :) pois deu bastante trabalho:"


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)


os.system("12") #clear
typewriter(message)



def calculadora():

    op = input(
        '\n\033[1;33;34mQuel tipo de calculo você quer fazer?\
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
        print(calculadora())
    else:
        print('\033[4;33;33mO comando nao sera executado se nao digitar 1\033[m')


if __name__ == '__main__':
    main()
print('\n')
print('Obrigado por usar a calculadora python :)  ')
