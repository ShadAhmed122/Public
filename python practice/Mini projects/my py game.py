import pygame,random
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
gWindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("White Snake")
pygame.display.update()

sx=450
sy=300
fps=60
exitgame=False
Gameover=False
score=0


clock=pygame.time.Clock()

xspeed=0
yspeed=0
spd=1.5

fdx=random.randint(20,880)
fdy=random.randint(20,580)
def fun1():
    global fdx,fdy
    fdx = random.randint(20, 880)
    fdy = random.randint(20, 580)
    

while not exitgame:
    for i in pygame.event.get():
        print(i)
        if i.type == pygame.QUIT:
            exitgame=True

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                xspeed = spd
                yspeed = 0
            if i.key == pygame.K_LEFT:
                xspeed = -spd
                yspeed = 0
            if i.key == pygame.K_UP:
                xspeed = 0
                yspeed = -spd
            if i.key == pygame.K_DOWN:
                xspeed = 0
                yspeed = spd
    if abs(sx-fdx)<10 and abs(sy-fdy)<10:
        fun1()
    sx+=xspeed
    sy+=yspeed
    gWindow.fill(white)
    gWindow.blit(pygame.font.SysFont(None,55).render("Score: "+ str(score),True,black),5,5)
    pygame.draw.rect(gWindow, red, (fdx, fdy, 10, 10))
    pygame.draw.rect(gWindow,green,(sx,sy,10,10))
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
