# # LAB_VENV


# ## using what you've learned , create a new project to print Text Art in the terminal :
# - Create a virtual environment & activate it
# - Use ART package to print Text Art.
# - Print the phrase "BELIEVE and ACHEIVE" designed with font block.

from art import *

Art=text2art("BELIEVE and ACHEIVE",font='block')
print(Art)

# ## Bonus
# - Come up with different phrases with different art and decoration
Art2=text2art("Hello",font='random')
print(Art2)
