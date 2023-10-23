import time
import sys
import random
code=0
codenum=0
guesses=0
print("Welcome to Code Breakers, In this game you have to guess the code to win. You will have 5 chances to guess the code using 3 clues!, the code has 3 possible answers!")

#code1=gigabyte
#code2=paris
#code3=burger
codenum=random.randint(1,6)
if codenum==(1,2):
	code=gigabyte
if codenum==(3,4):
	code=paris
if codenum==(5,6):
	code=burger

def template():
	print(a)
	print(b)
	print(c)
	if input()==code:
		print("Well done, you won!")
	else:
		print("Sorry, that was wrong. Try again!")
		guesses()

def guesses():
	if guesses==3:
		sys.exit()
		
template()
if code==gigabyte:
	a="It's the technical name for 1000 megabytes"
	b="It's the most common form of storage"
	c="1000 of these make a terabyte"
	
if code==paris:
	a="It's the capital of France"
	b="The native language is French"
	c="It's a very popular tourist destination"
	
if code==burger:
	a="It originated from the port of 'Hamburg'"
	b="Usualy consists of a peice of meat with 2 peices of bread surronding it"
	c="It's a very popular american food."
