import random
import math

name = "yowaimo"

def inttobit(n):
    #print("entered inttobit")
    g= [int(digit) for digit in bin(n)[2:]] 
    f=8-len(g)
    i=[0]*f
    i.extend(g)
    return i
    #print("exited inttobit")
def inttobit5(n):
    #print("entered inttobit")
    g= [int(digit) for digit in bin(n)[2:]] 
    f=5-len(g)
    i=[0]*f
    i.extend(g)
    return i
    #print("exited inttobit")
def detect(p):
    if(sum(convert(lookWho(p),'enemy'))-3>0 or (sum(convert(lookWho(p),'both')))-3>0):
        return 1
    else:
        return 0
def bittoint(d):
    #print("entered bittoint")
    i=0
    for bit in d:
        i = (i << 1) | bit
    ####print(i)
    #print("exited bittoint")
    return i

def moveTo(x, y, Pirate):
    #print("entered moveTo")
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0]>x:
        return 4
    if position[0]<x:
        return 2
    if position[1]>y:
        return 1
    if position[1]<y:
        return 3
    #print("exited moveTo")
def moveToRake(x,y,pirate,dir):
    position = pirate.getPosition()
    if dir==1 or dir==3:
        if position[0]>x:
            return 4
        if position[0]<x:
            return 2
        if position[0] == x:
            return 0
    if dir==2 or dir==4:
        if position[1]>y:
            return 1
        if position[1]<y:
            return 3
        if position[1]==y:
            return 0

def tobits(s):
    #print("entered tobits")
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    #print("exited tobits")
    return result
def frombits(bits):
    #print("entered frombits")
    ####print(bits)###
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    #print("exited frombits")
    return ''.join(chars)  

def setint(i,s,startBit):
    #print("entered setint")
    g=inttobit(i)
    s[startBit:startBit+8]=g
    return g
    #print("exited setint")
def setRake(i,s):
    #print("entered setRake")
    rakePathBit=10
    rakePathLen=8
    g=inttobit(i+1)
    s[rakePathBit:rakePathBit+rakePathLen]=g
    #print("exited setRake")
def setAltRake(i,s):
    #print("entered setRake")
    rakePathBit=18
    rakePathLen=8
    g=inttobit(i+1)
    s[rakePathBit:rakePathBit+rakePathLen]=g
    #print("exited setRake")

def getint(s,startBit):
    #print("entered getint")
    g=s[startBit:startBit+8]
    i=bittoint(g)
    #print("exited getint")
    return i
def getRake(s):
    #print("entered getRake")
    ####print(s)
    rakePathBit__2=10
    rakePathLen=8
    g=s[rakePathBit__2:rakePathBit__2+rakePathLen]
    i=bittoint(g)
    #print("exited getRake")
    return i-1
def getAltRake(s):
    #print("entered getRake")
    ####print(s)
    rakeAltPathBit__2=18
    rakePathLen=8
    g=s[rakeAltPathBit__2:rakeAltPathBit__2+rakePathLen]
    i=bittoint(g)
    #print("exited getRake")
    return i-1
    
def assignSelfRake(queue,s,rakes,pirate):
    #print("entered assignSelfRake")
    flag=0
    rakeAssignBit=8
    if s[rakeAssignBit]==0:
        for i in range(len(queue)):
            if queue[i]==0:
                queue[i]=1
                setRake(i,s)
                s[rakeAssignBit]=1
                flag=1
                break
        
    #print("exited assignSelfRake")
    return (queue,flag)
def assignSelfAltRake(queue,s,rakesalt,pirate):
    #print("entered assignSelfRake")
    flag=0
    rakeAssignBit=8
    if s[rakeAssignBit+1]==0:
        for i in range(len(queue)):
            if queue[i]==0:
                queue[i]=1
                setAltRake(i,s)
                s[rakeAssignBit+1]=1
                flag=1
                break
        
    #print("exited assignSelfRake")
    return (queue,flag)
    


