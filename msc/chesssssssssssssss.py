def ches(kp,rp,rm):
    c=0

    a=rp
    while (a+1)%8!=0:
        a+=1
        if a==kp:
            c=1


    a=rp
    while a%8!=0:
        a-=1
        if a==kp:
            c=1

    
    a=rp
    while a-8>=0:
        a-=8
        if a==kp:
            c=1

    a=rp
    while a+8<=63:
        a+=8
        if a==kp:
            c=1


    if kp==rp or kp<0 or kp>63 or rp<0 or rp>63 or c==1:
        return 'illegal state'




    f=0
    
    a=rm
    while (a+1)%8!=0:
        a+=1
        if a==rp:
            f=1
        if a==kp:
            c=1


    a=rm
    while a%8!=0:
        a-=1
        if a==rp:
            f=1
        if a==kp:
            c=1

    
    a=rm
    while a-8>=0:
        a-=8
        if a==rp:
            f=1
        if a==kp:
            c=1

    a=rm
    while a+8<=63:
        a+=8
        if a==rp:
            f=1
        if a==kp:
            c =1
    if f==0:
        return 'move not allowed'
    if rm<0 or rm>63 or rm==kp or rm==rp or c==1:
        return 'illegal move'
    if (kp==0 and rm==9) or (kp==7 and rm==14) or (kp==56 and rm==49) or (kp==63 and rm==54):
        return 'stop'

    return "continue"

kp=54
rp=6
rm=7
#print(ches(kp,rp,rm))