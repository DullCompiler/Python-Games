#the tale of lenny
import pygame
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)
GPIO.output(25,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
lenny='(° ͜ʖ °)'
lennydead='(x .ʖ x)'
bor='BORING'
exc='EXCITING'
las='LASER KILLED HIM'
dra='DRAGON TURNED THE WORLD ALL YELLOW'
sti='STICK'
sun='SUN'
a=0
b=1
print('This is the tale of lenny')
print(lenny)
time.sleep(1)
print('lenny was a happy chap')
time.sleep(1)
print('But one day he had a ______')
time.sleep(1)
print('What day did lenny have? Did lenny have BORING or EXCITING day (use the the words in captital to decide!)')
if input()==(bor):
    print('Oh well then, lenny existed for a bit')
    print(lennydead)
    print('There is that what you want!')
    print('THE END')
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.50)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(0.50)
    GPIO.output(25,GPIO.HIGH)
    time.sleep(0.50)
    GPIO.output(25,GPIO.LOW)
    time.sleep(0.50)
    GPIO.output(23,GPIO.LOW)
    time.sleep(0.50)
    GPIO.output(18,GPIO.LOW)
if input()==(exc):
    print('lenny walked out of his 12$ house and on to the street but then a LASER KILLED HIM or a DRAGON TURNED THE WORLD ALL YELLOW')
    print('/``\_(° .ʖ °)_________(===============>:=(OOOO)=-_-_-_-=')
    if input()==(las):
        print('Well then, ok. lenny was killed by a pink laser beam from the meme star, and he died.')
        print('/``\_(x .ʖ(==================>:=(OOOO)=-_-_-_-=')
        print(lennydead)
        print('THE END')
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
    if input()==(dra):
        print('Well, ah yes wise choice. The world was suddenly turned yellow by a fluffy, pink and purple, cuddly and sweet hearted dragon. But lenny was having none of that, lenny was going to make it stop existing for a bit. Now how was lenny going to destroy said dragon?')
        print('Did lenny destroy said dragon with a STICK or a SUN')
        if input()==(sti):
            print('Ok lenny hit it with a stick and it cuddled him to death.')
            print('---(x .ʖ>:=(OOOO)=-_-_-_-=')
            print(lennydead)
            print('THE END')
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(25,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
        if input()==(sun):
            print('the sun is a deadly laser')
            print('( 0(=============)')
            print('and the moon is a deadly rock')
            print('0=deadly rock')
            print('Suddenly lenny grabbed the sun with oven mittens and shot down said dragon!')
            print('(° .ʖ °)¬0(===============):=(OOOO)=-_-_-_-=')
            print('Well done lenny/player, You have just defeated said dragon!')
            print('THE END')
            pygame.mixer.init()
            pygame.mixer.music.load("/home/pi/Music/YouWon.ogg")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == False:
                continue
            if a<b:
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(23,GPIO.HIGH)
                GPIO.output(25,GPIO.HIGH)
                GPIO.output(25,GPIO.LOW)
                GPIO.output(23,GPIO.LOW)
                GPIO.output(18,GPIO.LOW)
        
    
