n1=int(input('introduceti prima nota'))
n2=int(input('introduceti a doua nota'))
n3=int(input('introduceti a treia nota'))
if(n3<8):
     if(n1>n2):
          print(n1)
     else:
          print(n2)
else:
     print(n1,' ',n2,' ',n3)