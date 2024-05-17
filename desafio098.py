#Faca um programa que tenha uma função chamada #contador(), que receba tres parametros: inicio
#fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens atraves da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada.
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        if passo > 0:
            passo *= -1
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ')

print('-=' * 15)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('FIM!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)
print('FIM!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
contador(inicio, fim, passo)
print('FIM!')