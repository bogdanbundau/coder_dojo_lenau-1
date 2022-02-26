import random as r
import pygame as p
import math as m
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
p.init()

window = p.display.set_mode([500, 500])
running = True
scor = 0
x_rosu = r.randint(0, 500)
y_rosu = r.randint(0, 500)
x = 250
y = 250
rad = 20
w=False
a=False
s=False
d=False
mancare_spawned = False
cords_list_m = []
colors = [[191, 0, 230], [35, 0, 150], [3, 173, 32], [235, 150, 5], [193, 227, 2]]
mancare_rad = [3, 4, 5]
def mancare(cate):
    global mancare_x
    global mancare_y
    for i in range(cate):
            mancare_x = r.randint(0, 500)
            mancare_y = r.randint(0, 500)
            cords_list_m.append([mancare_x, mancare_y, r.choice(colors), r.choice(mancare_rad)])

mancare(40)
while running:
    coordMouseX,coordMouseY = p.mouse.get_pos()
    print(coordMouseX, coordMouseY)
    vecDirectieX = coordMouseX - x
    vecDirectieY = coordMouseY - y
    events = p.event.get()
    for event in events:
        if event.type == p.KEYDOWN:
            if event.key == K_UP:
                w=True
                
            
        if event.type == p.KEYDOWN:
            if event.key == K_DOWN:
                s=True
                
        
            if event.key == K_LEFT:
                a=True
                
        
            if event.key == K_RIGHT:
                d=True
                
        if event.type == p.QUIT:
            running = False

        if event.type == p.KEYUP:
            if event.key == K_UP:
                w=False
                
            
        
            if event.key == K_DOWN:
                s=False
                

        
            if event.key == K_LEFT:
                
                a=False
       
            if event.key == K_RIGHT:
                
                d=False

    if w:
        y-=0.1
    elif s:
        y+=0.1
    elif a:
        x-=0.1
    elif d:
        x+=0.1

    if coordMouseY > y:
        y=y+0.1
    else:
        y=y-0.1
    if coordMouseX > x:
        x=x+0.1
    else:
        x=x-0.1


    if (x_rosu - x)**2 + (y_rosu - y)**2 < rad**2:
        print("Merge")
        rad+=5
        scor+=1
        x_rosu = r.randint(0, 500)
        y_rosu = r.randint(0, 500)

    for i in range(len(cords_list_m)):


        if (cords_list_m[i][0] - x)**2 + (cords_list_m[i][1] - y)**2 < rad**2:
            cords_list_m[i][0] = r.randint(0, 500)
            cords_list_m[i][1] = r.randint(0, 500)
            print("Merge")
            rad+=1
            scor+=1



        p.draw.circle(window,cords_list_m[i][2], (cords_list_m[i][0],cords_list_m[i][1]),cords_list_m[i][3])
    p.draw.circle(window,(255, 0, 0), (x_rosu, y_rosu), 15 )
    p.draw.circle(window, (0, 201, 167), (x, y), rad)
    
    p.display.update()
    
    p.display.flip()
    window.fill((196, 252, 239))
p.quit()
print("Scorul tau este " + str(scor))
