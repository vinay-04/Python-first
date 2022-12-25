from pygame import *
from random import *
init()
win=display.set_mode((500,500))
display.set_caption("Snake")

x=250
y=250
w=25
h=25
v=8
fx=randint(0,400)
fy=randint(0,400)
fps=60
s=0




clock= time.Clock()


run=True
while run:
    clock.tick(fps)
    for e in event.get():
        if e.type == QUIT:
            run=False

    k = key.get_pressed()
    if k[K_LEFT] and x > v:
        x -= v
    if k[K_RIGHT] and x < 500 - w - v:
        x += v
    if k[K_UP] and y > v:
        y -= v
    if k[K_DOWN] and y < 500 - h - v:
        y += v


    if abs(fx-x)<=12 and abs(fy-y)<=12:
        s+=1
        print("score:",s)
        fx = randint(0,400)
        fy = randint(0,400 )
        x+=10


    win.fill((255, 255, 255))
    draw.rect(win, (255, 0, 0), (fx, fy, 10, 10))
    draw.rect(win,(0,0,0),(x,y,w,h))
    display.update()


try:
    QUIT()
except:
    print()

