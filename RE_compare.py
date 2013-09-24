import re

cnt=0
DEP=13 # recursion depth
re1=r'^(0|(10))*1*$'
re2=r'^((?!110).)*$'


def diff(mystr,dep):
    if dep>DEP:
        return
    m1=re.match(re1, mystr)
    m2=re.match(re2,mystr)
    global cnt
    cnt+=1
    DEBUG=0
    if m1!=None and m2!=None : # same
        if DEBUG==1:
            print cnt,'match succ',mystr#,m1,m2
        k=1
    elif m1==None and m2==None: # same
        if DEBUG==1:
            print cnt,'match succ', mystr
        k=1
    else:
        print cnt,'fail match',mystr,m1,m2
    diff(mystr+'0',dep+1)
    diff(mystr+'1',dep+1)
    return


diff('',0)
print 'finish'