def selectRake(x,y,a,rakes,rakesalt):
    #print("entered selectRake")
    if(x==0 and y==0):
        i=0
        dir=2
        while(3*i+1<a+1):
            rakesalt.append([0,3*i])
            rakes.append([0,3*i+1])
            rakesalt.append([0,3*i+2])
            i+=1
    elif(x==0 and y==a-1):
        i=0
        dir=1
        while(3*i+1<a+1):
            rakesalt.append([3*i,a-1])
            rakes.append([3*i+1,a-1])
            rakesalt.append([3*i+2,a-1])
            i+=1
        #rakes.append([0,0])
    elif(x==a-1 and y==0):
        dir=3
        i=0
        while((a+1)-(3*i+1)>0):
            rakesalt.append([(a)-3*i,0])
            rakes.append([(a)-(3*i+1),0])
            rakesalt.append([(a)-(3*i+2),0])
            i+=1
        #rakes.append([a-1,a-1])
    elif(x==a-1 and y==a-1):
        dir=4
        i=0
        while((a+1)-(3*i+1)>0):
            rakesalt.append([a-1,(a)-(3*i)])
            rakes.append([a-1,(a)-(3*i+1)])
            rakesalt.append([a-1,(a)-(3*i+2)])
            i+=1
        #rakes.append([0,a-1])
    return dir
    #print("exited selectRake")

def look(p):
    views = [p.investigate_nw()[0],p.investigate_up()[0],p.investigate_ne()[0],
             p.investigate_left()[0],       ''          ,p.investigate_right()[0],
             p.investigate_sw()[0],p.investigate_down()[0],p.investigate_se()[0]]
    return views
def lookWho(p):
    views = [p.investigate_nw()[1],p.investigate_up()[1],p.investigate_ne()[1],
             p.investigate_left()[1],       ''          ,p.investigate_right()[1],
             p.investigate_sw()[1],p.investigate_down()[1],p.investigate_se()[1]]
    return views
def convert(views,key):
    ls=[]
    for i in views:
        if(i!=''):
            if(i==key):
                ls.append(1)
            else:
                ls.append(0)
        else:
            ls.append(3)
    return ls
def islandcheck(pirate,t,islandstartBit,islandlen,key):
    if(t[islandstartBit]==0):
        views=look(pirate)
        dx=-3
        dy=-3
        x,y=pirate.getPosition()
        v=convert(views,key)
        if(v==     [1,0,0,
                    0,3,0,
                    0,0,0 ]):
            dx=-2
            dy=-2
        if(v==     [1,1,0,
                    0,3,0,
                    0,0,0 ]):
                    dx=-1
                    dy=-2
        if(v==     [1,1,1,
                    0,3,0,
                    0,0,0 ]):
                    dx=0
                    dy=-2
        if(v==     [0,1,1,
                    0,3,0,
                    0,0,0 ]):
                    dx=1
                    dy=-2
        if(v==     [0,0,1,
                    0,3,0,
                    0,0,0 ]):
                    dx=2
                    dy=-2
        if(v==     [0,0,1,
                    0,3,1,
                    0,0,0 ]):
                    dx=2
                    dy=-1
        if(v==     [0,0,1,
                    0,3,1,
                    0,0,1 ]):
                    dx=2
                    dy=0
        if(v==     [0,0,0,
                    0,3,1,
                    0,0,1 ]):
                    dx=2
                    dy=1          
        if(v==     [0,0,0,
                    0,3,0,
                    0,0,1 ]):
                    dx=2
                    dy=2
        if(v==     [0,0,0,
                    0,3,0,
                    0,1,1]):
                    dx=1
                    dy=2
        if(v==     [0,0,0,
                    0,3,0,
                    1,1,1]):
                    dx=0
                    dy=2
        if(v==     [0,0,0,
                    0,3,0,
                    1,1,0]):
                    dx=-1
                    dy=2   
        if(v==     [0,0,0,
                    0,3,0,
                    1,0,0]):
                    dx=-2
                    dy=2
        if(v==     [0,0,0,
                    1,3,0,
                    1,0,0]):
                    dx=-2
                    dy=1
        if(v==     [1,0,0,
                    1,3,0,
                    1,0,0 ]):
                    dx=-2
                    dy=0
        if(v==     [1,0,0,
                    1,3,0,
                    0,0,0 ]):
                    dx=-2
                    dy=-1
        if(dx!=-3):
            bitx=inttobit(x+dx)
            bity=inttobit(y+dy)
            print("Island found at ",x+dx," ",y+dy)
            out=bitx+bity
            return out

