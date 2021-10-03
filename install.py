import time
import platform
from vicode.replace_path import replace_path
from vicode.create_vicode import create_vicode
from vicode.installation_result import installation_result
from vicode.complete_installation import complete_installation


def main():
    """
    This is the main runnable function that will install the app
    """
    distro = platform.system()
    if distro == "Windows" or "Linux":
        try:
            print("WELCOME TO VI CODE")
            print("*-*-*-*-*-*-*-*-*-*")
            print("\n")
            time.sleep(0.5)

            print("PREPARING TO INSTALL THE APP")
            replace_path(distro)
            print("    ➔ Path in vim files to other files are changed according to your OS")
            print("\n")
            time.sleep(0.5)

            print("STARTING INSTALLATION")
            config_dir_status, old_nvim_status = create_vicode(distro)
            time.sleep(0.5)

            print("\n")
            print("SUCCESSFUL INSTALLATION")
            installation_result(distro, config_dir_status, old_nvim_status, 30)

            print("\n")
            print("    ➔ THANKS FOR CHOOSING VI-CODE")
            complete_installation()

        except Exception as e:
            print('error:')
            print(e)
            print('\n')
            print("UNSUCCESSFUL: Sorry, Due to some error the installation was broken or unsuccessful")

    else:
        print("SORRY YOU CANT INSTALL THE APP")
        print("I Am very sorry to say that our app is not yet optimised for the OS that you are using now")
        print("Currently we are only have the support for Windows and linux platform")


if __name__ == '__main__':
    main()
