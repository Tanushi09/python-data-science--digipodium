import pgzrun

WIDTH = 1200     #use ls instead of dir
HEIGHT = 600

scr=0

def gamescr(title,bgcolor='gray',info="PLAY THE GAME"):
        screen.fill(bgcolor)
        screen.draw.text(title,center=(WIDTH/2,HEIGHT/2),fontsize=100,color='white',align='center')
        screen.draw.text(info,center=(WIDTH/2,HEIGHT/2+100),fontsize=50,color='white',align='center')
        
def draw():
    if scr==0:
        gamescr('amazing game','black','press space to start')
    elif scr==1:
        gamescr(bgcolor='lavender',title='game is running')
    elif scr==2:
        gamescr('game over',info='go home')

def update():
    global scr
    if keyboard.SPACE and scr==0:
        scr=1
    if keyboard.ESCAPE and scr==1:
        scr=2
    if keyboard.RETURN and scr==2:
        scr=0
    print(scr)



    
pgzrun.go()