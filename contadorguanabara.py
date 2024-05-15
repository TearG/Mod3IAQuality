def contador(*num):
    #print(num)
    #for valor in num:
      #  print(f'{valor} ', end='')
    #print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)