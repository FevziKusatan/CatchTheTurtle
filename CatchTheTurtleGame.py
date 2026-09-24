import turtle, random, time
from matplotlib.pylab import size

screen = turtle.Screen()
screen.title("Catch The Turtle Game")
screen.bgcolor("lightblue")

scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.penup()

timeTurtle = turtle.Turtle()
timeTurtle.hideturtle()
timeTurtle.penup()

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.shapesize(2, 2)
turtle_instance.color("green")
turtle_instance.penup()

score = 0
gameTime = 30

def setUpScoreTurtle():
    
    topHeight = screen.window_height() / 2
    y = topHeight * 0.8
    scoreTurtle.goto(0, y)
    scoreTurtle.write("Score: 0", align="center", font=("Arial", 24, "normal"))
def setUpTimeTurtle():
    
    topHeight = screen.window_height() / 2
    y = topHeight * 0.7
    timeTurtle.goto(0, y)
    timeTurtle.write("Time: 30", align="center", font=("Arial", 24, "normal"))
def moveTurtle():
    if gameTime > 0:
        turtle_instance.hideturtle()
        turtle_instance.setpos(random.randint(-200, 200), random.randint(-200, 200))
        turtle_instance.showturtle()
        def handleClick(x,y):
            global score
            score += 1
            scoreTurtle.clear()
            scoreTurtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
        screen.ontimer(moveTurtle, 600)    
        def UpdateTime():
            global gameTime
            gameTime -= 1
            timeTurtle.clear()
            if gameTime == 0: 
                    endGame()
            elif gameTime > 0:
                timeTurtle.write(f"Time: {gameTime}", align="center", font=("Arial", 24, "normal"))
                turtle_instance.onclick(handleClick)
                
        screen.ontimer(UpdateTime, 1000)
    elif gameTime == 0:
        endGame()
def endGame():
    turtle_instance.hideturtle()
    timeTurtle.clear()
    scoreTurtle.goto(0, 0)
    scoreTurtle.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 24, "normal"))
    scoreTurtle.hideturtle()
    
setUpScoreTurtle()
setUpTimeTurtle()
moveTurtle()
screen.mainloop()