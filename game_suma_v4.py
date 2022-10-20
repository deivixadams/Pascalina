#Agregando la parte de dectar si el usuario hizo la suma correcta...

import pygame, random, time
pygame.init()

# Texto de los botones
bton1_text = "0000"
bton2_text = "0000"
bton3_text = "0000"

#Variables globales
bton_suma_correcta = 0
NIVEL_SUMA = 1



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
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 400
size = SCREEN_WIDTH, SCREEN_HEIGHT
width, height = size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flash Suma...")


#Definiendo texto y clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
#text = font.render('', True, (255, 0, 0))

# def displaysuma(text):
#     text_render = font.render(text, True, BLACK)
#     screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
#     #pygame.time.wait(500)
#     #x, y, w , h = text_render.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
#     #x, y = position
#     #screen.blit(text_render, (x, y))
#     #return numText


#Aqui controlamos el nivel de dificultad
def endtime():
    message_end_time = pygame.time.get_ticks() + 2000
    return message_end_time


# Suma Aleatoria
def suma_aleatoria():
    aleatorio = random.randint(1, 3)
    a = random.randint(0,5)
    b = random.randint(0,5)
    c = a + b
    suma = (f"{a} + {b}")
    global bton_suma_correcta 


    #Asignando valores a los botones
    global bton1_text 
    global bton2_text 
    global bton3_text 
    print(aleatorio)
    if aleatorio == 1:
        bton1_text = str(c)
        bton2_text = str(random.randint(0,100)+c)
        bton3_text = str(random.randint(0,100)-c)
        bton_suma_correcta = 1
    elif aleatorio == 2:
        bton2_text = str(c)
        bton1_text = str(random.randint(0,100)+c)
        bton3_text = str(random.randint(0,100)-c)
        bton_suma_correcta = 2
    elif aleatorio == 3:
        bton3_text = str(c)
        bton1_text = str(random.randint(0,100)+c)
        bton2_text = str(random.randint(0,100)-c)
        bton_suma_correcta = 3
    
    return suma


def button(screen, position, text):

    #size boton fix
    lentext = len(text)
    if lentext == 1:
        text = "  "+ text +"  "
    elif lentext == 2:
        text = "  "+ text +" "
    elif lentext == 3:
        text = " "+ text +" "
    elif lentext == 4:
        text = " " + text

    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, RED)



    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))
    # return screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
 
# def correcto(v):
#     global aciertos
#     if v == 1:
#        print("Correcto")
#        aciertos+=1
#     else:
#        print("Incorrecto")
        

# def valor_bton1(v):
#     if v == 1:
#         pass
#     if v == 2:
#         pass


 
def main():
   
    #Aciertos control
    aciertos = 0

    # La primera vez numero a desplegar
    numtext = suma_aleatoria()
    text_render = font.render(numtext, True, BLACK)
    message_end_time = endtime() # tiempo de despliegue

    t = True
    
    while t:
        #En cada loop background color is set to yellow
        screen.fill(YELLOW)
        #Control fps no matter how fast the computer is
        #clock.tick(60)
        #reading initial time
        current_time = pygame.time.get_ticks()

        # # Asignando valores a los botones
        # bton1_text = valor_bton1(1)
        # bton2_text = valor_bton1(2)

        b1 = button(screen, (300, 300), "Exit")
        b2 = button(screen, (400, 300), bton1_text)
        b3 = button(screen, (500, 300), bton2_text)
        b4 = button(screen, (600, 300), bton3_text)

        for event in pygame.event.get():
            if (event.type == pygame.quit):
                t = False
                #pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    t = False
                # key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                # if key_to_start:
                #     start()
                
                #-----------------Botones-----------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    t = False
                elif b2.collidepoint(pygame.mouse.get_pos()) and bton_suma_correcta == 1:
                    aciertos += 1
                    print("Correcto")
                elif b3.collidepoint(pygame.mouse.get_pos()) and bton_suma_correcta == 2:
                    aciertos += 1
                    print("Correcto")
                elif b4.collidepoint(pygame.mouse.get_pos()) and bton_suma_correcta == 3:
                    aciertos += 1
                    print("Correcto")



        #Generando números aleatorios
        '''Se debe seleccionar de forma aleatoria la operación básica a realizar'''
       
        #control del texto desplegado
        if current_time < message_end_time:
            screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
        else:
            message_end_time = endtime()
            numtext = suma_aleatoria()
            text_render = font.render(numtext, True, BLACK)
            screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
            # displaysuma(numText)


         
        pygame.display.flip()
    print("Aciertos: ", aciertos)       
    
if __name__ == "__main__":
    main()
    #
    exit()  
