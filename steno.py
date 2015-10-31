from PIL import Image

def bits_code(code):
    """Converts a string into an array of the bit code"""
    eight_code = []
    for i in code:
        bit  = bin(ord(i))[2:]
        print(bit)
        bit = '00000000'[len(bit):] + bit
        print(bit)
        eight_code.extend([int(b) for b in bit])
    return eight_code

bits = bits_code('he')

image = Image.open('cat.jpg')
im = image.load()
x_size, y_size = image.size

x,y = 0,0
for bit in bits:
    #print(im[x,y])
    r,g,b = im[x,y][0], im[x,y][1],im[x,y][2]
    
    im[x,y] = (r-r%2 + bit,g,b)
    
    print(im[x,y])
    
    x+=1
    if x>x_size:
        x = 0
        y+=1
        if y>y_size:
            raise IndexError("image is not large enough")
    

image.save('cat_secret.jpg')