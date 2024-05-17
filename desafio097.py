#Faca um programa que tenha uma função chamada escreva(),
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
def escreva(msg):
    a = len(msg)
    b = '-' * a
    print(b)
    print(msg)
    print(b)


msg = input('Digite sua mensagem, por favor:')
escreva(msg)
