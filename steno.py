from PIL import Image

def bits_code(message):
    """Converts a string into an array of the bit code
    @return: an array of 0's and 1's that is the bitcode of the String message
    
    >>> bits_code('he')
    0110100001100101
    """
    result = []
    for char in message:
        eight_bit  = bin(ord(char))[2:]
        eight_bit = '00000000'[len(eight_bit):] + eight_bit #coerces bit to length from 7 to 8
        result.extend([int(bit) for bit in eight_bit])
    return result

def encodes(picturein_pn,pictureout_pn,message):
    """
    encodes an image (stenography!)
    @param picturein_pn: the pointer for the input file 
    @param pictureout_pn: the pointer for the output file
    @param message: String to be stenographized into our picture 
    """
    image = Image.open(picturein_pn)  
    x_size, y_size = image.size
    im = image.load()
    
    bits = bits_code(message)
        
    x,y = 0,0
    for bit in bits:
        # im[x,y] returns a tuple (r,g,b)
        r,g,b = im[x,y][0], im[x,y][1],im[x,y][2] # update rgb values 
        
        #encoding (currently last bit of red)
        im[x,y] = (r-r%2 + bit,g,b)
        
        x,y = update_location(x,y,x_size,y_size)
       
    
    image.save(pictureout_pn)

def update_location(x,y, max_x,max_y):
    """
    updates x and y values
    reads left to right over top to bottom
    @return: (x,y) a tuple of the updated x and y values
    """
    x+=1
    if x>max_x: # if we finish with a row
        x = 0
        y+=1
        if y>max_y:
            raise IndexError("image is not large enough") # ran out of fucking space   
    return (x,y)   

encodes('cat.jpg', 'cat_secret.png', 'he')    

