# Faça um programa que tenha uma função chamada area(), 
# que receba as dimensoes de um terreno retangular (largura e 
# comprimento) e mostre a area do terreno
def area(larg, comp):
    a = larg * comp
    print(f'A Área de um terreno {larg}x{comp} é de {a} metro(s) quadrados.')
    

print('Controle de Terrenos')
print('--------------------')
larg = float(input('LARGURA  (m):'))
comp = float(input('COMPRIMENTO (m):'))
area(larg, comp)

