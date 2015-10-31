from PIL import Image, ImageFilter
MAX_MESSAGE_LENGTH = 30

def decode(picture_name):
    """Takes in a picture name, and returns a list with the bits of the secret message.
    @param picture_name: filename of the picture to be decoded
    @return: a string of bits
    """
    try:
        picture_file = Image.open(picture_name)
    except TypeError as e:
        print('invalid file name, exiting')
        return
    message = ''
    bit_list = picture_traverse(picture_file)
    for bit in bit_list:
        message += str(bit)
    return message

def code_bits(bits):
    """Translates a string of bits into a readable string.
    @param bits: a list of bits taken from the picture
    @return: '<secret message>' a string that was the hidden message
    """
    string_code = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8] #decryption algorithm
        string_code.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(string_code)

def picture_traverse(picturefile): # temporary y_max implementation because test image is too large
    """Traverses a picture 2d-array style, left to right and decodes the binary message encoded into the file.
    @param picturefile: the picture that is to be decoded
    @return: [binary1, binary2, ...] a list of the bits hidden the red value of the picture
    """
    message_length = get_message_length(picturefile)
    x_max = picturefile.size[0]*3
    value_list = []
    y_max = message_length // x_max + 1
    for y in range(1, y_max):
        for x in range(x_max):
            value_list.append(list(picturefile.getpixel((x,y))))
    bit_list = [character_num % 2 for character_num in range(message_length)]  # take only the required number of bits
    return bit_list

def get_message_length(picturefile):
    """Gets the length of the message encoded inside the picture.
    The length of the message is encoded in the first 10 pixels, giving us 2^30 maximum length.
    @param picturefile: the picture to be decoded
    @return: int - the number of characters in the message
    """
    binary_length_list = []
    for x in range(MAX_MESSAGE_LENGTH//3):
        binary_length_list.append(list(picturefile.getpixel((x, 1)))) # grabs tuples only from the top line
    count = 0
    while count < len(binary_length_list):
        binary_length_list[count] %= 2
    binary_string = ''
    for bit in binary_length_list:
        binary_string += str(bit)
    return int(binary_string, 2)

s = decode('cat_secret.png')
print(code_bits(s[:16]))

    