a=input().split()
t=int(a[0])
h=int(a[1])
c=0
#if t%2==0 and h%2==0:
#    if (t//2+h)%2!=0:
#        t-=2
#        h+=2
#        c+=4
#elif t%2!=0 and h%2==0:
#    if ((t+1)//2+h)%2!=0:
#        t-=1
#        h+=1
#        c+=2
#    else:
#        t-=3
#        h+=3
#        c+=6
#elif t%2!=0 and h%2!=0:
f=1
i=0
while f!=0:
    if (t+i)%2==0 and ((t+i)//2+h)%2==0:
        t-=i
        h+=i
        c=i*2
        f=0
    i+=1
#elif t%2==0 and h%2!=0:
#    if (t//2+h)%2!=0:
#        t-=1
#        h+=2
#        c+=4

print((t//2+h)//2+t//2+c)



# 1 6173 30247