def islandread(pirate,t,islandstartBit,islandlen):
    q=t[islandstartBit+1:islandstartBit+1+islandlen-1]
    x=bittoint(q[0:8])
    y=bittoint(q[8:16])
    return (x,y)

def listintobit(l):
    #print("entered listintobit")
    g=[]
    for i in l:
        g.extend(inttobit5(i))
    #print("exited listintobit")
    return g     
def listbittoint(l):
    #print("entered listbittoint")
    g=[]
    for i in range(0,len(l),5):
        g.append(bittoint(l[i:i+5]))
    #print("exited listbittoint")
    return g  

##############################

def ActPirate(pirate):
    ID=pirate.getID()
    rakes=[]
    rakesalt=[]
    #startbit2=startBit1 + len1
    #TODO: Add code here to add rakes
    
    dir=0
    finalMoveDir=0
    x,y=pirate.getDeployPoint()
    a=pirate.getDimensionX()
    dir=selectRake(x,y,a,rakes,rakesalt)
    t=tobits(pirate.getTeamSignal())
    s=tobits(pirate.getSignal())

    ###for team msg
    maxPirates=0.1*a*a
    teamStatus=getint(t,0)
    rakeQueueStartBit=8
    rakeQueueLen=len(rakes)
    altRakeStartBit=rakeQueueStartBit+rakeQueueLen
    altRakeStartLen=len(rakesalt)
    island1startBit= altRakeStartBit+altRakeStartLen
    island1len=17
    island2startBit= island1startBit+island1len
    island2len=17
    island3startBit= island2startBit+island2len
    island3len=17
    island1lurkbit=island3startBit+island3len
    island2lurkbit=island1lurkbit+1
    island3lurkbit=island2lurkbit+1 
    island1defenceSet=island3lurkbit+1
    island1defenceSetLen=45
    island2defenceSet=island1defenceSet+island1defenceSetLen
    island2defenceSetLen=45
    island3defenceSet=island2defenceSet+island2defenceSetLen
    island3defenceSetLen=45
    island1woodbit=island3defenceSet+island3defenceSetLen
    island2woodbit=island1woodbit+1
    island3woodbit=island2woodbit+1
    ###for team msg

    ###for self msg
    selfStatus=getint(s,0)
    rakeStatus=8
    rakePathBit__2=10
    rakeAltPathBit__2=18
    trawlStatusBit=26
    trawlCompletionBit=27
    defendingIslandNumberBit=28
    defendingIslandNumberPos=30
    defendingIslandNumberPosLen=5
    ###for self msg

    ##############
    bootMsg =[0]*800
    bootMsg2=[1]*800
    if(len(t)==0):
        t=bootMsg
    if(len(s)==0):
        s=bootMsg
    ##############

    pos=[[-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1]]
    flag=0
    flag1=0
    i=0
    if(teamStatus==1):
        if((s[rakeStatus]==0 and s[rakeStatus+1]==0)or selfStatus==3):
            if(s[defendingIslandNumberBit]==0 and s[defendingIslandNumberBit+1]==0):
                l1=listbittoint(t[island1defenceSet:island1defenceSet+island1defenceSetLen])
                for i in range(0,len(l1)):
                    r=l1[i]
                    if(r!=0):
                        flag1=1
                        s[defendingIslandNumberBit]=0
                        s[defendingIslandNumberBit+1]=1
                        s[defendingIslandNumberPos:defendingIslandNumberPos+defendingIslandNumberPosLen]=inttobit5(i)
                        k=island1defenceSet+(i*5)
                        t[k:k+5]=inttobit5(r-1)
                        selfStatus=1
                        break
                l2=listbittoint(t[island2defenceSet:island2defenceSet+island2defenceSetLen])
                for i in range(0,len(l2)):
                    r=l2[i]
                    if(r!=0):
                        flag1=1
                        s[defendingIslandNumberBit]=1
                        s[defendingIslandNumberBit+1]=0
                        s[defendingIslandNumberPos:defendingIslandNumberPos+defendingIslandNumberPosLen]=inttobit5(i)
                        k=island2defenceSet+(i*5)
                        t[k:k+5]=inttobit5(r-1)
                        selfStatus=1
                        break
                    
                l3=listbittoint(t[island3defenceSet:island3defenceSet+island3defenceSetLen])
                for i in l3:
                    r=l3[i]
                    if(r!=0):
                        flag1=1
                        s[defendingIslandNumberBit]=1
                        s[defendingIslandNumberBit+1]=1
                        s[defendingIslandNumberPos:defendingIslandNumberPos+defendingIslandNumberPosLen]=inttobit5(i)
                        k=island3defenceSet+(i*5)
                        t[k:k+5]=inttobit5(r-1)
                        selfStatus=1
                        break
                    
            else:
                flag1=1
                islandstartbit=0
                islandwoodbit=0
                islandN=bittoint([s[defendingIslandNumberBit],s[defendingIslandNumberBit+1]])
                if(islandN==1):
                    islandstartbit=island1startBit
                    islandwoodbit=island1woodbit
                elif(islandN==2):
                    islandstartbit=island2startBit
                    islandwoodbit=island2woodbit
                elif(islandN==3):
                    islandstartbit=island3startBit
                    islandwoodbit=island3woodbit
            
                x,y=islandread(pirate,t,islandstartbit,17)
                i=bittoint(s[defendingIslandNumberPos:defendingIslandNumberPos+defendingIslandNumberPosLen])
                x-=pos[i][0]
                y-=pos[i][1]
                print("Defending island ",x," ",y)
                if(pirate.getPosition()==(x,y)):
                    t[islandwoodbit]=detect(pirate)
                finalMoveDir=moveTo(x,y,pirate)
        

    if(selfStatus==0 or selfStatus==2 or selfStatus==3):
        if(s[rakeStatus]==0 and s[rakeStatus+1]==0): 
            t[rakeQueueStartBit:rakeQueueStartBit+rakeQueueLen],flag=assignSelfRake(t[rakeQueueStartBit:rakeQueueStartBit+rakeQueueLen],s,rakes,pirate)
            if(flag==1):
                i=getRake(s)
                if(i==0):
                    pass
                if(i!=-1):
                    x,y=rakes[i]
                    finalMoveDir=moveToRake(x,y,pirate,dir)
                    if finalMoveDir!=0:
                        s[rakeStatus]=1
                        s[rakeStatus+1]=0
                    elif finalMoveDir==0:
                        s[rakeStatus]=1
                        s[rakeStatus+1]=1
                else:
                    flag1=1
            else :
                t[altRakeStartBit:altRakeStartBit+altRakeStartLen],flag=assignSelfAltRake(t[altRakeStartBit:altRakeStartBit+altRakeStartLen],s,rakesalt,pirate)
                i=getAltRake(s)
                if(i!=-1):
                    flag1=1
                    x,y=rakesalt[i]
                    finalMoveDir=moveToRake(x,y,pirate,dir)
                    if finalMoveDir!=0:
                        s[rakeStatus]=0
                        s[rakeStatus+1]=1
                    elif finalMoveDir==0:
                        s[rakeStatus]=1
                        s[rakeStatus+1]=1

                
        elif(s[rakeStatus]==0 and s[rakeStatus+1]==1):
            i=getAltRake(s)
            if(i==0):
                pass
            if(i!=-1):
                flag1=1
                x,y=rakesalt[i]
                finalMoveDir=moveToRake(x,y,pirate,dir)
                if finalMoveDir!=0:
                    s[rakeStatus]=0
                    s[rakeStatus+1]=1
                if finalMoveDir==0:
                    s[rakeStatus]=1
                    s[rakeStatus+1]=1

            
        elif(s[rakeStatus]==1 and s[rakeStatus+1]==0):
            i=getRake(s)
            if(i==0):
                pass
            if(i!=-1):
                flag1=1
                x,y=rakes[i]
                finalMoveDir=moveToRake(x,y,pirate,dir)
                if finalMoveDir!=0:
                    s[rakeStatus]=1
                    s[rakeStatus+1]=0
                if finalMoveDir==0:
                    s[rakeStatus]=1
                    s[rakeStatus+1]=1
        
        elif(s[rakeStatus]==1 and s[rakeStatus+1]==1):
            flag1=1
            trawlStatus=s[trawlStatusBit]
            finalMoveDir,trawlStatusF,trawlCompletion=trawl(pirate,x,y,dir,trawlStatus,a)
            if(selfStatus==0 and trawlStatusF!=trawlStatus):
                selfStatus=2
            elif(selfStatus==2 and trawlStatusF!=trawlStatus):
                selfStatus=3
            s[trawlStatusBit]=trawlStatusF
            s[trawlCompletionBit]=trawlCompletion


        if(t[island1startBit]==0):
            a=islandcheck(pirate,t,island1startBit,island1len,'island1')
            if(a!=None):
                t[island1startBit]=1
                t[island1startBit+1:island1startBit+1+island1len-1]=a
        if(t[island2startBit]==0):
            a=islandcheck(pirate,t,island2startBit,island2len,'island2')
            if(a!=None):
                t[island2startBit]=1
                t[island2startBit+1:island2startBit+1+island2len-1]=a
        if(t[island3startBit]==0):
            a=islandcheck(pirate,t,island3startBit,island3len,'island3')
            if(a!=None):
                t[island3startBit]=1
                t[island3startBit+1:island3startBit+1+island3len-1]=a
    
        #
    if(flag1==0): #aaaa
        if(t[island1lurkbit]==1):
            x,y=islandread(pirate,t,island1startBit,island1len)
            #print("Lurking at island1",x,' ',y)
            finalMoveDir=moveTo(x,y,pirate)
        if(t[island2lurkbit]==1):
            x,y=islandread(pirate,t,island2startBit,island2len)
            #print("Lurking at island2",x,' ',y)
            finalMoveDir=moveTo(x,y,pirate)
        if(t[island3lurkbit]==1):
            x,y=islandread(pirate,t,island3startBit,island3len)
            #print("Lurking at island3",x,' ',y)
            finalMoveDir=moveTo(x,y,pirate)
        #
    
    #################
    if((x,y)==pirate.getDeployPoint() and finalMoveDir==2):
        print(ID," ",selfStatus," ",i," ",finalMoveDir)
    s[0:0+8]=inttobit(selfStatus)
    t[0:0+8]=inttobit(teamStatus)
    pirate.setTeamSignal(frombits(t))
    pirate.setSignal(frombits(s))
    return finalMoveDir

