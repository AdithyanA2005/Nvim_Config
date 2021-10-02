status = {}


def manage_key_values(distro, config_dir, old_nvim):
    """
    This function will add keys and values to the success table items
    """
    status['installation status'] = 'successful'
    status['operating system'] = distro

    if config_dir:
        status['config directory'] = config_dir

    if old_nvim == "deleted":
        status['old nvim config'] = 'deleted'

    elif "renamed" in old_nvim:
        status['old nvim config'] = 'renamed to ' + old_nvim.split('↑')[1]


def show_success_table(char_length):
    """
    This will beautify the table with correct no of spaces between the key and value
    """
    for key in status:
        print(key.upper() + " "*(char_length - len(key)) + "➔ " + status[key].upper())


def result(distro, error, config_dir, old_nvim, success_table_len):
    """
    This will check for errors if there is a error it will show the error
    else if there is no error then it will show the success messages
    """
    if error:
        print('error:\n' + error)
        print('\n')
        print("UNSUCCESSFUL: Sorry, Due to some error the installation was broken or unsuccessful")

    else:
        print("\n")
        print("SUCCESSFUL INSTALLATION")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-")
        manage_key_values(distro, config_dir, old_nvim)
        show_success_table(success_table_len)
