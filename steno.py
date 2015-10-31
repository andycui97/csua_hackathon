from PIL import Image

bits = [1,1,0,1,0,0,0,1,1,0,0,1,0,1]

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