import os
import shutil
import pathlib
import time


def get_config_dir(distro):
    """
    This will decide where to keep the nvim files according to different os
    """
    if distro == "Windows":
        config_dir = f"{pathlib.Path.home()}\\AppData\\Local\\"
    elif distro == "Linux":
        config_dir = f"{pathlib.Path.home()}/.config/"

    return config_dir


def check_nvim_old(nvim_dir, config_dir):
    """
    This if else will check whether nvim folder exist already or not.
    Then it will give you the option either to delete it or rename it
    """
    status = False
    if pathlib.Path(f"{nvim_dir}").is_dir():
        print("    ➔ It is noticed that you already have a existing 'nvim' folder")
        time.sleep(0.5)
        print(f"    ➔ Located at: {nvim_dir}\n")
        time.sleep(0.5)

        print("    ➔ WHAT DO TOU WANT TO DO WITH THAT FOLDER")
        time.sleep(0.5)
        print("        ➔ ENTER 'D' TO DELETE IT")
        print("        ➔ ENTER 'R' TO RENAME IT")
        del_or_rename = input("        ➔ ENTER NOW: ").upper()

        if del_or_rename == "D":
            print("            ➔ YOU HAVE CHOSEN TO DELETE IT")
            input("            ➔ PRESS ENTER KEY TO CONTINUE OR 'Ctr+C' TO STOP INSTALLATION ")
            shutil.rmtree(f"{nvim_dir}")
            print("            ➔ SUCCESSFULLY DELETED THE EXISTING  FOLDER")
            status = "deleted"

        elif del_or_rename == "R":
            print("            ➔ YOU HAVE CHOSEN TO RENAME IT")
            input("            ➔ PRESS ENTER KEY TO CONTINUE OR 'Ctr+C' TO STOP INSTALLATION ")
            new_name = input("            ➔ RENAME: ")
            os.rename(f"{nvim_dir}", f"{config_dir}{new_name}")
            print("            ➔ SUCCESSFULLY RENAMED")
            print(f"            ➔ YOUR EXISTING 'nvim' FOLDER IS RENAMED TO '{new_name}'")
            status = f"renamed↑{new_name}"
    return status


def copy_config_dir(working_dir, nvim_dir):
    """
    This function will add[copy] the necessary data into the created nvim folder
    """
    shutil.copytree(f"{working_dir}/nvim", nvim_dir)


def create_vicode(distro):
    """
    This will run old nvim function and run the copy nvim function and return old nvim
    """
    working_dir = pathlib.Path().absolute()
    config_dir = get_config_dir(distro)
    old_nvim = check_nvim_old(f"{config_dir}nvim", config_dir)
    copy_config_dir(working_dir, f"{config_dir}nvim")
    return config_dir, old_nvim
