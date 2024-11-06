from collections import deque

#def dedeck(a):
#    dek=deque()
#    n='net'
#    d='da'
#    for i in a:
#        if i =="(":
#            dek.append(i)
#        if i ==")":
#            if len(dek)==0:
#                return n
#            else:
#                dek.pop()
#    if len(dek)!=0:
#        return n
#    return d 
            

def dedeck(a):
    dek=deque()
    n='net'
    d='da'
    for i in a:
        if i =="(":
            dek.append(i)
        if i ==")":
            if len(dek)==0:
                return n
            else:
                if dek.pop()!="(":
                    return n
        if i =="[":
            dek.append(i)
        if i =="]":
            if len(dek)==0:
                return n
            else:
                if dek.pop()!="[":
                    return n
        if i =="{":
            dek.append(i)
        if i =="}":
            if len(dek)==0:
                return n
            else:
                if dek.pop()!="{":
                    return n
    if len(dek)!=0:
        return n
    return d 
            
        
print(dedeck(input()))