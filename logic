import random
def startgame():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat


def add_2(mat):
    c=random.randint(0,3)
    d=random.randint(0,3)
    while mat[c][d]!=0:
        c=random.randint(0,3)
        d=random.randint(0,3)
    mat[c][d]=2
    return mat


def compress(mat):
    temp=[]
    changed=False
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        k=0
        for j in range(4):
            if mat[i][j]!=0:
                temp[i][k]=mat[i][j]
                changed=True
                k+=1
    return temp,changed



def merge(temp):
    changed=False
    for i in range(4):
        for j in range(3):
            if temp[i][j]==temp[i][j+1] and temp[i][j]!=0:
                temp[i][j]=temp[i][j+1]*2
                temp[i][j+1]=0
                changed==True
    return temp,changed


def reverse(mat):
    temp=[]
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        for j in range(4):
            temp[i][j]=mat[i][-j-1]
    return temp

def transpose(mat):
    temp=[]
    for i in range(4):
        temp.append([0]*4)
    for i in range(4):
        for j in range(4):
            temp[i][j]=mat[j][i]
    return temp
def move_left(mat):
    comp,changed1=compress(mat)
    merg,changed2=merge(comp)
    changed=changed1 or changed2
    comp=compress(merg)
    return comp,changed

def move_right(mat):
    right=reverse(mat)
    right_shift,changed1=compress(right)
    right_comp,changed2=merge(right_shift)
    changed=changed1 or changed2
    mat=compress(right_comp)
    mat=reverse(mat)
    return mat,changed


def move_up(mat):
    trans=transpose(mat)
    left_shift,changed1=compress(trans)
    left_comp,changed2=merge(left_shift)
    changed=changed1 or changed2
    left_shift=compress(left_comp)
    mat=transpose(left_shift)
    return mat,changed


def move_down(mat):
    trans=transpose(mat)
    rev=reverse(trans)
    movL,changed1=compress(rev)
    com,changed2=merge(movL)
    changed=changed1 or changed2
    movL=compress(com)
    rev=reverse(movL)
    trans=transpose(rev)
    mat=trans
    return mat,changed

def curr_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "YOU WON !!!"
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'MATCH IS GOING ON'
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                return "MATCH IS GOING ON"
    for i in range(4):
        for j in range(3):
            if mat[j][i]==mat[j+1][i]:
                return "MATCH IS GOING ON"
    return "YOU LOST !!!"
















