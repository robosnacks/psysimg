import argparse

# Start offset of each unit, 0x800000 bytes between each disk
UNIT = {
     '4': 0x102000,
     '5': 0x902000,
     '9': 0x1102000,
     '10': 0x1902000,
     '11': 0x2102000,
     '12': 0x2902000
}

SLICE = 0x7fe000

def main ():
     parser =  argparse.ArgumentParser()
     group = parser.add_mutually_exclusive_group(required=True)
     group.add_argument("-e", "--image-to-extract", type=str, help="image to extract a specified unit from")
     group.add_argument("-u", "--image-to-update", type=str, help = "image to be updated with a specified modified unit")
     parser.add_argument("volume", type=str, help=".vol file to be extracted or to update image with")
     parser.add_argument("unit", type=str, choices=["4","5","9","10","11","12"], help="unit #, can be 4,5,9,10,11 or 12")
     args = parser.parse_args()

     if args.image_to_extract:
          extractvol(args.image_to_extract,args.volume,UNIT[args.unit])
     elif args.image_to_update:
          updateimage(args.image_to_update,args.volume,UNIT[args.unit])
     else:
          parser.print_help()

def extractvol(img,vol,unit):
    with open(img,'rb') as src:
          src.seek(unit)
          with open(vol,'wb') as dest:
               data = src.read(SLICE)
               dest.write(data)

def updateimage(img,vol,unit):
     with open(img,'r+b') as dest:
          dest.seek(unit)
          with open(vol,'rb') as src:
               data = src.read()
               dest.write(data)

if __name__ == '__main__':
     main()
