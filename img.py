from PIL import Image


image = Image.open("img.jpg")
width = image.size[0]
height = image.size[1]
width_resized = width//3
height_resized = height//3
resized_image = image.resize((width_resized, height_resized), Image.ANTIALIAS)
pix = resized_image.load()
f = open('image.txt','w')
for i in range(height_resized):
    for j in range(width_resized):
        a = pix[j, i][0]
        b = pix[j, i][1]
        c = pix[j, i][2]
        s = (a + b + c) // 3

        if s in range(0,32):
            f.write('@')
        elif s in range(32,64):
            f.write('O')
        elif s in range(64,96):
            f.write('c')
        elif s in range(96,128):
            f.write('+')
        elif s in range(128,160):
            f.write('/')
        elif s in range(160,192):
            f.write('*')
        elif s in range(192,224):
            f.write('.')
        elif s in range(224,256):
            f.write(' ')
    f.write('\n')
f.close()


