import turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segement = turtle.Turtle("square")
        snake_segement.color("white")
        snake_segement.penup()
        snake_segement.goto(position)
        self.segments.append(snake_segement)
    
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            next_x =self.segments[segment_number -1].xcor()
            next_y = self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(next_x, next_y)

        self.segments[0].forward(20)

    def up(self):
        if(self.head.heading() != 270):
            self.segments[0].seth(90)

    def down(self):
        if(self.head.heading() != 90):
            self.segments[0].seth(270)

    def left(self):
        if(self.head.heading() != 0):
            self.segments[0].seth(180)

    def right(self):
        if(self.head.heading() != 180):
            self.segments[0].seth(0)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]