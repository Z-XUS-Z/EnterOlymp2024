
def autist_cut (stiks, tail):
    alstiks = stiks[0]
    if tail == 3:
        alstiks +=sum(stiks[-3:])+stiks[-2]
        stiks = stiks[1:]
        return alstiks
    
    alstiks+= sum(stiks[-2:])*stiks[-2]
    stiks=stiks[1:]
    return alstiks
    
    
    
l=int(input())
stiks=[]
maxn=0
maxl=l
stik=int(input())
stiks.append(stik)
for i in range(2,l+1):
    stik=int(input())
    stiks.append(stik)
    if i % 2 ==0:
        continue
    q = autist_cut(stiks, 2 if len(stiks)==3 else 2)
    if q > maxn:
        maxn=q
        maxl=(i-1)//2
    
if l%2 == 0:
    q=autist_cut(stiks,2)
    if q >maxn:
        maxn=q
        maxl= l//2
        
print("tadam",maxl,maxn)