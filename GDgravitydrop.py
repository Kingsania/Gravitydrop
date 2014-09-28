"""
filename: gravitydrop.py
description: This program finds out the amount of energy released by objects dropped
language: Python 2.7.8
date created: September 27, 2014
"""

from GDitems import *

def Intro():
    #Introduces the user to this program, explains what to do.
    print "This program is designed to find the amount of energy an object has right before hitting the ground when dropped from another object."

def Interface():
    #This program provides the options the user can do.
    
    a = True;    
    #This is run as a loop until a becomes false.
    while  a == True:
        print ""
        print "What would you like to do now?"
        print "[1] Run program"
        print "[2] Change unit system"
        print "[3] Make new item"
        print "[4] Change constants"
        print "[5] Show all items in database"
        print "[6] Exit program "
        b = input("")
        print ""
        
        if b == 1:
            #This moves to another function that runs the actual 'simulation', in theory.
            Energy = ImpactEnergy(Man,Box)
            Time = ImpactTime(Man, Box)
            print "It took "  + str(Time) + " seconds to hit the ground."
            print "A total of " + str(Energy) + " Joules were released."

        if b == 2:
            #This moves to a function that changes the unit system shown in the simulation and new items.
            print "I lied, you don't get to change it. Metric for life!"

        if b == 3:
            #This calls the itemMaker() and adds it to the database.
            print "In order to make an item, it needs three things, name, mass and height."
            print "Type each on seperate lines."
            na = raw_input("Name (string): ")
            ma = input("Mass (integer) [m]: ")
            he = input("Height (integer) [kg]: ")
            ni = itemMaker(na,ma,he)
            items.append(ni)
            print ""
            print "Item has been added."

        if b == 4:
            #This changes the pre-existing constants in the simulation.
            print "It needs to exist before you can change it."

        if b == 5:
            #This prints out the name of every item in the database with an option of going into any item's stats.

            for i in items:
                print i.name
            data = True
            while data == True:
                print ""
                print "Type [1] to see all items again, [2] to select an item and view its data, or [3] to return to menu."
                datainput = raw_input("")
                
                if datainput == "1":
                    for i in items:
                        print i.name
                        
                elif datainput == "2":
                    print ""
                    print "Type the position it appears in the list, with the topmost being 1."
                    n = input("")
                    n = n-1
                    
                    print ""
                    print "Name: " + items[n].name
                    print "Mass: " + items[n].mass
                    print "Height: " + items[n].height
                
                elif datainput == "3":
                    data = False
                    
                else:
                    print "Not a valid input, try again."
        
        if b == 6:
            #This exits the program.
            print "Exiting gravitydrop.py... "
            a = False
            
        if b == 7:
            #Prints the first item's name in the list, to show that variables carry over between programs.
            print items[1].name


#Constants
g = 9.81 #gravitation acceleration [m/s^2]

def ImpactEnergy(falling, notfalling):
    #This function calculates the amount of kinetic energy the falling object has just before impact
    #This function uses the mass of the falling object and the height of the notfalling object.
    #Inputs: falling (item), nonfalling (item)
    #Return: Energy (int)
    
    h= notfalling.height #[m]
    m= falling.mass      #[kg]

    Energy = m*g*h       #[J]
    return Energy

def ImpactTime(falling, notfalling):
    #This function measures the time it takes the falling object to hit the ground.
    #Inputs: falling (item), nonfalling (item)
    #Return: Time (int)

    # The equation used for this is Velcoity (final) / acceleration = time (seconds)
    # Velcoity is obtained by getting the square root of 2*acceleration*height of nonfalling

    g = 9.8
    Vel = (2*g*notfalling.height)**.5
    Time = Vel / g
    return Time

def Master():
    "Runs all the other functions in this program."
    Intro()
    Interface()

Master()
