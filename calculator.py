num1 = int(input('Enter a number '))
num2 = int(input('Enter another number '))

print('1. Add +')
print('2. Subtract -')
print('3. Multiply *')
print('4. Divide /')
print('5. Square s')

val = input('What operation would you like to perform? ')

if val == 1: 
   sum = num1 + num2 
   print('Your answer is ', sum)