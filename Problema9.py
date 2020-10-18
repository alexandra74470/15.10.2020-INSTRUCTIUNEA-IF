xa=int(input('introduceti numarul bilelor mici de culoare alba'))
xr=int(input('introduceti numarul bilelor mici de culoare rosie'))
xv=int(input('introduceti numarul bilelor mici de culoare verde'))
ya=int(input('introduceti numarul bilelor mari de culoare alba'))
yr=int(input('introduceti numarul bilelor mari de culoare rosie'))
yv=int(input('introduceti numarul bilelor mari de culoare verde'))
xt=xa+xr+xv
yt=ya+yr+yv
print('total=',xt==yt)
if(xt>yt):
    print('bile mici sunt mai multe')
elif(yt>xt):
    print('bile mari sunt mai multe')
else:
    print('este un numar egal de bile mari si bile mici')
if((xa+ya>xr+yr)and(xa+ya>xv+yv)):
    print('bile albe')
if((xr+yr>xa+ya)and(xr+yr>xv+yv)):
    print('bile rosii')
if((xv+yv>xa+ya)and(xv+yv>xr+yv)):
    print('bile verzi')
if((xa+ya==xr+yr)and(xa+ya>xv+yv)and(xr+yr>xv+yv)):
    print('bile albe si rosii')
if((xa+ya==xv+yv)and(xa+ya>xr+yr)and(xv+yv>xr+yr)):
    print('bile albe si verzi')
if((xr+yr==xv+yv)and(xr+yr>xa+ya)and(xv+yv>xa+ya)):
    print('bile rosii si verzi')
if((xr+yr==xa+ya)and(xa+ya==xv+yv)and(xv+yv==xr+yr)):
    print('numarul bilelor de fiecare culoare este egal')