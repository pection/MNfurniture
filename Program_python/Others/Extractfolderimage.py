import os
import sys
import numpy as np
from PIL import Image
num=1
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to output image")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
args = vars(ap.parse_args())

path =args["input"]

filelist=[]

for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".jpg")):
            filelist.append(os.path.join(root,file))


logo2Height = watermark2.height
for filename in filelist:
    image = Image.open(filename)
    num += 1

    image.save(args["output"]+str(num)+'.jpg')
