from PIL import *


def decode(picture_name):
    try:
        picture_file = Image.open(picture_name)
        pixel_array = picture_file.load()
    except TypeError as e:
        print('invalid file name, exiting')
        return
    bit_list = []
    message = ''
    for pixel_row in pixel_array:
        for pixel in pixel_row:
            bit_list.append(pixel[0]%2)
    for bit in bit_list:
        message += bit
    return message
    
    