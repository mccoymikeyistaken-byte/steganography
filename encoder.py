from PIL import Image

def encode_msg(imgPath,msg,finalImg):
    # Encode data
    msgInBinary = ''
    msg = msg + "#####"
    for char in msg:
      binary = format(ord(char),'08b')
      msgInBinary += binary

    img = Image.open(imgPath)
    width , height = img.size
    pixels = img.load()

    bit_index = 0

    for y in range(0,height):
        for x in range(0,width):

            if bit_index >= len(msgInBinary):
                img.save(f'{finalImg}.png')
                print("msg encoded")
                return
            
            r, g, b = pixels[x, y]

            if bit_index < len(msgInBinary):
                r = (r & 254) | int(msgInBinary[bit_index])
                bit_index+=1

            if bit_index < len(msgInBinary):
                g = (g & 254) | int(msgInBinary[bit_index])
                bit_index+=1

            if bit_index < len(msgInBinary):
                b = (b & 254) | int(msgInBinary[bit_index])
                bit_index+=1

            pixels[x, y] = (r, g, b)

    img.save(f'{finalImg}.png')
    