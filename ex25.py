# write a following patten a full peramid.
number=0
fun=3
while number<3:
    space=0
    while space<fun:
        print(" ",end="")
        space = space +1
    i=0
    while i <=number:
        print("* ",end="")
        i=i+1
    print("")
    number=number+1
    fun=fun-1