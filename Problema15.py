x=int(input('locul ocupat de Radu'))
if(x<=125):
    if(x%5==1):
        print('A')
    if(x%5==2):
        print('B')
    if(x%5==3):
        print('c')
    if(x%5==4):
        print('D')
    else:
        print('E')
else:
    print('Radu nu a intrat in lista elevilor din clasa a V-a')