import turtle as t 
import random as rd
t.bgcolor("yellow")
# game_started=0     

catterpillar=t.Turtle()
catterpillar.shape("square")
catterpillar.speed(0)
catterpillar.penup()
# catterpillar.forward(200)
catterpillar.hideturtle()


leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape("leaf",leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.penup()
leaf.hideturtle()
leaf.shape()

text_turtle=False
text_turtle=t.Turtle()
text_turtle.write("press space to start",align="center",font=("Arial",18,"bold"))
text_turtle.hideturtle()




score_turtlet=t.Turtle()
score_turtlet.hideturtle()
score_turtlet.speed(0)



# main logic
def outside_window():
    left_wall=-t.window_width()/2
    right_Wall=t.window_width()/2
    top_Wall=-t.window_width()/2
    bottom_Wall=t.window_width()/2
    (x,y)=catterpillar.pos()
    outsise=x<left_wall or x >right_Wall or y > top_Wall or y <bottom_Wall
    return outsise

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    catterpillar.color("yellow")
    leaf.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("GAme over",align="center", font=("Aerial",30,"bold"))

def display_score(current_score):
    score_turtlet.clear()
    score_turtlet.penup()
    x=(t.window_width()/2)-50
    y=(t.window_height()/2)-50
    score_turtlet.write(str(current_score),align="right",font=("Aerial",30,"bold"))


def start_game():
    game_started=False
    if game_started :
        return
    game_started=True
    score=0
    text_turtle.clear()
    catterpillar_speed=2
    catterpillar_length=3
    catterpillar.shapesize(1,catterpillar_length,1)
    catterpillar.showturtle()
    display_score(score)
    place_leaf()
    while True:
        catterpillar.forward(catterpillar_speed)
        if catterpillar.distance(leaf)<20:
            place_leaf()
            catterpillar_length=catterpillar_length+1
            catterpillar.shapesize(1,catterpillar_length,1)
            catterpillar_speed=catterpillar_speed+1
            score=score+10
            display_score(score)
        else:
            outside_window()
            game_over()       
            break



def move_up():
    
t.onkey(start_game,'space')
t.onkey(move_up,"Up")
t.onkey(move_down,"Down")
t.onkey(move_left,"Left")
t.onkey(move_right,"Right")
t.listen()
t.mainloop()


t.Screen().exitonclick()