import pygame as pg
import sys

pg.init()
WIDTH, HEIGHT = 800,800
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
box = pg.Rect(50,50, 200,75)
text = ''
active = False
font = pg.font.Font(None, size=14)

class InputBox(pg.Rect):
    pass



def check_position(position, box):
    if box.collidepoint(position):
        return True
    else: 
        return False


while running:
    screen.fill((100,100,100))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running= False
            pg.quit()
            sys.exit()
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_position(event.pos, box):
                active = True
            else:
                active= False

        if event.type == pg.KEYDOWN:
            if active:
                if event.key == pg.K_RETURN:
                    print(text)
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

            
    pg.draw.rect(screen, color= (255,255,255), rect=box)
    
    text_render = font.render(text, True, (0,0,0))
    screen.blit(text_render, (box.x+20, box.y+4))
    pg.display.flip()


        
