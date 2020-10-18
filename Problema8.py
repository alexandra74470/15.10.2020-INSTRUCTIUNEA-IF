a=int(input('introduceti primul numar'))
b=int(input('introduceti al doilea numar'))
if(a%2==0)and(b%2==0):
    if(a>b):
        print(a)
    elif(a==b):
        print(a,' ',b)
    else:
        print(b)
elif (a%2==0)and(b%2!=0):
    print(a)
elif(a%2!=0)and(b%2==0):
    print(b)
else:
    print('nu sunt numere pare')