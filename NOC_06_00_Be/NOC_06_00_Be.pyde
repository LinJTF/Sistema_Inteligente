# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(130, 130, PVector(0, 0))
    

def draw():
    background(255)
    food.update()
    food.display()
    vehicle.applyForce(food.get_position() - vehicle.get_position())
    vehicle.update()
    vehicle.display()
    if (food.get_position().dist(vehicle.get_position()) < 3.0):
        food.random_position()
        food.food_eated()


        
    
