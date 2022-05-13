#inverted half peramid
number=0
while number<=5:
    i=1
    while i<=number:
        if i%2==0:
            print('2',end='')
        else:
            print('1',end='')
    
        i=i+1
    i=0
    print("")
    number=number+1