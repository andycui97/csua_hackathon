from PIL import Image
from open_read_file import read_file
from cryptography.fernet import Fernet
from pip._vendor.distlib.compat import raw_input
MAX_MESSAGE_LENGTH = 30

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
    
    message_length = len(message)
    
    encode_length(message_length,im)
 
    bits = bits_code(message)
    
    encode_bits(bits,im,x_size,y_size)
    
    
    """# to be used for testing
    print(bits)
    for i in range(MAX_MESSAGE_LENGTH//3):
        print(im[i,0])
    print()
    for i in range(32):
        print(im[i,1])
    """
    
    image.save(pictureout_pn)

def update_location(x,y, max_x,max_y):
    """
    updates x and y values
    reads left to right over top to bottom
    @return: (x,y) a tuple of the updated x and y values
    """
    x+=1
    if x>=max_x: # if we finish with a row
        x = 0
        y+=1
        if y>=max_y:
            raise IndexError("image is not large enough") # ran out of fucking space   
    return (x,y)   

def encode_length(message_length, im):
    
    message_length_bitstring = ('0'*MAX_MESSAGE_LENGTH)[len(bin(message_length)[2:]):] + bin(message_length)[2:]
    for i in range(MAX_MESSAGE_LENGTH//3):
        r,g,b = im[i,0][0], im[i,0][1],im[i,0][2]
        r,g,b = (r-r%2 + int(message_length_bitstring[3*i]),g-g%2 + int(message_length_bitstring[3*i+1]),b-b%2 + int(message_length_bitstring[3*i+2]))
        im[i,0] = (r,g,b)
    
def encode_bits(bits,im,x_size,y_size):
    
    x,y = 0,1
    
    len_bits = len(bits)
    
    # we need 3 extra bits to fall back on dwai about it
    bits.append(0)
    bits.append(0)
    bits.append(0)
     
    for i in range(len_bits//3+1):     
        # im[x,y] returns a tuple (r,g,b)
        r,g,b = im[x,y][0], im[x,y][1],im[x,y][2] # update rgb values 
        
        #encoding (currently uses all three color values)
        im[x,y] = (r-r%2 + bits[3*i],g-g%2 + bits[3*i+1],b-b%2 + bits[3*i+2])

        
        x,y = update_location(x,y,x_size,y_size)
       
 
if(__name__ == '__main__'):
    
    message_path = raw_input('Enter path of message: ')
    message_name = raw_input('Enter file name containing message: ')
    
    try:
        s = read_file(message_path + message_name)
    except FileNotFoundError as err:
        print("There is no such path or file")
        pass
    
    picture_path = raw_input('Enter path for pictures: ')
    input_name =  raw_input('Enter name of input file: ')
    output_name =  raw_input('Enter name of output file: ')
    
    
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    #print(cipher_suite.encrypt(s.encode('utf-8')))
    
    try:
        encodes(picture_path+input_name, picture_path+output_name, cipher_suite.encrypt(s.encode('utf-8')).decode('utf-8'))    
    except FileNotFoundError as err:
        print("There is no such path or file")
        pass
    
    print("Stenography successful, here is your key (please save it): " + str(key.decode('utf-8')))

