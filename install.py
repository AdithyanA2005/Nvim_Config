import time
import platform
from vicode.replace_path import replace_path
from vicode.create_vicode import create_vicode
from vicode.installation_result import result
from vicode.complete_installation import complete_installation


def main():
    """
    This is the main runnable function
    """
    distro = platform.system()
    if distro == "Windows" or "Linux":
        try:
            print("STARTING TO OPTIMISE THE APP FOR YOUR OS")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            time.sleep(0.5)

            replace_path(distro)
            print("-------------------------------------------------------\n\n")
            time.sleep(0.5)

            print("STARTING INSTALLATION")
            print("*-*-*-*-*-*-*-*-*-*-*-*\n")
            config_dir_status, old_nvim_status = create_vicode(distro)
            error = False
            print("-------------------------------------------------------")
            time.sleep(0.5)

        except Exception as e:
            error = e

        result(distro, error, config_dir_status, old_nvim_status, 30)
        print('\n')
        time.sleep(0.4)
        complete_installation()

    else:
        print("SORRY YOU CANT INSTALL THE APP")
        print("I Am very sorry to say that our app is not yet optimised for the OS that you are using now")
        print("Currently we are only have the support for Windows and linux platform")


if __name__ == '__main__':
    main()
