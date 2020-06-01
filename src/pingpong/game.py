import turtle as t
import simpleaudio as sa

#background music
bgm_obj = sa.WaveObject.from_wave_file('bgm.wav')
bgm_obj.play()

#construct background
game = t.Screen()
game.title('double ping pong')
game.bgcolor('black')
game.setup(800, 600)
game.tracer(0) # no refresh

border = t.Turtle()
#border.ht()
border.up()
border.color('white')
border.shape('turtle')
border.goto(-380, 350)
border.down()
border.goto(-380, -350)
border.goto(380, -350)
border.goto(380, 350)
border.goto(-380, 350)


#create left racket
r1 = t.Turtle()
r1.ht() # hide
r1.up() # pen up
r1.speed(0)
r1.color('yellow')
r1.shape('square')
r1.shapesize(5, 1) # strench square 100 * 20
r1.goto(-350, 0)
r1.st() # show

#create right racket
r2 = t.Turtle()
r2.ht() # hide
r2.up() # pen up
r2.speed(0)
r2.color('green')
r2.shape('square')
r2.shapesize(5, 1) # strench square
r2.goto(350, 0)
r2.st() # show

#create ball
#radius = 10
ball = t.Turtle()
ball.up() # pen up
ball.speed(0)
ball.color('white')
ball.shape('circle')
#ball.st()
#speed of ball
ball.dx = 0.2
ball.dy = 0.2

player_speed = 50
r1_score = 0
r2_score = 0

head = t.Turtle()
head.ht()
head.up()
head.color('white')
head.goto(-5, 300)
head.write('SCORE', align = 'center', font = ('Arial', 20, 'bold'))

#write score
def write_score():
    pen.clear()
    score_text = 'LEFT: {}    VS    RIGHT: {}'.format(r1_score, r2_score)
    pen.write(score_text, align = 'center', font = ('Arial', 15))

pen = t.Turtle()
pen.ht()
pen.up()
pen.color('white')
pen.goto(-5, 250)
write_score()

def r1_up():
    y = r1.ycor()
    if y < 300:
        r1.sety(y + player_speed)

def r1_down():
    y = r1.ycor()
    if y > -300:
        r1.sety(y - player_speed)

def r2_up():
    y = r2.ycor()
    if y < 300:
        r2.sety(y + player_speed)

def r2_down():
    y = r2.ycor()
    if y > -300:
        r2.sety(y - player_speed)


game.listen()
game.onkey(r1_up, 's')
game.onkey(r1_down, 'x')
game.onkey(r2_up, 'Up')
game.onkey(r2_down, 'Down')

#whether to end game
running = True
def stop_loop():
    global running;
    running = False

root = game.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', stop_loop)

#main loop
while running:
    game.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    #catch ball
    
    if ball.ycor() < r2.ycor() + 50 and ball.ycor() > r2.ycor() - 50 and ball.xcor() > 340:
        ball.dx *= -1
        ball.setx(339)

    if ball.ycor() < r1.ycor() + 50 and ball.ycor() > r1.ycor() - 50 and ball.xcor() < -340:
        ball.dx *= -1
        ball.setx(-339)

    #ball out of screen
    if ball.xcor() > 380:
        ball.goto(0, 0)
        r1_score += 1
        #print('left win')
        pen.clear()
        write_score()
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        r2_score += 1
        #print('right win')
        pen.clear()
        write_score()

#game.mainloop()
