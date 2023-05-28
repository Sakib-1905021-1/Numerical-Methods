import turtle
import os
import winsound


wn = turtle.Screen()
wn.title("Pong by Sakib")
wn.bgcolor("black")
wn.setup(width=800, height = 600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = .12
ball.dy = .12

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Sakib: 0 Player Abir : 0", align="center", font=("Cascadia", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
def play():
    winsound.PlaySound("Start.mp3", winsound.SND_ASYNC)

while True:
    play()
    wn.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("point.mp3")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("point.mp3")

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1
        #os.system("point.mp3")

    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1
        #os.system("point.mp3")

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        #os.system("point.mp3")
        score_b += 10
        pen.clear()
        pen.write("Player Sakib: {} Player Abir : {}".format(score_a, score_b), align="center", font=("Cascadia", 24,  "normal"))

    if (ball.xcor() <- 340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1
        #os.system("point.mp3")
        score_a += 10
        pen.clear()
        pen.write("Player Sakib: {} Player Abir : {}".format(score_a, score_b), align="center", font=("Cascadia", 24, "normal"))
