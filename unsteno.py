from PIL import Image, ImageFilter


def decode(picture_name):
    try:
        picture_file = Image.open(picture_name)
        pixel_array = picture_file.load()
    except TypeError as e:
        print('invalid file name, exiting')
        return
    bit_list = []
    message = ''
    x, y = 0, 0
    limitx, limity = picture_file.size
    while y < limity:
        x = 0
        while x < limitx:
            bit_list.append(picture_file.getpixel((x,y))[0] % 2)
            #print(x, y)
            x += 1
        y += 1
    for bit in bit_list:
        message += str(bit)
    return message

m = decode('cat_secret.png')
print(m[:16])
    