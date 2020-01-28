'''A module for helper functions used for various tasks '''


# Finding and replacing a string in a text file
def find_and_replace(file_name, old_string, new_string):
    """
    GIVEN a file_name, an old_string to find, a new_string to replace it with
    OPEN file_name and read it
    REPLACE old_string with new_string
    WRITE new_string back to file_name
    """
    try:
        with open(file_name, "r+") as file:
            text = file.read()
            new_text = text.replace(old_string, new_string)
            file.seek(0)
            file.write(new_text)
            file.truncate()
    except IOError as e:
        print(e)

