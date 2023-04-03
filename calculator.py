num1 = int(input('Enter a number '))
num2 = int(input('Enter another number '))

print('1. Add +')
print('2. Subtract -')
print('3. Multiply *')
print('4. Divide /')
print('5. Square s')

val = int(input('What operation would you like to perform? '))

if val == 1: 
    sum = num1 + num2
    print('Your answer is ', sum)
elif val == 2:
    sum = num1 - num2
    print('Your answer is ', sum)
elif val == 3:
    sum = num1 * num2
    print('Your answer is ', sum)
elif val == 4:
    sum = num1 / num2
    print('Your answer is ', sum)
elif val == 5:
    sum = num1 ** num2
    print('Your answer is ', sum)

   