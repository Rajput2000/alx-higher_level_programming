#!/usr/bin/python3
def complex_delete(new_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary
    ...

    Parameters
    ----------
    new_dictionary : dictionary
        the given dictionary to delete value from

    Return:
        the new dictionary
    """

    while value in new_dictionary.values():
        for k, v in new_dictionary.items():
            if v == value:
                del new_dictionary[k]
                break

    return (new_dictionary)