def trawl(pirate,x,y,dir,trawlStatus,a):
    dirAct=dir
    trawlCompletionBit=0
    trawlStatusF=trawlStatus
    lookTarget=0
    dx=0
    dy=0
    if(trawlStatus==1):
        if(dir==1):
            dirAct=3
        elif(dir==2):
            dirAct=4
        elif(dir==3):
            dirAct=1
        elif(dir==4):
            dirAct=2

    if(dirAct==1):
        lookTarget=1
        dy=-1
    elif(dirAct==2):
        lookTarget=5
        dx=1
    elif(dirAct==3):
        lookTarget=7
        dy=1
    elif(dirAct==4):
        lookTarget=3
        dx=-1
    k=convert(look(pirate),'wall')[lookTarget]
    print("k:",look(pirate))
    if(k!=0 and (x==0 or x==a-1 or y==0 or y==a-1)):
        trawlCompletionBit=1
        if(trawlStatus==0):
            trawlStatusF=1
        elif(trawlStatus==1):
            trawlStatusF=0
    elif(((x+dx)>-1 or (x+dx)<a or (y+dy)>-1 or (y+dy)<a)!=True):
        trawlCompletionBit=1
        if(trawlStatus==0):
            trawlStatusF=1
        elif(trawlStatus==1):
            trawlStatusF=0
   

    return (dirAct, trawlStatusF,trawlCompletionBit)


