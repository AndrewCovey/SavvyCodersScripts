def calc(num1, num2, oper):
    return eval(str(num1) + ' ' + str(oper) + ' ' + str(num2))

num1 = float(input('Provide a number: '))
num2 = float(input('Provide another number: '))
oper = str(input('Provide a four function arithmetic operator (+,-,*,/): '))

print('Your equation is ' + str(num1) + ' ' + str(oper) + ' ' + str(num2) + '; and the answer is: ' + str(calc(num1, num2, oper)))