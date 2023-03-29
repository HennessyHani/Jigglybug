print('Pythagoras Calculator')
print('1. Find the length of A given B and C')
print('2. Find the length of B given A and C')
print('3. Find the length of C given A and B')

value = int(input('What is your choice? '))
if value == 1:
    B = int(input('Enter a value for B '))
    C = int(input('Enter a value for C '))
    A = sqrt(C**2 - B**2)
    print('The value of A is ', A)
