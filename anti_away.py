import emoji
import keyboard
import time

i = 1
boo = emoji.emojize(':ghost:')
constantine = emoji.emojize(':latin_cross:')

while i >= 1:
    keyboard.send("F13")
    time.sleep(5)
    print(f"\n{boo}")
    print("It must be some kind of wizardry\n"
          "or a ghost...\n"
          "WTF...\n"
          f"\nHit [ CTRL + C ] to call John Constantine {constantine}")