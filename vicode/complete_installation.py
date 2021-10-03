import webbrowser


def complete_installation():
    """
    This function will print and show to open our website so that the user could know more about it
    """
    print("        ➔ Installed successfully doesn't mean that this is now completely usable")
    print("        ➔ There are few more steps to do to get the complete out of this app")
    print("        ➔ To know more about it go to out websites after installation section")
    print("        ➔ LINK: youtube.com")
    input("        ➔ PRESS ENTER TO QUIT AND OPEN WEBSITE: ").upper()
    webbrowser.open('youtube.com')
