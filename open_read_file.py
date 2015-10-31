def read_file(text_file):
    """ Takes in a text file and opens and reads it. Returns a string with the contents of the text file."""
    text_file = open(text_file, 'r')
    return text_file.read()

def write_file(text_file,text):
    text_file = open(text_file, 'w')
    text_file.write(text)
    text_file.close()