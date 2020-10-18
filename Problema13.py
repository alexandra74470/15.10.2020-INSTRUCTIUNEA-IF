x=int(input('introduceti locul pe care l-a ocupat Ionel'))
if(x<100):
    if(x%4==1):
        print('alb')
    if(x%4==2):
        print('rosu')
    if(x%4==3):
        print('albastru')
    else:
        print('negru')
else:
    print('Ionel nu a primit tricou')