import turtle
import time
import random

retrazo = 0.1
s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Proyecto Serpiente')

snake = turtle.Turtle()
snake.speed()
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []


def up():
    snake.direction = 'up'

def down():
    snake.direction = 'down'
def right():
    snake.direction = 'right'

def left():
    snake.direction = 'left'



def movimiento():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y -20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")

while True:
    s.update()

    if snake.distance(comida) < 20 :
        x = random.randint(-250,250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)

    movimiento()
    time.sleep(retrazo)


turtle.done()