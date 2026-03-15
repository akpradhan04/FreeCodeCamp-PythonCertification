def add_setting(dic, tup):
    lower_tuple = tuple(map(str.lower, tup))
    if lower_tuple[0] in dic:
        return f"Setting '{lower_tuple[0]}' already exists! Cannot add a new setting with this name."
    else:
        dic[lower_tuple[0]] = lower_tuple[1]
        return f"Setting '{lower_tuple[0]}' added with value '{lower_tuple[1]}' successfully!"

def update_setting(dic, tup):
    lower_tuple = tuple(map(str.lower, tup))

    if lower_tuple[0] in dic:
        dic[lower_tuple[0]] = lower_tuple[1]
        return f"Setting '{lower_tuple[0]}' updated to '{lower_tuple[1]}' successfully!"
    else:
        return f"Setting '{lower_tuple[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic, key):
    lower_key = key.lower()
    if lower_key in dic:
        del dic[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dic):
    if not dic:
        return "No settings available."
    else:
        text = "Current User Settings:\n"
        for key, value in dic.items():
            text += f'{key.capitalize()}: {value}\n'

    return text

test_settings = {'theme':'dark', 'volume':'medium'}

