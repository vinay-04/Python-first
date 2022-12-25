import pygame

sw=500
a=500
b=500
fps=60
#char1
#char=
char_v=5
char_x=100
char_y=300
char_w=25
char_h=25
#char2
#char2=
char2_v=5
char2_x=300
char2_y=100
char2_w=25
char2_h=25

pass_through=True

c=pygame.time.Clock()

run=True
pygame.init()

win = pygame.display.set_mode((a, b))
pygame.display.set_caption("hello")

def gameover():
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("GAMEOVER", True, (255, 255, 255), (0,0,0))
    win.blit(text,(150,250))


def chars():
    win.fill((0,0,0))
    g=pygame.draw.rect(win, (0, 0, 255), (char_x, char_y, char_w, char_h))
    h=pygame.draw.rect(win, (255, 0, 255), (char2_x, char2_y, char2_w, char2_h))


while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    c.tick(fps)

    k=pygame.key.get_pressed()
    if k[pygame.K_LEFT] and char_x>char_v :
        char_x-=char_v
    if k[pygame.K_RIGHT]and char_x<sw-char_w-char_v:
        char_x+=char_v
    if k[pygame.K_UP] and char_y>char_v:
        char_y-=char_v
    if k[pygame.K_DOWN] and char_y<sw-char_h-char_v:
        char_y+=char_v

    if k[pygame.K_a] and char2_x>char2_v :
        char2_x-=char2_v
    if k[pygame.K_d]and char2_x<sw-char2_w-char2_v:
        char2_x+=char2_v
    if k[pygame.K_w] and char2_y>char2_v:
        char2_y-=char2_v
    if k[pygame.K_s] and char2_y<sw-char2_h-char2_v:
        char2_y+=char2_v

    if abs(char_y-char2_y)<=24 and abs (char_x-char2_x)<=24:
         pass_through=False

    else:
        chars()


    pygame.display.update()


quit()
