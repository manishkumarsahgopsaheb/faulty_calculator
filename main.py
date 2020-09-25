# i have to build a faulty calculator which shows the correct result
# for all the operations except some of the operation like
# 45*3=555, 56+9=77,56/6=4

operator = input('enter the operator')
val1 = int(input('enter the first operand'))
val2 = int(input('enter the second operand'))

if operator == '*':
    if val1 == 45 and val2 == 3:
        print('555')
    else:
        print('multiplication is:', val1*val2)
elif operator == '+':
    if val1 == 56 and val2 == 9:
        print('77')
    else:
        print('sum is:', val1 + val2)
elif operator == '/':
        if val1 == 56 and val2 == 6:
            print('4')
        else:
            print('division is:', val1/val2)
elif operator == '-':
    print('substraction is:', val1-val2)