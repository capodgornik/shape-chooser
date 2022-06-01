'''
Author: Celine Podgornik
Date: February 12th, 2017

Description:
This program allows the user to draw the number of polygons they want with characteristics
of the user's choosing. 
'''

import turtle

def polygon(pierre, num_sides, side_length):
    '''
    This function draws a polygon. 
    
    Parameters:
    pierre: a turtle that is used to draw the polygon.
    num_sides: an integer that determines how many sides the polygon will have.
    side_length: an integer that determines the side length of the polygon.

    Returns: None
    '''
    
    for i in range(num_sides):
        pierre.forward(side_length)
        pierre.left(360/num_sides)
    return None

#==========================================================
def main():
    '''
    When the file is run, first the user is asked how many polygons they would like to see. Then, for each polygon
    the user is asked how many sides the polygon should have, what color the polygon should be, and what the side
    length of the polygon should be. After answering these three questions about the polygon, the turtle will draw
    the polygon using that information before the program asks about the next polygon. 
    '''
    
    num_polygons = int(input("Enter the number of polygons you'd like to see: "))
    rory = turtle.Turtle()
    rory.pensize(5)
    rory.speed(0)
    rory.shape('turtle')
    
    for i in range(num_polygons):
        sides = int(input("Enter the number of sides: "))
        color = input("Enter the color: ")
        length = int(input("Enter the side length for you polygon: "))
        rory.pencolor(color)
        polygon(rory, sides, length) 
        
    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
