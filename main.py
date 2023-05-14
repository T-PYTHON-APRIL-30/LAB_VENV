'''using what you've learned , create a new project to print Text Art in the terminal :
*Create a virtual environment & activate it
Use ART package to print Text Art.
Print the phrase "BELIEVE and ACHEIVE" designed with font block.'''

from art import *

art1 = text2art("BELIEVE and ACHEIVE",font='block', chr_ignore=True) # Return ASCII text with block font
print(art1)

print()
print()


'''Bonus
Come up with different phrases with different art and decoration'''

#WORK HARD
art2 = text2art('WORK HARD', font='cybermedum',decoration='random')
print(art2)