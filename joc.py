import random as r
import pygame as p
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
while running:
    events = p.event.get()
    for event in events:
        if event.type == p.KEYDOWN:
            if event.key == K_UP:
                y-=10;
        if event.type == p.KEYDOWN:
            if event.key == K_DOWN:
                y+=10;
        if event.type == p.KEYDOWN:
            if event.key == K_LEFT:
                x-=10;
        if event.type == p.KEYDOWN:
            if event.key == K_RIGHT:
                x+=10;
        if event.type == p.QUIT:
            running = False
    if (x_rosu - x)**2 + (y_rosu - y)**2 < 30*30:
        print("Merge")
    
    p.draw.circle(window,(255, 0, 0), (x_rosu, y_rosu), 15)
    p.draw.circle(window, (0, 0, 255), (x, y), 20)
    
    p.display.update()
    
    p.display.flip()
    window.fill((50, 100, 42))
p.quit()