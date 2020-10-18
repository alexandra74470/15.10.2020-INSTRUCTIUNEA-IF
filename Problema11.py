a=int(input('introduceti primul numar'))
b=int(input('introduceti al doilea numar'))
c=int(input('introduceti al treilea numar'))
if((a%2==0)and(b%2==0)and(c%2==0)):
    print(a,'par',b,'par',c,'par')
if((a%2==0)and(b%2!=0)and(c%2==0)):
    print(a,'par',b,'impar',c,'par')
if((a%2==0)and(b%2==0)and(c%2!=0)):
    print(a,'par',b,'par',c,'impar')
if((a%2!=0)and(b%2==0)and(c%2==0)):
    print(a,'impar',b,'par',c,'par')
if((a%2!=0)and(b%2!=0)and(c%2!=0)):
    print(a,'impar',b,'impar',c,'impar')
if((a%2!=0)and(b%2==0)and(c%2!=0)):
    print(a,'impar',b,'par',c,'impar')
if((a%2!=0)and(b%2!=0)and(c%0==0)):
    print(a,'impar',b,'impar',c,'par')
if((a%2==0)and(b%2!=0)and(c%2!=0)):
    print(a,'par',b,'impar',c,'impar')