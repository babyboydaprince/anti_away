import errno
import emoji
import sys
import keyboard
import time
from pyfiglet import Figlet
from termcolor import colored
from colorama import Fore


"""Anti-Away was created to assist you 
when you feel in need of being away.

Use-it wisely!
Don't confuse absence with laziness..."""

class AntiAway:

    """SET-UP"""
    def __init__(self):
        """Unicode emoji print value"""
        # self.boo = '\U0001F47B'
        # self.constantine = '\u271D'

        """In case of emoji lib usage"""
        self.boo = emoji.emojize(':ghost:')
        self.constantine = emoji.emojize(':latin_cross:')

        self.main()


    """MAIN RUNNER"""
    def main(self):
        self.banner()
        self.action()


    @staticmethod
    def banner():
        """BANNER"""
        f = Figlet(font='mini')

        print('\n')
        print(colored(f.renderText('A n t i  A w a y'),
                      'green',
                      attrs=['blink']))


    def wizardry(self):
        print(f"\n{self.boo}")
        sys.stdout.write("It must be some kind of wizardry\n"
                         "or a ghost...\n"
                         "WTF...\n"
                         f"\nHit [ CTRL + C ] to call John Constantine "
                         f"{self.constantine}")

    @staticmethod
    def always_here(value):
        try:
            i = 1
            while i >= 1:
                keyboard.send("F13")
                time.sleep(value)
        except IOError as io:
            if io[0] == errno.EPERM:
                sys.exit(f'You must be root/adm to run it: \n{io}')
        except Exception as err:
            print(f'An exception occurred: \n{err}')

    def action(self):
        while True:
            try:
                interval = input("\nChoose the execution interval "
                                 "time in seconds or milliseconds (numbers only).\n"
                                 "Example: seconds -> 10, 120 "
                                 "and milliseconds -> 0.15, 0.5.\n\n"
                                 "----> ")

                user_input = float(interval)

                self.wizardry()
                self.always_here(user_input)

            except ValueError:
                print('\n')
                print(rf"{Fore.RED}Please insert a valid value: {Fore.RESET}")

            except KeyboardInterrupt:
                print('\n')
                print(rf"{Fore.GREEN}Successful exorcism!{Fore.RESET}")
                print('\n')
                sys.exit(1)


if __name__ == '__main__':
    AntiAway()
