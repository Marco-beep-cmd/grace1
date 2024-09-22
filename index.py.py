import math
import turtle
import time
import pygame  # Para la música

# Inicializar pygame para la música
pygame.mixer.init()
pygame.mixer.music.load("flowersss.mp3")  
pygame.mixer.music.play(-1)  

# Configuración inicial de turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
phi = 137.508 * (math.pi / 180.0)
turtle.fillcolor("orangered")
turtle.pencolor("black")
for i in range(160):  
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.setheading(i * 137.508)
    turtle.stamp()  


turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for i in range(160, 300):  
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    

    turtle.setheading(turtle.towards(0, 0) + 180)
    
    
    turtle.begin_fill()
    turtle.circle(100, 110)  
    turtle.left(100)
    turtle.circle(80, 90)
    turtle.end_fill()

# Girar la flor completa
def girar_flor():
    for _ in range(36):  # 36 iteraciones de 10 grados hacen una vuelta completa
        turtle.right(10)
        time.sleep(0.1)  # Pausa para el efecto de giro lento

# Función para mostrar el mensaje con efecto de "latido"
def mostrar_mensaje():
    turtle.penup()
    turtle.goto(0, -250)  #  mensaje debajo de la flor
    turtle.pendown()
    
    # Latido constante sin cambiar tamaño
    while True:
        turtle.clear()  
        turtle.color("yellow")
        turtle.write("Te quiero, estas flores amarillas son para vos", align="center", font=("Arial", 30, "bold"))
        time.sleep(0.5)
        
        turtle.clear()  
        time.sleep(0.5)  
girar_flor()
mostrar_mensaje()  
turtle.done()
pygame.mixer.music.stop()  
