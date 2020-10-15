n1=int(input('introduceti numaul primului elev'))
n2=int(input('introduceti numarul elevului al doilea'))
n3=int(input('introduceti numarul elevului al treilea'))
p1=int(input('introduceti punctajul primului elev'))
p2=int(input('introduceti punctajul elevului al doilea'))
p3=int(input('introduceti punctajul elevului al treile'))
if(p1>p2)and(p1>p2):
    print(n1)
if(p2>p1)and(p2>p3):
    print(n2)
if(p3>p1)and(p3>p2):
    print(n3)
if(p1==p2)and(p1>p3)and(p2>p3):
    print(n1,'si',n2,',acelasi punctaj')
if(p1==p3)and(p1>p2)and(p3>p2):
    print(n1,'si',n3,',acelasi punctaj')
if(p2==p3)and(p2>p1)and(p3>p1):
    print(n2,'si',n3,',acelasi punctaj')
if(p2==p1)and(p2==p3)and(p1==p3):
    print('toti participanti au punctaj egal')