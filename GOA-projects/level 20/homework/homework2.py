print('''available products:
        
cola(1), fanta'(2), pepsi(3), 
lays(4), doritos(5), pringles(6), 
snikers(7), kitkat(8), kinder(9).
      
      ''')



user_input = int(input('enter product number:  '))

products = ['cola', 'fanta', 'pepsi', 
            'lays', 'doritos', 'pringles', 
            'snikers', 'kitkat', 'kinder']



user_choice = products [ user_input-1 ]
print(' ')
print('You recieved ' + user_choice + '!')
print(' ')


















































































