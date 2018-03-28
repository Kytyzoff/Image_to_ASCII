from PIL import Image

image = Image.open("img.jpg")
width = image.size[0]
height = image.size[1]
width_resized = width//3
height_resized = height//3
resized_image = image.resize((width_resized, height_resized), Image.ANTIALIAS)
resized_image = resized_image.convert('L')
pix = resized_image.load()
f = open('image.txt','w')
symbols = ['@','O','c','+','/','*','.',' ']

for i in range(height_resized):
    for j in range(width_resized):
        a = pix[j, i]
        n = 255 // int(len(symbols)-1)
        f.write(symbols[(a//n)])
    f.write('\n')
f.close()


