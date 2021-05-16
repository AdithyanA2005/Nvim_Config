import platform

def main():
    """
    This is the main runnable function
    """
    distro = platform.system()
    
    loc_changer(distro, 'init.vim')
    loc_changer(distro, 'vim-plug/plugins.vim')
    loc_changer(distro, 'plug-config/start-screen.vim')
    

def loc_changer(distro, filename):
    f = open(filename, 'r')
    old_text = f.read()

    if distro == "Windows":
        new_text = old_text.replace('.config', 'AppData/Local')
    elif distro == "Linux":
        new_text = old_text.replace('AppData/Local', '.config')
    else:
        print("OS not recognised")

    print(new_text)
    f = open(filename, 'w')

    f.write(new_text)
    f.close()


if __name__ == '__main__':
    main()
