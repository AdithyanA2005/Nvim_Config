import os


def change_path(distro, text):
    """
    This function will provide different path for different os that will be replaced in the nvim files
    """
    if distro == "Windows":
        text = text.replace('.config', 'AppData\\Local')
    elif distro == "Linux":
        text = text.replace('AppData\\Local', '.config')

    return text


def replace_path(distro):
    """
    This function will change the path in all the nvim files according to your os
    """
    for root, dirs, files in os.walk("nvim", topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            file = open(filename, 'r', encoding="utf-8")
            text = file.read()
            file.close()
            text = change_path(distro, text)
            file = open(filename, 'w', encoding="utf-8")
            file.write(text)
            file.close()
