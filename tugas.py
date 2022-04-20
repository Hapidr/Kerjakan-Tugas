

x = int(input())
y = int(input())
z = int(input())

if x > y:
    if x > z:
        if y > z:
            max = x
            min = z
            print(f'max {max}, min {min}')

        else:
            max = x
            min = y
            print(f'max {max}, min {min}')
    else:
        max = z
        min = y
        print(f'max {max}, min {min}')
elif x > z:
    max = y
    min = z
    print(f'max {max}, min {min}')
    if y > z:
        max = y
        min = x
        print(f'max {max}, min {min}')
    else:
        max = z
        min = x
        print(f'max {max}, min {min}')

