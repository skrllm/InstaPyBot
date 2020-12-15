
from time import sleep
from pyfiglet import Figlet

def artName(timeSleep=0): # function to print text in ascii art
    
    """
    ->\
    \n:param timeSleep:\
    \n:return:\
    """
    
    f = Figlet(font='slant')
    instagramName = f.renderText('Instagram bot')
    print(instagramName)
    sleep(timeSleep)

