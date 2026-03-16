from PIL import Image

#pass img in function
def decode_msg(imgPath):
    #get img details
    img = Image.open(imgPath)
    width , height = img.size
    pixels = img.load()

    binaryString = ''
    #loop thru pixels
    for y in range(0,height):
        for x in range(0,width):
           
          r, g, b = pixels[x, y]

          binaryString += str(r&1)
          binaryString += str(g&1)
          binaryString += str(b&1)

    realMsg = ''
    for bit in range(0,len(binaryString),8):
      byte = binaryString[bit:bit+8]
      currchar = chr(int(byte,2))
      realMsg += currchar
      if "#####" in realMsg:
            break
    realMsg = realMsg.replace("#####","")

    print("Hidden message:", realMsg) 


