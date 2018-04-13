import pdb
pdb.set_trace()
m=[["","",""],["","",""],["","",""]]
def checkandplace(m,a,b,x):
    if m[a][b]=="x" or m[a][b]=="o":
        return 2
    else:
        m[a][b]=x

def printboard(m):
    for i in m:
        print(i)


def checkwin(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m==[0][0]==m[1][0]==m[2][0]==x or m[0][1]==m[1][1]==m[2][1]==x or m[0][2]==m[1][2]==m[2][2]==x or m[0][0]==m[1][1]==m[2][2] ==x or m[0][2]==m[1][1]==m[2][0]==x:
        return 3
def blank(m,a,b,x):
    if m[0][0]=="" or m[0][1]=="" or m[0][2]=="" or m[1][0]==""or m[1][1]=="" or m[1][2]=="" or m[2][0]=="" or m[2][1]==""or m[2][2]=="":
        return 0
while True:
    printboard(m)
    print("player A turn")
    a=int(input("x="))
    b=int(input("y="))
    w=checkandplace(m,a,b,"x")
    if w==2:
        print("overlap not allowed")
    t=checkwin(m,a,b,"x")
    if t==3:
        print("player A wins")
        break
    o=blank(m,a,b,"x")
    if o==0:
        print("space available")
        continue
    printboard(m)
    while True:
        printboard(m)
        print("player B turn")
        a=int(input("x="))
        b=int(input("y="))
        w=checkandplace(m,a,b,"o")
        if w==2:
            print("overlap not allowed")
        t=checkwin(m,a,b,"o")
        if t==3:
            print("player B wins")
            break
        o=blank(m,a,b,"o")
        if o==0:
            print("space available")
            continue
        printboard(m)
       
        

    
