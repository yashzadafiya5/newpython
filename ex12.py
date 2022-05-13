'''
    12) Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
'''

birthdate=int(input("enter your birthdate"))
birthmonth=int(input("enter your birthmonth"))


if (birthdate>=21  or birthmonth==3) and (birthdate<=19 or birthmonth==4):
    print("your zodic sign is  'aries' and your zodic symbole is 'The ram' ")
if (birthdate>=20  or birthmonth==4) and (birthdate<=20 or birthmonth==5):
    print("your zodic sign is  'Taurus' and your zodic symbole is 'The Bull' ")
if (birthdate>=21  or birthmonth==5) and (birthdate<=20 or birthmonth==6):
    print("your zodic sign is  'Gemini' and your zodic symbole is 'The Twins' ")
if (birthdate>=21  or birthmonth==6) and (birthdate<=22 or birthmonth==july):
    print("your zodic sign is 'Cancer' and your zodic symbole is 'The Crab' ")
if (birthdate>=23  or birthmonth==7) and (birthdate<=22 or birthmonth==8):
    print("your zodic sign is 'Leo' and your zodic symbole is 'The Lion' ")
if (birthdate>=23  or birthmonth==8) and (birthdate<=22 or birthmonth==9):
    print("your zodic sign is 'Virgo' aries and your zodic symbole is 'The Virgin ' ")
if (birthdate>=21  or birthmonth==9) and (birthdate<=19 or birthmonth==10):
    print("your zodic sign is 'Libra' and your zodic symbole is 'The Scales' ")
if (birthdate>=21  or birthmonth==10) and (birthdate<=19 or birthmonth==11):
    print("your zodic sign is 'Scorpio'  and your zodic symbole is 'The Scorpion' ")
if (birthdate>=21  or birthmonth==11) and (birthdate<=19 or birthmonth==12):
    print("your zodic sign is 'Sagittarius'  and your zodic symbole is 'The Archer' ")
if (birthdate>=21  or birthmonth==12) and (birthdate<=19 or birthmonth==1):
    print("your zodic sign is 'Capricorn'  and your zodic symbole is The 'Goat' ")
if (birthdate>=21  or birthmonth==1) and (birthdate<=19 or birthmonth==2):
    print("your zodic sign is 'Aquarius'  and your zodic symbole is 'The water Bearer' ")
if (birthdate>=21  or birthmonth==2) and (birthdate<=19 or birthmonth==3):
    print("your zodic sign is 'Pisces' and your zodic symbole is 'The Fishes' ")



