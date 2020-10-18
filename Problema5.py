ac=int(input('introduceti anul curent'))
lc=int(input('introduceti luna curenta'))
zc=int(input('introduceti ziua curenta'))
an=int(input('introduceti anul nasterii'))
ln=int(input('introduceti luna nasterii'))
zn=int(input('introduceti ziua nasterii'))
if lc==ln: 
     print(ac-an,'ani') 
else:
    print(ac-an+1,'ani')