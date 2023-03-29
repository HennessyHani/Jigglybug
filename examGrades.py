mark = int(input('What is the mark? '))

if mark > 100 or mark < 1:
    print('  !!ERROR!!')
elif mark < 50:
    print('Fail')
elif mark < 61.70:
    print('Pass')
elif mark < 71.10:
    print('Merit')
else:
    print('Distinction')