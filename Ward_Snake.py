# Simple Snake game in Python. 
# By Ward A. Leavines

import turtle # imports the turtle
import time # imports the time
import random # imports the random, which lets us use random numbers and placing the food to different locations

delay = 0.1 # delays the movement to 0.1 seconds

# score
score = 0 # score is set to zero
high_score = 0 # high score is set to zero

# Set up the screen 
wn = turtle.Screen() # sets up the Screen
wn.title("Snake Game") # displays the title and the author
wn.bgcolor("black") # gives the background color a "dark" appearance
wn.setup(width=600, height=600) # sets up the size of the window for the snake game 
wn.tracer(0) # turns off the animation on the screen (aka the screen updates)

# Snake head
head = turtle.Turtle() # Displays the head of the snake
head.speed(0) # The animation speed of the turtle module. It is set to 0 to allow it to move as fast as possible.
head.shape("circle") # gives the snake head a circle shape 
head.color("green") # gives the snake a green color
head.penup() # lines will not be drawn
head.goto(0,0) # puts the snake at the center of the screen 
head.direction = "stop" # represents the direction/action the snake will go to at the start of the game (You can set it to the following: stop, right, left, up, down)

# Snake food
food = turtle.Turtle() # Displays the food for the snake
food.speed(0) # The animation speed of the turtle module. It is set to 0 to allow it to move as fast as possible.
food.shape("circle") # gives the food a round shape
food.color("yellow") # gives the food a yellow color
food.penup() # lines will not be drawn
food.goto(0,100) # puts the snake at the center of the screen 

# Double Snake food
food2 = turtle.Turtle() # Displays the second food for the snake
food2.speed(0) # The animation speed of the turtle module. It is set to 0 to allow it to move as fast as possible.
food2.shape("circle") # gives the second food a round shape
food2.color("blue") # gives the second food a blue color
food2.penup() # lines will not be drawn
food2.goto(0,-100) # puts the snake at the center of the screen 

# segments of the snake's body
segments = [] 

# Pen
pen = turtle.Turtle() # sets up the score
pen.speed(0) # sets the speed
pen.shape("square") # gives the score a shape
pen.color("white") # gives the score a white font
pen.penup() # pen is up
pen.hideturtle() # hides the turtle
pen.goto(0, 260) # sets the score on 0 x-axis and 260 y-axis 
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal")) # displays the score 

# the go_up function is defined 
def go_up():
    # snake doesn't go the opposite direction of its trajectory
    if head.direction != "down":
        head.direction = "up"

# the go_down function is defined
def go_down():
    # snake doesn't go the opposite direction of its trajectory
    if head.direction != "up":
        head.direction = "down"

# the go_left function is defined
def go_left():
    # snake doesn't go the opposite direction of its trajectory
    if head.direction != "right":
        head.direction = "left"

# the go_right function is defined
def go_right():
    # snake doesn't go the opposite direction of its trajectory
    if head.direction != "left":
        head.direction = "right"

# the move function is defined
def move(): # makes the snake move
    if head.direction == "up": # if the head is pointing upwards
        y = head.ycor() # represents the y-coordinate of the variable
        head.sety(y + 20) # The head will move up by 20 each time 

# the move function is defined
def move(): # makes the snake move
    if head.direction == "up": # if the head is pointing upwards
        y = head.ycor() # represents the y-coordinate of the variable
        head.sety(y + 20) # The head will move up by 20 each time 

    if head.direction == "down": # if the head is pointing downwards
        y = head.ycor() # represents the y-coordinate of the variable
        head.sety(y - 20) # The head will move down by 20 each time 

    if head.direction == "left": # if the head is pointing left
        x = head.xcor() # represents the x-coordinate of the variable
        head.setx(x - 20) # The head will move left by 20 each time 
    
    if head.direction == "right": # if the head is pointing right
        x = head.xcor() # represents the x-coordinate of the variable
        head.setx(x + 20) # The head will move right by 20 each time 

