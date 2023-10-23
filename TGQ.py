import time
print("Welcome, To The Great Quiz.")
time.sleep(3)
print("My Name Is  And I Am The Great AI.")
time.sleep(3)
print("The Instructions Are Simple, There Will Be A Question and 3 Letters Corresponding To Answers (ie. a, b and c).")
print("Type The Answer You Think is Correct.")
score=0
correct=0
wrong=0

time.sleep(10)
##Q1
print("Question One")
print("What year was Python released?")
print("a 1991")
print("b 1988")
print("c 2001")
answer=input()
if answer == "a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was 1991.")
	wrong=wrong+1
	
##Q2
print("Question Two")
print("What Does IT Stand For?")
print("a Indigenous Tribe")
print("b Information Technology")
print("c Internet Timetable")
answer=input()
if answer =="b":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Information Technology.")
	wrong=wrong+1
	
##Q3
print("Question Three")
print("What Does The I in Iphone Stand For?")
print("a Inteligent")
print("b Interface")
print("c Internet")
answer=input()
if answer =="c":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Internet.")
	wrong=wrong+1
	
##Q4
print("Question Four")
print("Who Is Steve Wozniak")
print("a The Co-Founder Of Apple")
print("b The CEO Of Microsoft")
print("c The Leader Of A Neo-Luddism Group (A Group Against Technology!).")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was The Co-Founder Of Apple.")
	wrong=wrong+1
	
##Q5
print("Question Five")
print("How Many Coding Languages Are In Use?")
print("a 10,000,000")
print("b 500,000")
print("c 2000")
answer=input()
if answer =="c":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was 2000.")
	wrong=wrong+1
	
##Q6
print("Question Six")
print("Which Of These Is Not A Peripheral?")
print("a Motherboard")
print("b Moniter")
print("c Keyboard")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Motherboard.")
	wrong=wrong+1
	
##Q7
print("Question Seven")
print("What Does RAM Stand For?")
print("a Random Allocated Motherboard")
print("b Random Access Memory")
print("c Repute Allocated Mallware")
answer=input()
if answer =="b":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Random Access Memory.")
	wrong=+1
	
##Q8
print("Question Eight")
print("What's Special About Linux")
print("a It's Open Source")
print("b It's Built For Gaming")
print("c It's Speeds Up Your Computer")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was It's Open Source.")
	wrong=wrong+1
	
##Q9
print("Question Nine")
print("What Does AR Stand For")
print("a Augmented Reality")
print("b Allocated Read")
print("c Admin Rights")
answer=input()
if answer =="a":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Augmented Reality.")
	wrong=wrong+1
	
##Q10
print("Question 10")
print("Out Of The Following Options, What Isn't A Component'")
print("a CPU")
print("b GPU")
print("c Webcam")
answer=input()
if answer =="c":
	correct=correct+1
	print("Well Done, That Was Correct!")
else:
	print("That Was Wrong, The Answer was Webcam.")
	wrong=wrong+1
	
print("Well done")
print("Correct")
print(correct)
print("Wrong")
print(wrong)
print("Thank You For Playing")

