import time
import webbrowser

import pygame

Correct=0
Wrong=0
yaylight1=1
yaylight=1
a1='Pigs are _______, like us.'
a11=('animals')
b2='Eminem is a ______.'
b22=('rapper')
c3='You are using this on a _________ Pi.'
c33=('Raspberry')
d4='Cows only produce ____ after they have given birth.'
d44=('milk')
e5='Windows was made by _________.'
e55=('Microsoft')
f6='Apple use ___ for the Iphones OS'
f66=('iOS')
g7='The famous german scientist ______ Einstein, won a Nobel Prize!'
g77=('Albert')
h8='The capital of America is __________, D.C'
h88=('Washington')
print('Welcome to the Correct The Sentence Game!')
time.sleep(2)
print('To play the game, all you need to do is try to guess the missing words in the following sentences:')
time.sleep(2)
print('Oh, and spelling and punctuation does count.')
time.sleep(2)
print('Oi! Wait up, Would you like to listen to some music as you play this game[Y or N]')
if input()=='Y':
    webbrowser.open('http://youtube.com/watch?v=9W44NWYwa1g')
time.sleep(20)
print('Round one, Start')
#######################################
print (a1)
if input()==a11:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print (a11)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
######################################
print (b2)
if input()==b22:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print (b22)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
#######################################
print (c3)
if input()==c33:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(c33)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)	
#######################################
print (d4)
if input()==d44:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(d44)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
#######################################
print (e5)
if input()==e55:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(e55)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)	
#######################################
print (f6)
if input()==f66:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(f66)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
#######################################
print (g7)
if input()==g77:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(g77)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)	
#######################################
print (h8)
if input()==h88:
    Correct=Correct+1
    print('Correct')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzright.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)
else:
    Wrong=Wrong+1
    print(h88)
    print('Wrong')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/buzwrong.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == False:
        continue
    time.sleep(2)	
#######################################
print('Well done! You completed the game:)')
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Music/YouWon.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == False:
        continue
time.sleep(1)
print('Correct =')
print(Correct)
time.sleep(1)
print('Wrong =')
print(Wrong)