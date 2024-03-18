import random
import math

name = "sample1"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    print(position)
    if position[0] == x and position[1] == y:
        return 0
    if position[0]>x:
        print("down")
        return 4
    if position[0]<x:
        return 2
        print("up")
    if position[1]>y:
        return 1
        print("left")
    if position[1]<y:
        return 3
        print("right")

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result
def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)  


def ActPirate(pirate):
    rakes=[]
    dirx=-1
    diry=-1
    x,y=getDeployPoint()
    if(x==0 and y==0):
        rakes=[(1,1,2),(1,1,3),
                (4,4,2),(4,4,3),
                (7,7,2),(7,7,3),
                (10,10,2),(10,10,3),
                (13,13,2),(13,13,3),
                (16,16,2),(16,16,3),
                (19,19,2),(19,19,3),
                (22,22,2),(22,22,3),
                (25,25,2),(25,25,3),
                (28,28,2),(28,28,3),
                (31,31,2),(31,31,3),
                (34,34,2),(34,34,3),
                (37,37,2),(37,37,3)]
    elif(x==0 and y==39):
        rakes=[(1,38,1),(1,38,2),
                (4,35,1),(4,35,2),
                (7,32,1),(7,32,2),
                (10,29,1),(10,29,2),
                (13,26,1),(13,26,2),
                (16,23,1),(16,23,2),
                (19,20,1),(19,20,2),
                (22,17,1),(22,17,2),
                (25,14,1),(25,14,2),
                (28,11,1),(28,11,2),
                (31,8,1),(31,8,2),
                (34,5,1),(34,5,2),
                (37,2,1),(37,2,2)]
    elif(x==39 and y==0):
        rakes=[(38,1,3),(38,1,4),
                (35,4,3),(35,4,4),
                (32,7,3),(32,7,4),
                (29,10,3),(29,10,4),
                (26,13,3),(26,13,4),
                (23,16,3),(23,16,4),
                (20,19,3),(20,19,4),
                (17,22,3),(17,22,4),
                (14,25,3),(14,25,4),
                (11,28,3),(11,28,4),
                (8,31,3),(8,31,4),
                (5,34,3),(5,34,4),
                (2,37,3),(2,37,4)]
    elif(x==39 and y==39):
        rakes=[(38,38,1),(38,38,4),
                (35,35,1),(35,35,4),
                (32,32,1),(32,32,4),
                (29,29,1),(29,29,4),
                (26,26,1),(26,26,4),
                (23,23,1),(23,23,4),
                (20,20,1),(20,20,4),
                (17,17,1),(17,17,4),
                (14,14,1),(14,14,4),
                (11,11,1),(11,11,4),
                (8,8,1),(8,8,4),
                (5,5,1),(5,5,4),
                (2,2,1),(2,2,4)]
    
    bootMsg = [0]*160
    pirate.setSignal(frombits(bootMsg))

    """ 
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return random.randint(1, 4)
 """
    return moveTo(30,5,pirate)

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
