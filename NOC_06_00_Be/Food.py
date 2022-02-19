# The "Food" class
from random import randint

class Food():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.counter = 0

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
    def get_position(self):
        return self.position
    
    def random_position(self):
        self.position = PVector(randint(0, 640), randint(0, 360))
    
    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()# + PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
    
    def food_eated(self):
        self.counter = self.counter + 1
        print(self.counter)
