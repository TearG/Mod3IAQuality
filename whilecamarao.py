cardapio = ['frango a kiev', 
            'filet', 
            'bolinho de bacalhau', 
            'batata frita', 
            'camarão', 
            'costela ao molho barbecue']

item = cardapio.pop(0)

while item != 'camarão':
  print(f'Esse item não é o camarão! Este é {item} .Cadê o camarão?')
  item = cardapio.pop(0)

print(f'Aqui está o camarão! Este é {item} .')

