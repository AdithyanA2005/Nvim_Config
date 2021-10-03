status = {}


def manage_key_values(distro, config_dir, old_nvim):
    """
    This function will add keys and values to the success table items
    """
    status['installation status'] = 'successful'
    status['operating system'] = distro
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
        print("    ➔ " + key.upper() + " "*(char_length - len(key)) + "➔ " + status[key].upper())


def installation_result(distro, config_dir, old_nvim, success_table_len):
    """
    This will check for errors if there is a error it will show the error
    else if there is no error then it will show the success messages
    """
    manage_key_values(distro, config_dir, old_nvim)
    show_success_table(success_table_len)
