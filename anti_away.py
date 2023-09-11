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
    print(f"A ghost is pressing F13...\n"
          f"Does this key even exist?\n\n"
          f"A ghost pressing a ghost key...\nWTF man...\n"
          f"\nHit [ CTRL + C ] to call John Constantine {constantine}")