def ActTeam(team):
    t=tobits(team.getTeamSignal())
    l=team.getListOfSignals() 
    #print(team.getTotalGunpowder()," ",team.getTotalRum()," ",team.getTotalWood()," ",len(l))
    sl=[]
    for i in l:
        sl.append(tobits(i))
    rakes=[]
    rakesalt=[]
    #startbit2=startBit1 + len1
    #TODO: Add code here to add rakes
    
    dir=0
    finalMoveDir=0
    x,y=team.getDeployPoint()
    a=team.getDimensionX()
    dir=selectRake(x,y,a,rakes,rakesalt)

    ###for team msg
    teamStatus=getint(t,0)
    rakeQueueStartBit=8
    rakeQueueLen=len(rakes)
    altRakeStartBit=rakeQueueStartBit+rakeQueueLen
    altRakeStartLen=len(rakesalt)
    island1startBit= altRakeStartBit+altRakeStartLen
    island1len=17
    island2startBit= island1startBit+island1len
    island2len=17
    island3startBit= island2startBit+island2len
    island3len=17
    island1lurkbit=island3startBit+island3len
    island2lurkbit=island1lurkbit+1
    island3lurkbit=island2lurkbit+1
    island1defenceSet=island3lurkbit+1
    island1defenceSetLen=45
    island2defenceSet=island1defenceSet+island1defenceSetLen
    island2defenceSetLen=45
    island3defenceSet=island2defenceSet+island2defenceSetLen
    island3defenceSetLen=45
    island1woodbit=island3defenceSet+island3defenceSetLen
    island2woodbit=island1woodbit+1
    island3woodbit=island2woodbit+1
    
    ###for team msg
    print()
    ###for self msg
    rakeStatus=8
    rakePathBit__2=10
    rakeAltPathBit__2=18
    trawlStatusBit=26
    trawlCompletionBit=27
    defendingIslandNumberBit=28
    defendingIslandNumberPos=30
    defendingIslandNumberPosLen=5
    ###for self msg
    bootMsg =[0]*800
    if(len(t)==0):
        t=bootMsg

    if(t[island1woodbit]==1):
        team.buildWalls(1)
    if(t[island2woodbit]==1):
        team.buildWalls(2)
    if(t[island3woodbit]==1):
        team.buildWalls(3)


    j=t[island1startBit]+t[island2startBit]+t[island3startBit]
    if(j==1):
        teamStatus=1
    if(j==2):
        teamStatus=2
    n=len(sl)

    if(teamStatus==1):
        island1DefenceList=[0]*9
        island2DefenceList=[0]*9
        island3DefenceList=[0]*9
        for i in range(len(sl)):
            if(sl[i]==[]):
                continue
            k=sl[i][defendingIslandNumberPos:defendingIslandNumberPos+defendingIslandNumberPosLen]
            if(sl[i][defendingIslandNumberBit]==0 and sl[i][defendingIslandNumberBit+1]==1):
                island1DefenceList[bittoint(k)]+=1
            elif(sl[i][defendingIslandNumberBit]==1 and sl[i][defendingIslandNumberBit+1]==0):
                island2DefenceList[bittoint(k)]+=1
            elif(sl[i][defendingIslandNumberBit]==1 and sl[i][defendingIslandNumberBit+1]==1):
                island3DefenceList[bittoint(k)]+=1
        v=min(n//10,5)
        island1required=[0,v,0,
                         v,0,v,
                         0,v,0]
        island2required=[0,0,0,
                         0,0,0,
                         0,0,0]
        island3required=[0,0,0,
                        0,0,0,
                        0,0,0]
        island1target=[]
        for i in range(9):
            island1target.append(island1required[i]-island1DefenceList[i])
        island2target=[]
        for i in range(9):
            island2target.append(island2required[i]-island2DefenceList[i])
        island3target=[]
        for i in range(9):
            island3target.append(island3required[i]-island3DefenceList[i])
        print(island1target)
        t[island1defenceSet:island1defenceSet+island1defenceSetLen]=listintobit(island1target)
        t[island2defenceSet:island2defenceSet+island2defenceSetLen]=listintobit(island2target)
        t[island3defenceSet:island3defenceSet+island3defenceSetLen]=listintobit(island3target)
        



    #status 1,2,3 correspond to lurk islands
    if(j>0):
        if(teamStatus==0 or teamStatus==1):
            if(t[island1startBit]==1):
                teamStatus=1
                t[island1lurkbit]=1
            elif(t[island2startBit]==1):
                teamStatus=1
                t[island2lurkbit]=1
            elif(t[island3startBit]==1):
                teamStatus=1
                t[island3lurkbit]=1
        
    if(teamStatus==0 or teamStatus==1 ):
        rakeList=[0]*len(rakes)
        for i in sl:
            pos=getRake(i)
            rakeList[pos]=1
        rakeAltList=[0]*len(rakesalt)
        for i in sl:
            pos=getAltRake(i)
            rakeAltList[pos]=1
        t[rakeQueueStartBit:rakeQueueStartBit+rakeQueueLen]=rakeList
        t[altRakeStartBit:altRakeStartBit+altRakeStartLen]=rakeAltList

    t[0:0+8]=inttobit(teamStatus)
    team.setTeamSignal(frombits(t))
