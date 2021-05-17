import os
import shutil
import platform
import pathlib

def main():
    """
    This is the main runnable function
    """
    distro = platform.system()
    change_var = manage_loc(distro)
    old_nvim = package_loc(distro)
    result(change_var, old_nvim)


def manage_loc(distro):
	try:
		loc_changer(distro, 'init.vim')
		loc_changer(distro, 'coc-settings.json')
		loc_changer(distro, 'vim-plug/plugins.vim')
		loc_changer(distro, 'plug-config/start-screen.vim')
		return True

	except Exception as e:
		print(e)
		return False


def loc_changer(distro, filename):
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
	working_dir = pathlib.Path().absolute()

	# This if else will provide the paths
	if distro ==  "Windows":
		config_dir = f"{pathlib.Path.home()}/AppData/Local/"

	elif distro == "Linux":
		config_dir = f"{pathlib.Path.home()}/.config/"

	else:
		print("Distro Not Supported")	

	nvim_dir = f"{config_dir}/nvim"

	# This if else will check whether nvim folder exist or not
	if pathlib.Path(nvim_dir).is_dir():
		os.rename(nvim_dir, f"{config_dir}/nvim.old" )
		isold = True

	else:
		isold = False

	# This will move the nvim config data
	shutil.copytree(working_dir, nvim_dir)
	print(f" 	- Configuration being created at {nvim_dir}")
	return isold


def result(change, nvim):
	if change:
		print(" 	- All .vim files variables are optimised for your os")
	else:
		print(" 	- The files variable changing was not successfully done for your os")

	if nvim:
		print("	    - It is seen that you already have a existing counfiguration for nvim ")
		print(" 	  The existing config is renamed as nvim.old")
		print(" 	  If the old configuration is not needed the please delete it")
		print(" 	  And you new configuration is successfull")
		
	else:
		print(" 	- Your nvim configuration is successfull")


if __name__ == '__main__':
    main()
