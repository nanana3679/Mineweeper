import random


class cell:
    def __init__(self,contents,visible,flag):
        self.contents=contents
        self.visible=visible
        self.flag=flag

def set_mine(mine_num):
    for i in range(mine_num):
        if board[random.randint(0,n-1)][random.randint(0,n-1)].contents=='x':
            set_mine(0)
        else:
            board[random.randint(0,n-1)][random.randint(0,n-1)].contents='x'

def print_board():
    for i in range(n):
        for j in range(n):
            if board[i][j].visible==True:
                if cursor==[i,j]:
                    if board[i][j].flag==True:
                        print('>F',end='')
                    else:
                        print('>{}'.format(board[i][j].contents),end='')
                else:
                    if board[i][j].flag==True:
                        print(' F',end='')
                    else:
                        print(' {}'.format(board[i][j].contents),end='')

            else:
                if cursor==[i,j]:
                    if board[i][j].flag==True:
                        print('>F',end='')
                    else:
                        print('>█'.format(board[i][j].contents),end='')
                else:
                    if board[i][j].flag==True:
                        print(' F',end='')
                    else:
                        print('■'.format(board[i][j].contents),end='')
        print()


#시야,커서,깃발
#1,1,1 >f
#1,1,0 >{}               
#1,0,1 ⚑
#1,0,0 {:2}
#0,1,1 >f
#0,1,0 >█       
#0,0,1 ⚑
#0,0,0 ■

def act(act):

    if act=='4':
        if cursor[1]!=0:
            cursor[1]-=1
    if act=='8':
        if cursor[0]!=0:
            cursor[0]-=1
    if act=='2':
        if cursor[0]!=n-1:
            cursor[0]+=1
    if act=='6':
        if cursor[1]!=n-1:
            cursor[1]+=1

    if act=='5':
        if board[cursor[0]][cursor[1]].contents==' ': #빈칸일때
            board[cursor[0]][cursor[1]].visible=True
            expent(cursor[0],cursor[1])
        elif board[cursor[0]][cursor[1]].contents=='x': #지뢰일때
            for i in range(n):
                for j in range(n):
                    board[i][j].visible:True
            lose=True
        else:
            board[cursor[0]][cursor[1]].visible=True #숫자일때
            
    if act=='7':
        if board[cursor[0]][cursor[1]].flag==True:
            board[cursor[0]][cursor[1]].flag=False
        else:
            board[cursor[0]][cursor[1]].flag=True

    if act=='new':
        stat_newgame()
    
        
def expent(x,y):
        if x==0:
            if y==0:#7
                board[x][y+1].visible=True
                board[x+1][y].visible=True
                board[x+1][y+1].visible=True
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
            elif y==n-1:#9
                board[x][y-1].visible=True
                board[x+1][y-1].visible=True
                board[x+1][y].visible=True
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
            else:#8
                board[x][y-1].visible=True
                board[x][y+1].visible=True
                board[x+1][y-1].visible=True
                board[x+1][y].visible=True
                board[x+1][y+1].visible=True
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
        elif x==n-1:
            if y==0:#1
                board[x-1][y].visible=True
                board[x-1][y+1].visible=True
                board[x][y+1].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
            elif y==n-1:#3
                board[x-1][y-1].visible=True
                board[x-1][y].visible=True
                board[x][y-1].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
            else:#2
                board[x-1][y-1].visible=True
                board[x-1][y].visible=True
                board[x-1][y+1].visible=True
                board[x][y-1].visible=True
                board[x][y+1].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
        else:
            if y==0:#4
                board[x-1][y].visible=True
                board[x-1][y+1].visible=True
                board[x][y+1].visible=True
                board[x+1][y].visible=True
                board[x+1][y+1].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
            elif y==n-1:#6
                board[x-1][y-1].visible=True
                board[x-1][y].visible=True
                board[x][y-1].visible=True
                board[x+1][y-1].visible=True
                board[x+1][y].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
            else:#5
                board[x-1][y-1].visible=True
                board[x-1][y].visible=True
                board[x-1][y+1].visible=True
                board[x][y-1].visible=True
                board[x][y+1].visible=True
                board[x+1][y-1].visible=True
                board[x+1][y].visible=True
                board[x+1][y+1].visible=True
                #if board[x-1][y].contents==0:
                #    expent(x-1,y)
                #if board[x][y-1].contents==0:
                #    expent(x,y-1)
                #if board[x][y+1].contents==0:
                #    expent(x,y+1)
                #if board[x+1][y].contents==0:
                #    expent(x+1,y)
                
def set_hint():    
    for i in range(n):
        for j in range(n):
            if not board[i][j].contents=='x':
                if i!=0 and j!=0:
                    if board[i-1][j-1].contents=='x':
                        board[i][j].contents+=1
                if i!=0:
                    if board[i-1][j].contents=='x':
                        board[i][j].contents+=1
                if i!=0 and j!=n-1:
                    if board[i-1][j+1].contents=='x':
                        board[i][j].contents+=1
                if j!=0:
                    if board[i][j-1].contents=='x':
                        board[i][j].contents+=1
                if j!=n-1:
                    if board[i][j+1].contents=='x':
                        board[i][j].contents+=1
                if i!=n-1 and j!=0:
                    if board[i+1][j-1].contents=='x':
                        board[i][j].contents+=1
                if i!=n-1:
                    if board[i+1][j].contents=='x':
                        board[i][j].contents+=1
                if i!=n-1 and j!=n-1:
                    if board[i+1][j+1].contents=='x':
                        board[i][j].contents+=1
    for i in range(n):
        for j in range(n):
            if board[i][j].contents==0:
                board[i][j].contents=' '

def start_newgame():
    set_mine(mine_num)
    set_hint()
    for i in range(n):
        for j in range(n):
            board[i][j].visible:False
    cursor=[n//2,n//2]
    print('NEW GAME')

def judge_win():
    win_count=0
    for i in range(n):
        for j in range(n):
            if board[i][j].contents=='x' and board[i][j].flag==True:
                win_count+=1
    if win_count==mine_num:
        win=True
        
n=9

mine_num=10

board=[ [cell(0,True,False) for col in range(n)] for row in range(n) ]
cursor=[n//2,n//2]
program=1
win=False
lose=False


while program==1:
    
        start_newgame()
        
        while win==False and lose==False:
            print_board()
            act(input())
            judge_win()
            
        if win==True:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')
                
