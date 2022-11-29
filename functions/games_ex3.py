import pgzrun
from random import randint

HEIGHT= 600
WIDTH=1200

p= Actor('ironman',center=(WIDTH//2,HEIGHT//2))
c=Actor('cookie',(randint(0,WIDTH),randint(0,HEIGHT)))
title="IRON MAN GAME"
score=0

def draw():
    screen.fill('lavender')
    screen.draw.text(title,(10,10),center=(WIDTH//2,30),fontsize=30, color='blue',
            align = 'center',shadow=(.1,2),scolor='black')
    screen.draw.text(f'score:{score}',(10,10),fontsize=60,
        color='black')
    p.draw()
    c.draw()

def p_move():
    if keyboard.right and p.right< WIDTH :
        p.x+=10
        p.angle=-25
    if keyboard.left and p.left>0:
        p.x-=10
        p.angle=25
    if keyboard.up and p.top>0:
        p.y-=10
    if keyboard.down and p.bottom< HEIGHT:
        p.y+=15
    

def update():
    global score #tells python,that we want to change the value of the global variable score
    p_move()#function call
    if p.colliderect(c):
        score+=1
        c.pos=(randint(0,WIDTH),randint(0,HEIGHT))
        sounds.s1.play()
        #to add music - music.play('file name')
    
    print(p.x,p.y,p.angle)

pgzrun.go()