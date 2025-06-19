def greet (name):
    print ('Hello ' + name + '!')
    return 1

greet('Andrew')

def generate_receipt(item, cost):
    print('Your item, ' + item + ', costs $' + str(cost) + '.  Thank you and have a nice day!')
    return 1

generate_receipt('Shrimp Gumbo', 14.95)