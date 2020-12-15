# imported libraries
import os
import art
import platform
import botLike
import botComment
import botStories
import botDraw

mySystem = platform.system()  # which operating system is running

while True:

    art.artName(2)

    menu = ['Like', 'Comment and Like', 'View Stories', 'Draw for Comment']

    for indice, lista in enumerate(menu):  # loop to generate an index in the list of options

        print(f'\033[0;34m[{indice}]\033[m {lista}')  # print the list of options

    print('')
    print('\033[0;33m(to finish press Ctrl + C)\033[m')

    selected = int(input('Select a function for the bot: '))  # receive the function that will be started

    print('')

