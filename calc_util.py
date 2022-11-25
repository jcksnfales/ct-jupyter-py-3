from math import pi

def house_area(l, w):
    '''
        Takes a house's length 'l' and width 'w', then returns the house's floor area.
        Assumes the house in question is a simple rectangle. 
    '''
    return l * w

def circle_circumference(r):
    '''
        Takes a circle's radius 'r', then returns the circle's circumference.
    '''
    return 2 * pi * r