import pgzrun

HEIGHT= 600
WIDTH=1200

p= Actor('ironman',center=(WIDTH//2,HEIGHT//2))

title="IRON MAN GAME"

def draw():
    screen.fill('lavender')
    screen.draw.text(title,(10,10),center=(WIDTH//2,30),fontsize=30, color='blue',
            align = 'center',shadow=(.1,2),scolor='black')
    p.draw()

def p_move():
    if keyboard.right and p.right< WIDTH :
        p.x+=3
    if keyboard.left and p.left>0:
        p.x-=3
    if keyboard.up and p.top>0:
        p.y-=3
    if keyboard.down and p.bottom< HEIGHT:
        p.y+=3
    

def update():
    p_move()#function call
    
    print(p.x,p.y)

pgzrun.go()