import errno
import emoji
import sys
import keyboard
import time
import platform
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

        self.os_name = platform.system()

        self.main()


    """MAIN RUNNER"""
    def main(self):
        self.banner()
        self.os_hint()
        self.action()


    @staticmethod
    def banner():
        """BANNER"""
        f = Figlet(font='mini')

        print('\n')
        print(colored(f.renderText('A n t i  A w a y'),
                      'green',
                      attrs=['blink']))


    def os_hint(self):
        if self.os_name == 'Linux':
            print('Linux OS detected.')
            print('Hint: You must install the requirements '
                  'and run the script as root.\n')
        elif self.os_name == 'Windows':
            print('Windows OS detected.')
            print('Have fun my child.\n')


    def wizardry(self):
        print(f"\n{self.boo}")
        sys.stdout.write("It must be some kind of wizardry\n"
                         "or a ghost...\n"
                         "WTF...\n"
                         f"\nHit [ CTRL + C ] to call John Constantine "
                         f"{self.constantine}")


    def always_here(self, value):
        if self.os_name == 'Linux':
            # Maintaining F13 untill i find a ghost key
            key = 'F13'
        else:
            key = 'F13'

        try:
            i = 1
            while i >= 1:
                keyboard.send(key)
                time.sleep(value)
        except IOError as io:
            if io[0] == errno.EPERM:
                sys.exit(f'You must be root/adm to run it: \n{io}')
        except Exception as err:
            sys.exit(f'\n\nAn exception occurred: \n{err}')

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
