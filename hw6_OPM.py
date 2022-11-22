###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):            

#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.




#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    number_instances = 0

    def __init__(self, name, symptoms):
        self.name = str(name)
        self.symptoms = symptoms
        Patient.number_instances += 1

    def add_test(self, test_name, test_result):
            self.test_name = str(test_name)
            self.test_result = bool(test_result)
            
    def has_covid(self):
        if self.test_name == 'covid':
            if self.test_result == True:
                return 0.99
            else:
                return 0.01
        else:
            covid_symptoms = ['fever','cough','anosmia']
            matching_symptoms = [s for s in self.symptoms if any(covid_symptoms in s for covid_symptoms in covid_symptoms)]
            return 0.05 + 0.1*len(matching_symptoms)

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

from random import shuffle

class Card:
    global suit, value
    suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  
    def __init__(self):
        pass

class Deck(Card):
    def __init__(self):
        Card.__init__(self)
        self.cardset = []
        for n in suit:
            for c in value:
                self.cardset.append((c)+" "+"of"+" "+n)
                
    def shuffle(self):
        shuffle(self.cardset)
        return self.cardset
    
    def draw(self):
        if len(self.cardset) == 0:
            return "No cards left"
        else:
            drawncard = self.cardset.pop()
            return ("Card drawn is: " + drawncard)

###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

from abc import ABC, abstractmethod
from math import pi
 
class PlaneFigure(ABC):
 
    @abstractmethod
    def compute_perimeter(self):
        pass
    @abstractmethod
    def compute_surface(self):
        pass

class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = float(base)
        self.c1 = float(c1)
        self.c2 = float(c2)
        self.h = float(h)

    def compute_perimeter(self):
        perimetert = self.base + self.c1 + self.c2 + self.h
        return ('Perimeter is: ' + str(perimetert) + ' units')
    
    def compute_surface(self):
        areat = (self.base*self.h)/2
        return ('Area is: ' + str(areat) + ' squared units')

class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def compute_perimeter(self):
        perimeterr = self.a*2 + self.b*2
        return ('Perimeter is: ' + str(perimeterr) + ' units')
    
    def compute_surface(self):
        arear = self.a*self.b
        return ('Area is: ' + str(arear) + ' squared units')
    
class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = float(radius)

    def compute_perimeter(self):
        perimeterc = pi*self.radius*2
        return ('Perimeter is: ' + str(perimeterc) + ' units')
    
    def compute_surface(self):
        areac = pi*self.radius*self.radius
        return ('Area is: ' + str(areac) + ' squared units')
