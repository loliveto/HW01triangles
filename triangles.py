
"""
Laura Oliveto
Created based off of partial solution on canvas
I pledge my honor that I have abided by the Stevens Honor System
"""

import unittest     # this makes Python unittest module available
import math

def classify_triangle(a,b,c):
    """
    Determines the classification of a triangle based upon its side
    lengths a, b, and c.
    """
    name = ''

    if a == b and b == c and a == c:
        name = 'Equilateral'
    #this is where the fault lies, an improper check for isosceles
    elif a == c and b == c:
        name = 'Isosceles'
    #since the isosceles check is incorrect, this can also be faulty
    else:
        name = 'Scalene'
    
    if (a**2 + b**2) == round(c**2, 1):
        name = name + " and Right"

    if (a+b) <= c or (a+c) <= b or (b+c) <= a:
        name = 'Not a triangle'

    return name


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testIsosceles(self):
        self.assertEqual(classify_triangle(1.0,1.0,math.sqrt(2)), 'Isosceles and Right', 'Should be isosceles and right')
        self.assertEqual(classify_triangle(4,4,3), 'Isosceles', 'Should be isosceles')

    def testEqui(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral', 'Should be equilateral')

    def testScalene(self):
        self.assertEqual(classify_triangle(2,7,6), 'Scalene', 'Should be scalene')
        self.assertEqual(classify_triangle(3,4,5),'Scalene and Right', 'Should be scalene and right')

    def testTriangle(self):
        self.assertEqual(classify_triangle(1,2,1), 'Not a triangle', 'Should not be a triangle')

        

if __name__ == '__main__':
    # examples of running the code
    print("Example of running code:")
    print(classify_triangle(4,4,3))
    print(classify_triangle(1,2,1))
    print(classify_triangle(1.0,1.0,math.sqrt(2)))
    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
