from pygame import*
init()

win=display.set_mode((500,500))
display.set_caption("Hello")

x=50
y=300
w=40
h=60
v=7

jump=False
jumpcount=10

run=True

while run:

    time.delay(50)

    for i in event.get():
       if i.type==QUIT:
            run=False

    k=key.get_pressed()
    if k[K_LEFT] and x>v:
        x-=v
    if k[K_RIGHT] and x<500-w-v:
        x+=v

    if not(jump):
        if k[K_SPACE]:                      
            jump=True
    else:
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y-=(jumpcount**2)*0.5*neg
            jumpcount-=1
        else:
            jump=False
            jumpcount=10


    win.fill((0, 0, 0))

    draw.rect(win,(0,255,0),(x,y,w,h))
    display.update()

QUIT()
