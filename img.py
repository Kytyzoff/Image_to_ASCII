from __future__ import print_function, division

from PIL import Image

def img_to_ascii(img_path, output_path):

    # Initializing image
    image = Image.open(img_path)
    width, height = image.size

    # resizing image
    width_resized = width//3
    height_resized = height//3
    resized_image = image.resize((width_resized, height_resized), Image.ANTIALIAS)
    resized_image = resized_image.convert('L')
    pix = resized_image.load()

    # f = open(output_path+'\image.txt','w') # preparing txt file
    symbols = ['@','O','c','+','/','*','.',' '] # the alphabet
    buffer = ''

    # writing to the txt file
    for i in range(height_resized):
        for j in range(width_resized):
            a = pix[j, i]
            # choosing range of brightness for each symbol in alphabet
            n = 255 // int(len(symbols)-1)
            buffer = buffer + symbols[a//n]
        buffer = buffer +('\n')

    # writing to a file
    with open(output_path+'\image.txt','w') as f:
        f.write(bufer)

if __name__ == '__main__':

    import sys
    import os.path

    img_path = sys.argv[1]

    # Initializing output path
    output_path = os.path.dirname(img_path)
    print('Output path: '+output_path)

    img_to_ascii(img_path, output_path)

