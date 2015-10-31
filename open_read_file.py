def read_file(text_file):
    """ Takes in a text file and opens and reads it. Returns a string with the contents of the text file."""
    text_file = open(text_file, 'r')
    return text_file.read()