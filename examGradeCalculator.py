mark = int(input('What is the mark? '))
level = int(input('What is the level? '))

if level == 1:
    if mark > 100 or mark < 1:
        print('ERROR')
    elif mark < 50:
        print('Fail')
    elif mark < 61.70:
        print('Pass')
    elif mark < 71.10:
        print('Merit')
    else:
        print('Distinction') 

if level == 2:
    if mark > 100 or mark < 1:
        print('ERROR')
    elif mark < 40:
        print('Fail')
    elif mark < 51.65:
        print('Pass')
    elif mark < 66.10:
        print('Merit')
    else:
        print('Distinction') 
 