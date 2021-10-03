import os
import shutil
import platform
import pathlib


def manage_loc(distro):
    """
    This function will manage which file are need to be corrected on the OS path
    """
    loc_changer(distro, 'init.vim')
    loc_changer(distro, 'vim-plug/plugins.vim')
    loc_changer(distro, 'plug-config/start-screen.vim')


def loc_changer(distro, filename):
    """
    This function will change the path in the vim files
    """
    f = open(filename, 'r')
    old_text = f.read()

    if distro == "Windows":
        new_text = old_text.replace('.config', 'AppData/Local')
    elif distro == "Linux":
        new_text = old_text.replace('AppData/Local', '.config')
    else:
        print("OS not recognised")

    f = open(filename, 'w')
    f.write(new_text)
    f.close()


def package_loc(distro):
    """
    This function will create configuration directory according to the OS
    Then It will give option to rename any existing nvim configuration
    """
    if distro ==  "Windows":
	    config_dir = f"{pathlib.Path.home()}/AppData/Local/"
    elif distro == "Linux":
	    config_dir = f"{pathlib.Path.home()}/.config/"
    else:
	    print("Distro Not Supported")	

    if pathlib.Path(f"{config_dir}/nvim").is_dir():
        print(f"There is already a existing configuratin 'nvim' at '{config_dir}'")
        old_nvim_name = input("Rename It To: ")
        os.rename(f"{config_dir}/nvim", f"{config_dir}/{old_nvim_name}" )

    working_dir = pathlib.Path().absolute()
    shutil.copytree(working_dir, f"{config_dir}/nvim")


def main():
    """
    This is the main runnable function
    """
    distro = platform.system()
    manage_loc(distro)
    package_loc(distro)


if __name__ == '__main__':
    main()
