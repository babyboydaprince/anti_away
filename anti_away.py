# import emoji
import keyboard
import time
from pyfiglet import Figlet
from termcolor import colored


"""BANNER"""
f = Figlet(font='mini')
print('\n')
print(colored(f.renderText('A n t i  A w a y'),
              'green',
              attrs=['blink']))


"""SET-UP"""
i = 1
"""Unicode emoji print value"""
boo = '\U0001F47B'
constantine = '\u271D'

"""In case of emoji lib usage"""
# boo = emoji.emojize(':ghost:')
# constantine = emoji.emojize(':latin_cross:')


while True:
    try:
        interval = input("\nChoose the execution interval "
                          "time in seconds or milliseconds (numbers only).\n"
                          "Example: seconds -> 10, 120 "
                          "and milliseconds -> 0.15, 0.5.\n\n"
                          "----> ")

        user_input = float(interval)

        break
    except ValueError:
        print('Please insert a valid value')


while i >= 1:
    keyboard.send("F13")
    time.sleep(user_input)
    print(f"\n{boo}")
    print("It must be some kind of wizardry\n"
          "or a ghost...\n"
          "WTF...\n"
          f"\nHit [ CTRL + C ] to call John Constantine {constantine}")