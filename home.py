# from reg import InsertUserInfo as sajili
# import read as soma
# import update as sasisha
# import delete as futaData
# import total as jumla

print('\t \n Select the number of the service you need from the options below.')
for x in range(80 + 1):
    print('-',end="")
    
print('''
        1: Register a new product.
        2: Read product menu.
        3: Update the product.
        4: Delete the product.
        5: Check the total balance.
      ''')

def getUserOption():
    try:
        option = int(input('Write the option number: > '))
        if option == 1:
            import reg
        elif option == 2:
            import read
        elif option == 3:
            import update
        elif option == 4:
            import delete
        elif option == 5:
            import total
        else:
            print('An option value is out of range, choose a correct one!')
        
                    
    except ValueError:
        print('Invalid option value, select a correct option!')
        
getUserOption()