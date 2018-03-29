from __future__ import print_function, division

from PIL import Image

def img_to_ascii(img_path):

    # Initializing image
    image = Image.open(img_path)
    width, height = image.size

    # resizing image
    width_resized = width//3
    height_resized = height//3
    resized_image = image.resize((width_resized, height_resized), Image.ANTIALIAS)
    resized_image = resized_image.convert('L')
    pix = resized_image.load()

    f = open('image.txt','w') # preparing txt file
    symbols = ['@','O','c','+','/','*','.',' '] # the alphabet


    # writing to the txt file
    for i in range(height_resized):
        for j in range(width_resized):
            a = pix[j, i]
            # choosing range of brightness for each symbol in alphabet
            n = 255 // int(len(symbols)-1)
            f.write(symbols[(a//n)])
        f.write('\n')
    f.close()

if __name__ == '__main__':
    import sys
    img_path = sys.argv[1]
    print(img_path)
    img_to_ascii(img_path)
