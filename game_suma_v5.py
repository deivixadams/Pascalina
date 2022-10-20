'''
Pendientes:
4. Agregar 4 operaciones básicas
5. Agregar multiples pantallas
6. Agregar un menu de inicio
Como evitar multiples clicks
'''

#Agregando la parte de dectar si el usuario hizo la suma correcta...
#Sonido usando print(\a)
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

#Aqui controlamos el nivel de rapidez con que se despliega la suma
def endtime():
    message_end_time = pygame.time.get_ticks() + 3000
    return message_end_time

# #Aqui controlamos el nivel de rapidez con que se despliega correcto
# def endcorrecto():
#     correcto_end_time = pygame.time.get_ticks() + 1000
#     return correcto_end_time


#operaciones aleatorias pygame
def operaciones_aleatorias():
    # Suma Aleatoria
    lstoper = ["+","-","*","/"]    
    a = random.randint(1,3) #Aqui controlamos el nivel de dificultad
    b = random.randint(1,3) #Aqui controlamos el nivel de dificultad
    
    tipo_operacion = random.choice(lstoper)

    if tipo_operacion == "+":
        resultado_operacion = a + b 
        text_operacion = (f"{a} + {b}")
    elif tipo_operacion == "-":
        resultado_operacion = a - b 
        text_operacion = (f"{a} - {b}")
    elif tipo_operacion == "*":
        resultado_operacion = a * b 
        text_operacion = (f"{a} * {b}")
    elif tipo_operacion == "/":
        resultado_operacion = a // b 
        text_operacion = (f"{a} / {b}")

    aleatorio = random.randint(1, 3) #Para saber en cual boton se coloca la respuesta correcta

    # c = a + b
    
    global bton_suma_correcta 

    #Asignando valores a los botones
    global bton1_text 
    global bton2_text 
    global bton3_text 
    print(aleatorio)
    if aleatorio == 1:
        bton1_text = str(resultado_operacion)
        bton2_text = str(random.randint(0,100)+resultado_operacion)
        bton3_text = str(random.randint(0,100)+resultado_operacion+1)
        bton_suma_correcta = 1
    elif aleatorio == 2:
        bton2_text = str(resultado_operacion)
        bton1_text = str(random.randint(0,100)+resultado_operacion)
        bton3_text = str(random.randint(0,100)+resultado_operacion+1)
        bton_suma_correcta = 2
    elif aleatorio == 3:
        bton3_text = str(resultado_operacion)
        bton1_text = str(random.randint(0,100)+resultado_operacion)
        bton2_text = str(random.randint(0,100)+resultado_operacion+1)
        bton_suma_correcta = 3
    return text_operacion

# Suma Aleatoria
def suma_aleatoria():
    aleatorio = random.randint(1, 3)
    a = random.randint(0,3) #Aqui controlamos el nivel de dificultad
    b = random.randint(0,3) #Aqui controlamos el nivel de dificultad
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
 
def main():
   
    
    aciertos = 0 #Aciertos control
    txtcorrecto = " "  #control del mensaje correcto/incorrecto
    t = True #bucle maestro
    correcto = 0 #total de aciertos
    
    # La primera vez numero a desplegar
    numtext = operaciones_aleatorias()
    text_render = font.render(numtext, True, BLACK)
    message_end_time = endtime() # tiempo de despliegue
    # correcto_end_time = endcorrecto() # tiempo de despliegue
   
    
    while t:
        #En cada loop background color is set to yellow
        screen.fill(YELLOW)
        #Control fps no matter how fast the computer is
        #clock.tick(60)
        
        #reading initial time
        current_time = pygame.time.get_ticks()
        # current_time_correcto = pygame.time.get_ticks()

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
                    correcto = 1
                    print("Correcto \a")
                elif b3.collidepoint(pygame.mouse.get_pos()) and bton_suma_correcta == 2:
                    aciertos += 1
                    correcto = 1
                    print("Correcto \a")
                elif b4.collidepoint(pygame.mouse.get_pos()) and bton_suma_correcta == 3:
                    aciertos += 1
                    correcto = 1
                    print("Correcto \a")
                else:
                    correcto = 2
            else:
                correcto = 3
                    
            if correcto == 1:
                txtcorrecto = font.render("Correcto...", True, BLUE) #seteamos el texto correcto
            elif correcto == 2:
                txtcorrecto = font.render("Incorrecto", True, RED) #seteamos el texto incorrecto)       
            else: 
                txtcorrecto = font.render("", True, BLACK)    

        #Generando números aleatorios
        '''Se debe seleccionar de forma aleatoria la operación básica a realizar'''
       
        # #control del texto desplegado correcto o incorrecto
        # if current_time_correcto < correcto_end_time:           
        #     if  correcto:
        #         txtcorrecto = font.render("Correcto...", True, BLACK) #seteamos el texto de la suma
        #         screen.blit(txtcorrecto, (100,100)) #desplegamos el texto de la suma centro pantalla
        #     else:
        #         #correcto_end_time = endcorrecto()
        #         txtcorrecto = font.render("", True, BLACK) #seteamos el texto de la suma
        #         screen.blit(txtcorrecto, (100,100)) #desplegamos el texto de la suma centro pantalla
                
          #control del texto desplegado
        if current_time < message_end_time:
            screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
            screen.blit(txtcorrecto, (100,100))  
            # pygame.time.wait(200)

        else:
            message_end_time = endtime()
            numtext = operaciones_aleatorias()
            text_render = font.render(numtext, True, BLACK)
            screen.blit(text_render, text_render.get_rect(center = screen.get_rect().center))
            # displaysuma(numText)    
            #Borrando texto correcto
            # txtcorrecto = font.render("", True, BLACK)   
            # screen.blit(txtcorrecto, (100,100))  

        pygame.display.flip()
    text_acierto = font.render("Aciertos: " + str(aciertos), True, RED) #seteamos el texto de la suma
    screen.blit(text_acierto, (100,100)) #desplegamos el texto de la suma centro pantalla
    pygame.display.flip()
    print("Aciertos: ", aciertos)       
    pygame.time.wait(300)
if __name__ == "__main__":
    main()
    exit()  