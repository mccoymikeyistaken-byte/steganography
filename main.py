import argparse
import encoder
import decoder

parser = argparse.ArgumentParser(description="SIMPLE STEGANOGRAPHY TOOL")

parser.add_argument("mode", choices=["encode","decode"],help= "Encode/Decode" )
parser.add_argument("-m","--message",help="Message to hide")
parser.add_argument("-i","--image",required=True,help="Input Image")
parser.add_argument("-o","--output", default="encoded.png",help="filename of encoded image(without extension)")

args = parser.parse_args()

if args.mode == "encode":
    encoder.encode_msg(args.image, args.message,args.output)

elif args.mode == "decode":
    decoder.decode_msg(args.image)