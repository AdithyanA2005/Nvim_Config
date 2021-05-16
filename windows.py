def main():
    """
    This is the main runnable function
    """
    init_vim()


def init_vim():
    """
    This function will optimise tehe init file for windows
    """
    init_file = open('init.vim', 'r')
    init_text = init_file.read()

    wind_text = init_text.replace('.config', 'AppData/Local')
    print(wind_text)

    f = open('init.vim', 'w')
    f.write(wind_text)



if __name__ == '__main__':
    main()
