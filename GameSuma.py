from random import random
from random import randint
import pygame
from pygame.locals import *  #para cntrl de teclas
from threading import Thread

NIVEL_SUMA = 1

import time

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False
        self.image = font.render(self.text, 1, (0,0,0))

    def draw(self,window,outline=None):
                #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-4,self.width+4,self.height+8),0)
                    
        pygame.draw.rect(window, self.color, (self.x,self.y-2,self.width,self.height+4),0)
                
        if self.text != '':
            w, h = self.image.get_size()
            window.blit(self.image, (self.x + (self.width//2 - w//2), self.y + (self.height//2 - h//2 + 2)))

    def isOver(self, pos):
                #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                    
        return False

"""     def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):            
            if not self.over:
                beepsound.play()
                self.over = True
        else:
            self.over = False """

def generateRandomNumber():
    '''Se debe seleccionar de forma aleatoria la operación básica a realizar'''
    a = randint(0,5)
    b = randint(0,5)
    c = a + b
    numText = (f"{a} + {b} = ")
    return numText

def drawnumber(numText):
    print(numText)
    img2 = font2.render(numText, True, RED)
    screen.blit(img2, (30, 120))
    pygame.display.update()
    time.sleep(NIVEL_SUMA)
    

def dropnumber():
    screen.fill(YELLOW)
    pygame.display.update()



if __name__ == "__main__":
    #Colores
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)

    #Definiendo mi pantalla
    size = 640, 320
    width, height = size
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flash Suma...")
    screen.fill(YELLOW)

    #Iniciando Pygame
    pygame.init()

    #Font pygame
    font2 = pygame.font.SysFont('didot.ttc', 100)
    

    # the main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        n = generateRandomNumber()
        t1 = Thread(target=drawnumber(n))
        t1.start()
        #drawnumber(n)
        #pygame.display.update()
        #time.sleep(2)
        dropnumber()
        #pygame.display.update()

    pygame.quit()