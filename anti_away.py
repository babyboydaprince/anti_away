import os
import sys
import time
import platform
import subprocess
# import threading


"""Anti-Away was created to assist you 
when you feel in need of being away.

Use-it wisely!
Don't confuse absence with laziness..."""

class AntiAway:

    """SET-UP"""
    def __init__(self):
        self.os_name = platform.system()
        # self.background_task = None

        self.requirements = [
            'keyboard',
            'emoji',
            'pyfiglet',
            'termcolor',
            'colorama']

        self.install_missing_packages(self.requirements)
        self.main()


    """MAIN RUNNER"""
    def main(self):
        self.banner()
        self.os_hint()
        interval = self.action_menu()
        self.action(interval)

        # # Background tasking is necessairy for maintaining running animation (not stable)
        # self.background_task = threading.Thread(target=self.action(interval))
        # self.background_task.start()
        #
        # animate_task = threading.Thread(target=self.running_animation())
        # animate_task.start()

    @staticmethod
    def banner():
        from pyfiglet import Figlet
        from termcolor import colored

        """BANNER"""
        f = Figlet(font='mini')

        print('\n')
        print(colored(f.renderText('A n t i  A w a y'),
                      'green',
                      attrs=['blink']))


    @classmethod
    def running_animation(cls):
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


    @staticmethod
    def wizardry():
        import emoji
        """Unicode emoji print value"""
        # boo = '\U0001F47B'
        # constantine = '\u271D'

        """In case of emoji lib usage"""
        boo = emoji.emojize(':ghost:')
        constantine = emoji.emojize(':latin_cross:')
        print(f"\n{boo}")
        sys.stdout.write("It must be some kind of wizardry\n"
                         "or a ghost...\n"
                         "WTF...\n"
                         f"\nHit [ CTRL + C ] to call John Constantine "
                         f"{constantine}")


    @staticmethod
    def action_menu():
        from colorama import Fore

        while True:
            try:
                interval = input("\nChoose the execution interval "
                                 "time in seconds or "
                                 "milliseconds (numbers only).\n"
                                 "Example: seconds -> 10, 120 "
                                 "and milliseconds -> 0.15, 0.5.\n\n"
                                 "----> ")

                user_input = float(interval)

                if user_input:
                    return user_input

            except ValueError:
                print('\n')
                print(rf"{Fore.RED}Please insert a valid value: {Fore.RESET}")


    def action(self, timer):
        import keyboard
        from colorama import Fore

        try:
            # self.always_here(user_input)

            if self.os_name == 'Linux':
                # Maintaining F13 until I find a ghost key for linux systems
                key = 'F13'
            else:
                key = 'F13'

            self.wizardry()
            print('\n')

            i = 1
            while i >= 1:
                keyboard.send(key)
                time.sleep(timer)

        except KeyboardInterrupt:
            print('\n')

            print(rf"{Fore.GREEN}Successful exorcism!{Fore.RESET}")
            print('\n')
            sys.exit(1)

    # Installed dependency checker
    @staticmethod
    def is_package_installed(package_name):
        try:
            import importlib
            importlib.import_module(package_name)
            return True
        except ImportError:
            return False

    # Install missing dependencies and check root exec
    def install_missing_packages(self, packages):
        checkmark = '\u2713'

        try:
            if self.os_name == 'Windows':

                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"Installing missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')

            elif self.os_name == 'Linux':

                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"Installing missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    os.system('clear')

            elif self.os_name == 'Linux' and os.geteuid() != 0:
                # Running as root

                print("\nIt's recommended to run this script as root (sudo) "
                      "on Linux for system-wide installation.\n")

                print("You can run the script as root using: "
                      "sudo python anti_away.py\n")

                print("If you want to install packages in a "
                      "virtual environment, use a virtual environment.\n")

                print("\nExiting...")
                sys.exit(1)

            else:
                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"\nInstalling missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    sys.stdout.flush()
        except Exception as ex:
            print('\nAn exception occurred: \n', ex)


if __name__ == '__main__':
    # Time to Rock!
    AntiAway()
