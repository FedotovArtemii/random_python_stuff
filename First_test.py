import pygame, sys, random, math
pygame.init()
width = 500
height = 500
count = 0
inside = 0
pi_approx = 0
mistake = 0
screen=pygame.display.set_mode([width,height])
screen.fill([0,0,0])
pygame.draw.circle(screen, [255,255,255], [int(width / 2), int(height /2)],int(width/2), 1)
pygame.display.flip()
while True:
    point_x = random.randint(0, width)
    point_y = random.randint(0,height)
    d = (point_x - width/2)**2 + (point_y - height/2) **2
    count += 1
    if d > (width/2)** 2:
        color = [100,0,0]
    else:
        color = [0,100,0]
        inside += 1
    pygame.draw.circle(screen, color, [point_x,point_y],1,0)
    pygame.display.flip()
    pi_approx = 4 * (inside/count)
    square_mistake = float((math.pi - pi_approx)**2)
    print ('we think it is:', pi_approx, 'mistake is: ', square_mistake**0.5)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
