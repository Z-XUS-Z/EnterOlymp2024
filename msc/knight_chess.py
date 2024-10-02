def dvij_konya(gor,vert,doska):
    
    if verka_konya(gor,vert)==1:
        a=[]
        if verka_konya(gor+1,vert+2)==1:
            if doska[gor+1][vert+2]==0:
                a.append([gor+1,vert+2])
            
        if verka_konya(gor+1,vert-2)==1:
            if doska[gor+1][vert-2]==0:
                a.append([gor+1,vert-2])
            
        if verka_konya(gor-1,vert+2)==1:
            if doska[gor-1][vert+2]==0:
                a.append([gor-1,vert+2])
            
        if verka_konya(gor-1,vert-2)==1:
            if doska[gor-1][vert-2]==0:
                a.append([gor-1,vert-2])
            
        if verka_konya(gor+2,vert+1)==1:
            if doska[gor+2][vert+1]==0:
                a.append([gor+2,vert+1])

        if verka_konya(gor+2,vert-1)==1:
            if doska[gor+2][vert-1]==0:
                a.append([gor+2,vert-1])

        if verka_konya(gor-2,vert+1)==1:
            if doska[gor-2][vert+1]==0:
                a.append([gor-2,vert+1])

        if verka_konya(gor-2,vert-1)==1:
            if doska[gor-2][vert-1]==0:
                a.append([gor-2,vert-1])
        return(a)
    return 0

def verka_konya(gor,vert):
    if gor<0 or gor>7 or vert<0 or vert>7:
        return 0
    return 1

#def donkihot(gor,vert,doska,count):
#    if count >= 64:
#        return doska
#    npm=dvij_konya(gor,vert,doska)
#    if len(npm)==0:
#        return doska[gor,vert]=-1
#    for i in npm:
#        donkihot(i[0],i[1],doska,count+1)
#    return doska

doska=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print(dvij_konya(6,5,doska))