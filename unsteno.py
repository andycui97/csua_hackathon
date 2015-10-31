from PIL import Image, ImageFilter


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

def picture_traverse(picturefile, y_max=1): # temporary y_max implementation because test image is too large
    """Traverses a picture 2d-array style, left to right and decodes the binary message encoded into the file.
    @param picturefile: the picture that is to be decoded
    @param: y_max: the row number to iterate to
    @return: [binary1, binary2, ...] a list of the bits hidden the red value of the picture
    """
    x_max = picturefile.size[0]
    bit_list = []
    for y in range(y_max):
        for x in range(x_max):
            bit_list.append(picturefile.getpixel((x,y))[0] % 2)
    return bit_list

s = decode('cat_secret.png')
print(code_bits(s[:16]))

    