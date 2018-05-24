#this program finds the area of a circle in the most annoying way possible

import time #import the time module so we can add delays later

print("The circle calculator!") #print the name of the program
time.sleep(1) #this adds a bit of time delay, just to allow the human brain time to read and process the messages before moving on

print("Provide the radius of your circle to find the area (please only type numbers in to this program, or it will crash. Sorry.") #tell the user what the program does
time.sleep(2) #the number tells the computer how many seconds to wait, i've increased it to 2 here
print ("\n") #this prints a blank line, which will hopefully make the text on the screen appear a little less busy and confusing

radius = input("What is the radius of the circle? ") #This asks the user for the radius of a circle, and waits for input
time.sleep(1)
print ("\n")

pi = 3.14159  #that's pi, rounded to as many decimals as I could remember

area = pi * radius**2 #this is the actual calculation

print("Wait, hold on, I'm pretty stoned and can't remember how to do this") #print a little bit of a joke for the user. This has nothing to do with the calculation.
time.sleep(2) 
print("okay, ummmm...")
time.sleep(5)
print("Here we go, got it!")
time.sleep(2)
print ("\n")

print("The area of your circle is: ") 
time.sleep(1)
print(area) #tells the user the area of the circle
time.sleep(3) 
print ("\n")

test = raw_input("Did this help you pass your geometry test? (y/n) ") #get user feedback
time.sleep(1)
if test == "y": #If the user enters y
	print("You're very welcome") #we take credit
elif test == "yes": #If the user enters yes
	print("You're very welcome") #we take credit
elif test == "n": #if the user enters n
	print("That's definitely your fault, loser. Not mine.") #we give them a hard time
elif test == "no": #if the user enters no
	print("That's definitely your fault, loser. Not mine.") #we give them a hard time
else: #if the user doesn't enter y, n, yes, or no
	print("How hard is it to follow instructions? If you can't find the y or n keys, you have no hope for passing geometry") #let them know they failed at answering y/n
time.sleep(5)
print("That's all this program does right now") #Your program is a FAILURE. It's so dumb
time.sleep(1)

print("bye bye") #thank GOD we're getting out of here

# I hope you enjoyed this code. My wife rolled her eyes pretty hard and didn't care.

# I would like this program to have a response such as "Only enter a number" and ask for another input if a user enters letters or other characters as the radius of the circle
# I'd also like to end this program by asking if the user would like to find the area of another circle, allowing them to either repeat the program or end it with yes/no input

#If you can help me improve this silly little program in any way, please do! 