# Keyboard bindings
wn.listen() # wn represents window, and listen() listens for keyboard input
wn.onkeypress(go_up, "Up") # gets input from the "Up" arrow key
wn.onkeypress(go_down, "Down") # gets input from the "Down" arrow key
wn.onkeypress(go_left, "Left") # gets input from the "Left" arrow key
wn.onkeypress(go_right, "Right") # gets input from the "Right" arrow key

# Main game loop
while True: # repeats over and over again
    wn.update() # The screen updates and displays the green head

    # Checks for collision with the borders
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) # pauses the game for one second
        food.goto(0,100) # sends the yellow circle back to the 100 y-axis
        food2.goto(0,-100) # sends the blue circle back to the -100 y-axis
        head.goto(0,0) # sends the head back to zero
        head.direction = "stop" # stops the head after it makes a collision with the border and gives the player the chance to start over 

        # hide the segments
        for segment in segments: # goes through each segment of the snake's body one at a time
            segment.goto(1000, 1000) # moves the segments of the snake's body off the screen after the head collides with the borders

        #  clear the segments list 
        segments.clear()

        # Resets the player's score after the game resets
        score = 0 

        pen.clear() # Clears the score and high score as they update so that it doesn't overlap 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # displays the incrementing scores (Note: we use the format() to )



    # Checks if the snake head collides with the food
    if head.distance(food) < 20: # If the distance between the food and the snake is less than 20. (Note: It's less than 20 because each of the basic shapes from turtle are 20x20)
        # Move the food to a random spot on the screen
        x = random.randint(-290, 290) # gives boundary for the food on the x-axis
        y = random.randint(-290, 290) # gives boundary for the food on the y-axis
        food.goto(x, y)
        

        # Adds a segment to the snake's body as it collects the food
        new_segment = turtle.Turtle() # sets up the segment for the snake
        new_segment.speed(0) # sets the speed to zero
        new_segment.shape("circle") # gives the snake body a circle shape
        new_segment.color("red") # gives the snake body a color red
        new_segment.penup() # makes the snake body to move around on the screen
        segments.append(new_segment) # appends the snake body (aka segments = [])

        # shotens the delay as the snake gets longer
        delay = delay - 0.001

        # increments the score
        score = score + 10 # adds 10 to the current score

        # updates the high score if the player's score is greater than it at the end of the game
        if score > high_score: # if score is greater than high score
            high_score = score # then the high score will be updated

        pen.clear() # Clears the score and high score as they update so that it doesn't overlap 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # displays the incrementing scores (Note: we use the format() to )

    # Checks if the snake head collides with the food
    if head.distance(food2) < 20: # If the distance between the food and the snake is less than 20. (Note: It's less than 20 because each of the basic shapes from turtle are 20x20)
        # Move the food to a random spot on the screen
        x = random.randint(-290, 290) # gives boundary for the food on the x-axis
        y = random.randint(-290, 290) # gives boundary for the food on the y-axis
        food2.goto(x, y)
        

        # Adds a segment to the snake's body as it collects the food
        new_segment = turtle.Turtle() # sets up the segment for the snake
        new_segment.speed(0) # sets the speed to zero
        new_segment.shape("circle") # gives the snake body a circle shape
        new_segment.color("red") # gives the snake body a color red
        new_segment.penup() # makes the snake body to move around on the screen
        segments.append(new_segment) # appends the snake body (aka segments = [])

        # shotens the delay as the snake gets longer
        delay = delay - 0.001

        # increments the score
        score = score + 20 # adds 20 to the current score

        # updates the high score if the player's score is greater than it at the end of the game
        if score > high_score: # if score is greater than high score
            high_score = score # then the high score will be updated

        pen.clear() # Clears the score and high score as they update so that it doesn't overlap 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # displays the incrementing scores (Note: we use the format() to )


    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is 
    if len(segments) > 0: 
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move() # calls the function

    # check for head collisions with the body segments
    for segment in segments: 

        # if statement for when the snake's head collides with the body
        if segment.distance(head) < 20: 
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for segment in segments: # goes through each segment of the snake's body one at a time
                segment.goto(1000, 1000) # moves the segments of the snake's body off the screen after the head collides with the borders

            # clear the segments list 
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay) # The delay on top is 0.1 seconds

wn.mainloop() # Keeps the window open

