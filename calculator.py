import pygame as pg
import math

class Main():
    def __init__(self, n1, n2, i1):
        pg.init()
        RES = WIDTH, HEIGHT = 1600, 900
        screen = pg.display.set_mode(RES)
        clock = pg.time.Clock()
        pg.display.set_caption('Refraction Ray Simulator')
        FPS = 60
        
        center = (WIDTH//2, HEIGHT//2)
        i2 = math.degrees(math.asin(n1*math.sin(math.radians(i1))/n2))
        pos1 = (WIDTH/2-(math.tan(math.radians(i1)))*HEIGHT/2, 0)
        pos2 = (WIDTH/2+(math.tan(math.radians(i1)))*HEIGHT/2, 0)
        pos3 = (WIDTH/2+(math.tan(math.radians(i2)))*HEIGHT/2, HEIGHT)
        
        print('n1 : ', n1, ' | n2 : ', n2)
        print('i1 : ', i1, ' | i2 : ', i2)
        
        running = True
        while running:
            screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    
            pg.draw.line(screen, (255, 255, 255), (WIDTH, center[1]), (0 ,center[1]), 5)
            for i in range(0, HEIGHT, HEIGHT//20):
                if i//2 == int(i/2):
                    pg.draw.line(screen, (255, 255, 255), (center[0], i), (center[0], i+20), 5)
                    
            pg.draw.line(screen, (0, 255, 0), pos1, center, 5)
            pg.draw.line(screen, (0, 123, 0), pos2, center, 5)
            pg.draw.line(screen, (200, 0, 0), pos3, center, 5)
                
            pg.display.update()
            clock.tick(FPS)
        pg.quit()