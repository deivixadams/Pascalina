#importanto modulos de pygame   

#from game_suma_v9 import RED, YELLOW
import pygame, random, time
import sys

class say():
    def __init__(self, t1, t2):
        self.text = t1
        self.text2 = t2

    def imprimir(self):
        print(f"La variable:{self.text} el valor--> {self.text2}")


#Definimos colores
class Color:
    def __init__(self):
        #define colors for game
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.orange = (255, 165, 0)
        self.light_blue = (173, 216, 230)
        self.light_green = (144, 238, 144)
        self.light_red = (255, 182, 193)
        self.light_purple = (224, 102, 255)
        self.light_cyan = (224, 255, 255)
    

#Object screen
class ScreenMain:
    def __init__(self,size, caption, img):
        self.size = size #build a canva size
        self.img = img #asigning image to canvas
        self.caption = caption #asignando titulo a la ventana
        self.screen = pygame.display.set_mode(self.size) #build a screen
        pygame.display.set_caption(self.caption) #Defining a caption
        
        #background image
        self.background = pygame.image.load(self.img)
        self.background = pygame.transform.scale(self.background, (self.size))
        self.screen.blit(self.background,(0,0))

    def get_screen(self):
        return self.screen.get_size() 


#Object Boton
class Button:
    def __init__(self, screen, size, caption="Boton", color=Color().green, text_color=Color().light_red,buttonposs=(0,0)):
        self.screen = screen
        self.size = size 
        self.caption = caption 
        self.color = color 
        self.pos = buttonposs
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", 40)
        self.text_render = self.font.render(self.caption, 1, self.text_color) #rendering text
        self.bton_suma_correcta = 0


    #Defining button
    def drawbutton(self):
        x, y, w , h = self.text_render.get_rect()
        x, y = self.pos
        #Color líneas botón
        pygame.draw.line(self.screen, Color().green, (x, y), (x + w , y), 5)
        pygame.draw.line(self.screen, Color().green, (x, y - 2), (x, y + h), 5)
        pygame.draw.line(self.screen, Color().green, (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(self.screen, Color().green, (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(self.screen, Color().orange, (x, y, w , h)) #Color de fondo botón
        self.screen.blit(self.text_render, (x, y))

    #obtiendo el rect del boton
    def get_rect(self):
        x, y, w , h = self.text_render.get_rect()
        x, y = self.pos
        return pygame.Rect(x, y, w , h)
        #return self.text_render.get_rect()


#Class to display text on screen
class TextScreen:
    def __init__(self, screen,text, size, color, x, y):
        self.screen = screen
        self.textlst = text
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Arial", self.size)

    def display(self):
        for i in self.textlst:
            self.y += 30 #Controlo espacio entre lineas
            text = self.font.render(i, True, Color().white)
            text_rect = text.get_rect(right=self.x, top=self.y)
            #text_rect.right = (480)
            self.screen.blit(text, (text_rect))


#class game 
class Game():
    def __init__(self, nivel):
        # self.screen = screen
        self.repeat = True
        # Texto de los botones
        self.bton1_text = "11111"
        self.bton2_text = "22222"
        self.bton3_text = "33333"
        self.bton4_text = "Reset"
        self.bton5_text = "Nivel"
        self.aciertos = 0 #Aciertos control
        self.txtcorrecto = " "  #control del mensaje correcto/incorrecto
        self.correcto = 0 #total de aciertos
        self.incorrecto = 0 #total de errores
        self.Score = 0 #Puntaje
        self.Tiempo = 0 #Tiempo
        self.nivel = nivel #Nivel
        self.reset = 0 #Reset
        self.textinfo = ("Correcto:","Incorrecto:", "Puntaje:", "Score:", "Tiempo:")
        self.myscreen = ScreenMain((800,500), "Pascalina", "D://DEV//#CODE//GAMES//SUMA//IMG//background2.jpg")   
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.sizebtn = (40,40) #tamaño del boton
        self.posbty = 430 #sube o baja el boton
        self.font = pygame.font.SysFont("Arial", 100)
        self.numtext = " "
        self.message_end_time = pygame.time.get_ticks()
    
    # def set_nivel(self):
    #     self.nivel += 1
    #     self.endtime()
    #     if self.nivel > 3:
    #         self.nivel = 1

    # def get_nivel(self):
    #     return self.nivel

    def endtime(self):
        print("Nivel: ", self.nivel)
        if self.nivel == 1:
            self.message_end_time = pygame.time.get_ticks() + 3000
        elif self.nivel == 2:
            self.message_end_time = pygame.time.get_ticks() + 2000
        elif self.nivel == 3:
            self.message_end_time = pygame.time.get_ticks() + 1000
        elif self.nivel == 4:
            self.message_end_time = pygame.time.get_ticks() + 500
        elif self.nivel == 5:
            self.message_end_time = pygame.time.get_ticks() + 250
        return self.message_end_time

    #-------------------------Operaciones-------------------------
    #operaciones aleatorias pygame
    def operaciones_aleatorias(self):
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

        #Game().bton1_text = "fucking"
        
        return text_operacion, resultado_operacion
    # ------------------------------------------------------------


    def game_loop(self):
        text_render = self.font.render(self.numtext, True, Color().black)

        while self.repeat:
            current_time = pygame.time.get_ticks()
            operacion = Game(self.nivel).operaciones_aleatorias()
            self.numtext = operacion[0] #Genera operaciones aleatorias y botones

            # ------------No entiendo esta parte----------------
            '''Si quito esta línea de código el texto de indicadores se fuñe, pero no entiendo porque'''
            Game(self.nivel).endtime()   
            # ------------No entiendo esta parte----------------
            
            # ----------------------------#Desplegando los botones--------------------------
            b1 = Button(self.myscreen.screen, self.sizebtn,self.bton1_text,  Color().green, Color().black,(180, self.posbty))
            b1.drawbutton()
            b2 = Button(self.myscreen.screen, self.sizebtn,self.bton2_text, Color().green, Color().black,(280,self.posbty))
            b2.drawbutton()
            b3 = Button(self.myscreen.screen, self.sizebtn,self.bton3_text, Color().green, Color().black,(380,self.posbty))
            b3.drawbutton()
            b4 = Button(self.myscreen.screen, self.sizebtn,self.bton4_text, Color().green, Color().white,(480,self.posbty))
            b4.drawbutton() #Reset
            b5 = Button(self.myscreen.screen, self.sizebtn,self.bton5_text, Color().green, Color().red,(580,self.posbty))
            b5.drawbutton() #Nivel
            # ----------------------------#Desplegando los botones--------------------------

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.repeat = 0 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.get_rect().collidepoint(pygame.mouse.get_pos()) and self.bton_suma_correcta == 1:
                        self.aciertos += 1
                        self.txtcorrecto = "Correcto"
                        self.correcto += 1
                        self.Score += 1
                        self.bton_suma_correcta = 0
                    elif b2.get_rect().collidepoint(pygame.mouse.get_pos()) and self.bton_suma_correcta == 1:
                        self.aciertos += 1
                        self.txtcorrecto = "Correcto"
                        self.correcto += 1
                        self.Score += 1
                        self.bton_suma_correcta = 0
                    elif b3.get_rect().collidepoint(pygame.mouse.get_pos()) and self.bton_suma_correcta == 2:
                        self.aciertos += 1
                        self.txtcorrecto = "Correcto"
                        self.correcto += 1
                        self.Score += 1
                        self.bton_suma_correcta = 0
                    elif b4.get_rect().collidepoint(pygame.mouse.get_pos()): #Reset
                        say("b4", "reset").imprimir()
                    elif b5.get_rect().collidepoint(pygame.mouse.get_pos()):   #Nivel 
                        print(self.nivel)
                        self.nivel += 1
                        if self.nivel > 5:
                            self.nivel = 1
                else:
                    correcto = 3


            #control del texto desplegado
            if current_time < self.message_end_time:
                self.myscreen.screen.blit(text_render, text_render.get_rect(center = self.myscreen.screen.get_rect().center))
                #self.myscreen.screen.blit(self.txtcorrecto, (100,100))  
                # pygame.time.wait(200)
            else:
                '''
                Mucho poder en esta parte
                Controlamos el tiempo de despliegue del texto
                '''
                
                self.message_end_time = Game(self.nivel).endtime()
                self.numtext = Game(self.nivel).operaciones_aleatorias()[0] #This python trick is called tuple unpacking
                text_render = self.font.render(self.numtext, True, Color().black)
                self.myscreen.screen.blit(text_render, text_render.get_rect(center = self.myscreen.screen.get_rect().center))
                #Colocando los indicadores
                aleatorio = random.randint(1, 3) #Para saber en cual boton se coloca la respuesta correcta
                resultado_operacion = operacion[1] #Resultado de la operación 
                
                space = "  " #para centrar el texto
 
                if aleatorio == 1:
                    self.bton1_text= space+ str(resultado_operacion) + space
                    self.bton2_text= space+ str(random.randint(0,100)+resultado_operacion+1)+ space
                    self.bton3_text= space+ str(random.randint(0,100)+resultado_operacion)+ space
                    self.bton_suma_correcta = 1
                elif aleatorio == 2:
                    self.bton2_text= space+ str(resultado_operacion)+ space
                    self.bton1_text= space+ str(random.randint(0,100)+resultado_operacion+1)+ space
                    self.bton3_text= space+ str(random.randint(0,100)+resultado_operacion)+ space
                    self.bton_suma_correcta = 2
                elif aleatorio == 3:
                    self.bton3_text= space+ str(resultado_operacion)+ space
                    self.bton1_text= space+ str(random.randint(0,100)+resultado_operacion+1)+ space
                    self.bton2_text= space+ str(random.randint(0,100)+resultado_operacion)+ space
                    self.bton_suma_correcta = 3
                      

            escribir = TextScreen(self.myscreen.screen, self.textinfo,25,Color().white, 650, 30)
            escribir.display()

            pygame.display.flip()

#starting  the game
if __name__ == "__main__":
    #inicializando pygame
    pygame.init()
    game = Game(1)
    game.game_loop()
    pygame.quit()
    sys.exit()