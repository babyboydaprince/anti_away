import errno
import os
import emoji
import sys
import keyboard
import time
import platform
import subprocess
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

        self.install_requirements()
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

    @staticmethod
    def running_animation():
        frames = ["|", "/", "-", "\\"]
        while True:
            for frame in frames:
                sys.stdout.write(f"\rRunning {frame}")
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust the speed of animation here


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
            # Maintaining F13 until I find a ghost key for linux systems
            key = 'F13'
        else:
            key = 'F13'

        try:
            i = 1
            while i >= 1:
                self.running_animation()
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
                                 "time in seconds or "
                                 "milliseconds (numbers only).\n"
                                 "Example: seconds -> 10, 120 "
                                 "and milliseconds -> 0.15, 0.5.\n\n"
                                 "----> ")

                user_input = float(interval)

                self.wizardry()
                print('\n')
                self.always_here(user_input)

            except ValueError:
                print('\n')
                print(rf"{Fore.RED}Please insert a valid value: {Fore.RESET}")

            except KeyboardInterrupt:
                print('\n')
                print(rf"{Fore.GREEN}Successful exorcism!{Fore.RESET}")
                print('\n')
                sys.exit(1)

    def install_requirements(self):
        req_file_w = '.\\requirements.txt'
        req_file_l = './requirements.txt'

        try:
            if self.os_name == 'Windows':

                with open(req_file_w, 'r') as file:
                    requirements = file.read().splitlines()

                user_input = input("\nHint: If requirements were "
                                   "already installed, you can "
                                   "choose ( n ) to proceed.\n"
                                   "Do you want to proceed with "
                                   "the installation? (y/n): ")

                if user_input.lower() == 'y':
                    subprocess.check_call(['pip', 'install'] + requirements)
                    time.sleep(2)
                    os.system('cls')
                else:
                    print("\nInstallation aborted.")
                    time.sleep(2)
                    os.system('cls')

            elif self.os_name == 'Linux':
                with open(req_file_l, 'r') as file:
                    requirements = file.read().splitlines()

                if os.geteuid() == 0:
                    # Running as root
                    user_input = input("\nHint: If requirements were "
                                       "already installed, you can "
                                       "choose ( n ) to proceed.\n"
                                       "Do you want to proceed with "
                                       "the installation? (y/n): ")

                    if user_input.lower() == 'y':
                        subprocess.check_call(['pip', 'install'] +
                                              requirements)
                        time.sleep(2)
                        os.system('clear')

                    else:
                        print("\nInstallation aborted.")
                        time.sleep(2)
                        os.system('clear')
                else:
                    print("\nIt's recommended to run this script as root (sudo) "
                          "on Linux for system-wide installation.\n")

                    print("You can run the script as root using: "
                          "sudo python anti_away.py\n")

                    print("If you want to install packages in a "
                          "virtual environment, use a virtual environment.\n")

                    print("\nExiting...")
                    sys.exit(1)
            else:
                print("\nUnsupported operating system:", self.os_name)

        except FileNotFoundError:
            print("\nrequirements.txt file not found.")



if __name__ == '__main__':
    # Time to Rock!
    AntiAway()
