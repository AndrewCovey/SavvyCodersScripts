def greet (name):
    print ('Hello ' + name.title() + '!')
    return 1

greet('Andrew')
greet('casey')


def add_items(price1, price2):
    return price1 + price2

success = add_items(2,4)
print('Result of add items(2.4): ' + str(success))


def generate_receipt(item, cost):
    print('Your item, ' + item + ', costs $' + str(cost) + '.  Thank you and have a nice day!')
    return 1

generate_receipt('Shrimp Gumbo', 14.95)
generate_receipt('Bannana Soufle', 7.25)