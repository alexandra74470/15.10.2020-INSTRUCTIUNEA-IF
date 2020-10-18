g=int(input("Numarul de gaini")) 
b=int(input("Numarul total de boabe")) 
t=b//g
c=b-(g*t) 
if t>c: 
    print("Gaina primeste mai mult cu",t-c,"boabe") 
elif c>t: 
    print("Curcanul primeste mai mult cu",c-t,"boabe") 
else: 
    print("Primesc acelasi numar de boabe")