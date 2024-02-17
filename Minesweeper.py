import pygame,pygame.gfxdraw
import math,random

pygame.init()

def draw(s,x,y,l,g,c,m,f,condition,w,h,flagcount,eltime,f2):
    for i in range(x):
        for k in range(y):
            if m[i][k]==-1:
                pygame.draw.rect(s,c[0],(g+k*(l+g),g+i*(l+g),l,l))
            elif m[i][k]==0:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
            elif m[i][k]==1:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("1",True,c[2]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==2:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("2",True,c[3]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==3:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("3",True,c[4]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==4:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("4",True,c[5]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==5:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("5",True,c[6]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==6:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("6",True,c[7]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==7:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("7",True,c[8]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==8:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                s.blit(f.render("8",True,c[9]),(g+k*(l+g)+l/3,g+i*(l+g)))
            elif m[i][k]==9:
                pygame.draw.rect(s,c[0],(g+k*(l+g),g+i*(l+g),l,l))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l/3,g+i*(l+g)+l/2+l/4,2*l/3,l/6))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l/4,g+i*(l+g)+l/2+l/4-l/7+2,l/2,l/7))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2+l//17,math.ceil(g+i*(l+g)+l/2-0.42*l),l//8,0.6*l))
                pygame.gfxdraw.filled_trigon(s,int(g+k*(l+g)+l/2+l//17+1),int(g+i*(l+g)+l/2-0.4*l),int(g+k*(l+g)+l/2+l//17+1),int(g+i*(l+g)+l/2-0.05*l),int(g+k*(l+g)+l/2-l/3),int(g+i*(l+g)+l/2-0.22*l),(230,10,30))
                pygame.gfxdraw.aatrigon(s,int(g+k*(l+g)+l/2+l//17+1),int(g+i*(l+g)+l/2-0.4*l),int(g+k*(l+g)+l/2+l//17+1),int(g+i*(l+g)+l/2-0.05*l),int(g+k*(l+g)+l/2-l/3),int(g+i*(l+g)+l/2-0.22*l),(230,10,30))
            elif m[i][k]==10 and condition:
                pygame.draw.rect(s,c[10],(g+k*(l+g),g+i*(l+g),l,l))
                pygame.gfxdraw.filled_circle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.gfxdraw.aacircle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2-0.42*l),l//6,0.42*l))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2),l//6,0.42*l))
            elif m[i][k]==10 and not condition:
                pygame.draw.rect(s,c[0],(g+k*(l+g),g+i*(l+g),l,l))
            elif m[i][k]==11 and condition:
                pygame.draw.rect(s,c[1],(g+k*(l+g),g+i*(l+g),l,l))
                pygame.gfxdraw.filled_circle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.gfxdraw.aacircle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2-0.42*l),l//6,0.42*l))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2),l//6,0.42*l))
            elif m[i][k]==11 and not condition:
                pygame.draw.rect(s,c[0],(g+k*(l+g),g+i*(l+g),l,l))
            elif m[i][k]==12 and condition:
                pygame.draw.rect(s,c[11],(g+k*(l+g),g+i*(l+g),l,l))
                pygame.gfxdraw.filled_circle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.gfxdraw.aacircle(s,int(g+k*(l+g)+l/2),int(g+i*(l+g)+l/2),int(8*l/25),(0,0,0))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2-0.42*l),l//6,0.42*l))
                pygame.draw.rect(s,(0,0,0),(g+k*(l+g)+l/2-l//12,math.ceil(g+i*(l+g)+l/2),l//6,0.42*l))
    pygame.draw.rect(s,(100,100,100),(g,h,int(w-2*g),int(0.15*h-g)))
    pygame.draw.rect(s,(0,0,0),(w*0.3-l/3,h*1.075+l/4,2*l/3,l/6))
    pygame.draw.rect(s,(0,0,0),(w*0.3-l/4,h*1.075+l/4-l/7+2,l/2,l/7))
    pygame.draw.rect(s,(0,0,0),(w*0.3+l//17,math.ceil(h*1.075-0.42*l),l//8,0.6*l))
    pygame.gfxdraw.filled_trigon(s,int(w*0.3+l//17+1),int(h*1.075-0.4*l),int(w*0.3+l//17+1),int(h*1.075-0.05*l),int(w*0.3-l/3),int(h*1.075-0.22*l),(230,10,30))
    pygame.gfxdraw.filled_trigon(s,int(w*0.3+l//17+1),int(h*1.075-0.4*l),int(w*0.3+l//17+1),int(h*1.075-0.05*l),int(w*0.3-l/3),int(h*1.075-0.22*l),(230,10,30))
    colon=f2.render(":",True,(40,40,40))
    elpsedtimetext=f2.render("Elapsed Time",True,(40,40,40))
    s.blit(colon,(int(w*0.33),int(h*1.075-elpsedtimetext.get_height()/2)))
    s.blit(f2.render(str(flagcount),True,(40,40,40)),(int(w*0.35),int(h*1.075-elpsedtimetext.get_height()/2)))
    s.blit(colon,(int(w*0.461+elpsedtimetext.get_width()),int(h*1.075-elpsedtimetext.get_height()/2)))
    s.blit(elpsedtimetext,(int(w*0.45),int(h*1.075-elpsedtimetext.get_height()/2)))
    s.blit(f2.render(str(eltime),True,(40,40,40)),(int(w*0.481+elpsedtimetext.get_width()),int(h*1.075-elpsedtimetext.get_height()/2)))
    
def mouseposdetection(l,g,x,y,w,h):
    if g<=x<=w-g and g<=y<=h-g:
        ind=[]
        if (x-g)/(l+g)-math.floor((x-g)/(l+g))<=l/(l+g):
            ind.append((x-g)//(l+g))
        else:
            ind.append(-1)
        if (y-g)/(l+g)-math.floor((y-g)/(l+g))<=l/(l+g):
            ind.append((y-g)//(l+g))
        else:
            ind.append(-1)
    else:
        ind=[-1,-1]
    return ind

def countneighbormines(ind,m,r,c):
    count=0
    steps=[[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]
    for i in steps:
        if 0<=ind[1]+i[1]<r and 0<=ind[0]+i[0]<c:
            if m[ind[1]+i[1]][ind[0]+i[0]]:
                count+=1
    return count

def givepossibledirections(ind,r,c):
    if 0<ind[0]<c-1 and 0<ind[1]<r-1:
        return [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    elif ind[0]==0 and 0<ind[1]<r-1:
        return [[1,0],[0,1],[0,-1],[1,1],[1,-1]]
    elif ind[0]==0 and ind[1]==0:
        return [[1,0],[0,1],[1,1]]
    elif 0<ind[0]<c-1 and ind[1]==0:
        return [[1,0],[-1,0],[0,1],[1,1],[-1,1]]
    elif ind[0]==c-1 and ind[1]==0:
        return [[-1,0],[0,1],[-1,1]]
    elif ind[0]==c-1 and 0<ind[1]<r-1:
        return [[-1,0],[0,1],[0,-1],[-1,1],[-1,-1]]
    elif 0<ind[0]<c-1 and ind[1]==r-1:
        return [[1,0],[-1,0],[0,-1],[1,-1],[-1,-1]]
    elif ind[0]==c-1 and ind[1]==r-1:
        return [[-1,0],[0,-1],[-1,-1]]
    elif ind[0]==0 and ind[1]==r-1:
        return [[1,0],[0,-1],[1,-1]]

def openemptyboxes(ind,directions,controlledindices,m,r,c,mtrx,removedflag):
    controlledindices.append(ind)
    for i in directions:
        neighborindex=[ind[0]+i[0],ind[1]+i[1]]
        if neighborindex not in controlledindices and (mtrx[neighborindex[1]][neighborindex[0]]==-1 or mtrx[neighborindex[1]][neighborindex[0]]==9):
            z=countneighbormines(neighborindex,m,r,c)
            if mtrx[neighborindex[1]][neighborindex[0]]==9:
                removedflag+=1
            mtrx[neighborindex[1]][neighborindex[0]]=z
            if z==0:
                newdirection=givepossibledirections(neighborindex,r,c)
                if [-i[0],-i[1]] in newdirection:
                    newdirection.remove([-i[0],-i[1]])
                mtrx,removedflag,controlledindices=openemptyboxes(neighborindex,newdirection,controlledindices,m,r,c,mtrx,removedflag)
            else:
                controlledindices.append(neighborindex)
    return mtrx,removedflag,controlledindices

def placemines(n,r,c,ind,m):
    mapmatrix=m
    minematrix=[[0]*c for _ in range(r)]
    allpossibleindices=[]
    emptyareapos=[[ind[1],ind[0]],[ind[1]-1,ind[0]],[ind[1]+1,ind[0]],[ind[1],ind[0]-1],[ind[1],ind[0]+1],[ind[1]+1,ind[0]+1],[ind[1]+1,ind[0]-1],[ind[1]-1,ind[0]+1],[ind[1]-1,ind[0]-1],[ind[1]-2,ind[0]],[ind[1]+2,ind[0]],[ind[1]-2,ind[0]+1],[ind[1]-2,ind[0]-1],[ind[1]+2,ind[0]+1],[ind[1]+2,ind[0]-1],[ind[1],ind[0]+2],[ind[1],ind[0]-2],[ind[1]+1,ind[0]+2],[ind[1]-1,ind[0]+2],[ind[1]+1,ind[0]-2],[ind[1]-1,ind[0]-2]]
    for i in range(r):
        for k in range(c):
            if [i,k] not in emptyareapos:
                allpossibleindices.append([i,k])
    if len(allpossibleindices)>=n:
        allmines=random.sample(allpossibleindices,n)
    else:
        allmines=allpossibleindices
    for j in allmines:
        if mapmatrix[j[0]][j[1]]==-1:
            mapmatrix[j[0]][j[1]]=11
        minematrix[j[0]][j[1]]=1
    mapmatrix[ind[1]][ind[0]]=countneighbormines(ind,minematrix,r,c)
    return mapmatrix,minematrix,len(allmines)

def checkwin(mtrx,minemtrx,minenum):
    count=0
    for i,j in zip(mtrx,minemtrx):
        for k,l in zip(i,j):
            if k==9 and l==1:
                count+=1
            if k==-1:
                return False
    if count==minenum:
        return True
    return False

rowboxno=12
columnboxno=18
lengthofbox=35 # pixels
gaplength=3 # pixels

width=int((lengthofbox+gaplength)*columnboxno+gaplength)
height=int(((lengthofbox+gaplength)*rowboxno+gaplength))

screen=pygame.display.set_mode((width,int(height*1.15)))
pygame.display.set_caption("Minesweeper")
pygame.mouse.set_cursor(pygame.cursors.tri_left)

colors=[(220,220,220),(172,172,172),(0,1,247),(1,126,2),(251,2,0),(0,1,128),(126,3,1),(2,128,124),(0,0,0),(128,128,128),(240,10,30),(10,150,30)]

minesnumber=int(rowboxno*columnboxno*0.175)
flagnumber=minesnumber

matrix=[[-1]*columnboxno for _ in range(rowboxno)]
mines=[[0]*columnboxno for _ in range(rowboxno)]

pygame.font.init()
font1=pygame.font.SysFont("impact",int(20*lengthofbox/25))
font2=pygame.font.SysFont("impact",int(height*0.15*0.4))

gameoverscreen=pygame.Surface((width,height*1.15),pygame.SRCALPHA)
winscreen=pygame.Surface((width,height*1.15),pygame.SRCALPHA)
gameoverscreen.set_alpha(210)
winscreen.set_alpha(210)
gameoverscreen.fill((0,0,0))
winscreen.fill((0,0,0))
wingameoverfont=pygame.font.SysFont("impact",int(height*0.15))
click2playfont=pygame.font.SysFont("impact",int(height*0.08))
gameovertext=wingameoverfont.render("Game Over",True,(200,200,200))
wintext=wingameoverfont.render("You Win",True,(200,200,200))
click2playtext=click2playfont.render("-Click to Play Again-",True,(200,200,200))
gameoverscreen.blit(gameovertext,(int(width/2-gameovertext.get_width()/2),int(height/2-gameovertext.get_height()/2)))
gameoverscreen.blit(click2playtext,(int(width/2-click2playtext.get_width()/2),int(height/2-click2playtext.get_height()/2+height/5)))
winscreen.blit(wintext,(int(width/2-wintext.get_width()/2),int(height/2-wintext.get_height()/2)))
winscreen.blit(click2playtext,(int(width/2-click2playtext.get_width()/2),int(height/2-click2playtext.get_height()/2+height/5)))

isclickingovermine=False
initialclick=True
win=False
change=True
run=True

elapsedtime=0
    
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                run=False
            elif event.key==pygame.K_r and (win or isclickingovermine):
                matrix=[[-1]*columnboxno for _ in range(rowboxno)]
                mines=[[0]*columnboxno for _ in range(rowboxno)]
                minesnumber=int(rowboxno*columnboxno*0.175)
                flagnumber=minesnumber
                isclickingovermine=False
                initialclick=True
                win=False
                change=True
                elapsedtime=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and not isclickingovermine and not initialclick and not win:
                mousepos=pygame.mouse.get_pos()
                index=mouseposdetection(lengthofbox,gaplength,mousepos[0],mousepos[1],width,height)
                if index[0]!=-1 and index[1]!=-1:
                    if matrix[index[1]][index[0]]==11:
                        matrix[index[1]][index[0]]=10
                        isclickingovermine=True
                        for i in range(rowboxno):
                            for k in range(columnboxno):
                                if matrix[i][k]==9 and mines[i][k]==1:
                                    matrix[i][k]=12
                    elif matrix[index[1]][index[0]]==-1:
                        z=countneighbormines(index,mines,rowboxno,columnboxno)
                        matrix[index[1]][index[0]]=z
                        if z==0:
                            matrix,removedflagnumber,_=openemptyboxes(index,givepossibledirections(index,rowboxno,columnboxno),[],mines,rowboxno,columnboxno,matrix,0)
                            flagnumber+=removedflagnumber
                    if flagnumber==0:
                        win=checkwin(matrix,mines,minesnumber)
            elif (pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]) and (isclickingovermine or win):
                matrix=[[-1]*columnboxno for _ in range(rowboxno)]
                mines=[[0]*columnboxno for _ in range(rowboxno)]
                minesnumber=int(rowboxno*columnboxno*0.175)
                flagnumber=minesnumber
                isclickingovermine=False
                initialclick=True
                win=False
                change=True
                elapsedtime=0
            elif pygame.mouse.get_pressed()[0] and not isclickingovermine and initialclick:
                mousepos=pygame.mouse.get_pos()
                index=mouseposdetection(lengthofbox,gaplength,mousepos[0],mousepos[1],width,height)
                if index[0]!=-1 and index[1]!=-1:
                    if matrix[index[1]][index[0]]==-1:
                        difference=minesnumber-flagnumber
                        matrix,mines,minesnumber=placemines(minesnumber,rowboxno,columnboxno,index,matrix)
                        flagnumber=minesnumber-difference
                        matrix,removedflagnumber,_=openemptyboxes(index,givepossibledirections(index,rowboxno,columnboxno),[],mines,rowboxno,columnboxno,matrix,0)
                        flagnumber+=removedflagnumber
                        if flagnumber<0:
                            flagnumber=0
                        win=checkwin(matrix,mines,minesnumber)
                        initialclick=False
                        t0=pygame.time.get_ticks()
            elif pygame.mouse.get_pressed()[2] and not isclickingovermine and not win:
                mousepos=pygame.mouse.get_pos()
                index=mouseposdetection(lengthofbox,gaplength,mousepos[0],mousepos[1],width,height)
                if index[0]!=-1 and index[1]!=-1:
                    if (matrix[index[1]][index[0]]==-1 or matrix[index[1]][index[0]]==11) and flagnumber>0:
                        matrix[index[1]][index[0]]=9
                        flagnumber-=1
                        if flagnumber==0:
                            win=checkwin(matrix,mines,minesnumber)
                        change=True
                    elif matrix[index[1]][index[0]]==9 and mines[index[1]][index[0]]==0:
                        matrix[index[1]][index[0]]=-1
                        flagnumber+=1
                        change=True
                    elif matrix[index[1]][index[0]]==9 and mines[index[1]][index[0]]==1:
                        matrix[index[1]][index[0]]=11
                        flagnumber+=1
                        change=True
    if change:
        screen.fill((128,128,128))   
        draw(screen,rowboxno,columnboxno,lengthofbox,gaplength,colors,matrix,font1,isclickingovermine,width,height,flagnumber,elapsedtime,font2)
        if isclickingovermine:
            screen.blit(gameoverscreen,(0,0))
        elif win:
            screen.blit(winscreen,(0,0))
        pygame.display.update()
        change=False
    if not isclickingovermine and not win and not initialclick:
        elapsedtime=int((pygame.time.get_ticks()-t0)/1000)
        change=True
   
pygame.quit()
