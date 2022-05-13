
row=0
while row<=5:
    column=1
    while column<=row:
        if column%2==0:
            print('2',end=' ')
        elif column%3==1:
            print('3',end=' ')
        else:
            print('1',end=' ')
        
        column=column+1
    print("")
    row=row+1