
def dvij_konya_beta(gor,vert,doska):
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
        return(len(a))
    return 0

def greedy_sort(m):
    a=0
    for i in range(len(m)):
        for i in range(1,len(m)):
            if dvij_konya_beta(m[i][0],m[i][1],doska)>dvij_konya_beta(m[i-1][0],m[i-1][1],doska):
                a=m[i-1]
                m[i-1]=m[i]
                m[i]=a
            

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
        greedy_sort(a)
        return(a)
    return 0

def verka_konya(gor,vert):
    if gor<0 or gor>7 or vert<0 or vert>7:
        return 0
    return 1

def donkihot(gor,vert,doska,count):
    if count >= 64:
        return True
    npm=dvij_konya(gor,vert,doska)
    for i in npm:
        doska[i[0]][i[1]]=count
        if donkihot(i[0],i[1],doska,count+1):
            return True 
        doska[i[0]][i[1]]=0
    return False

doska=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
donkihot(3,3,doska,1)
print(doska)