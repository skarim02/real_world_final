#!/usr/bin/python3

import os, sys
from PIL import Image
import glob

for infile in glob.glob('ic*'):
    f, e = os.path.splitext(infile)
    outfile = f + ".JPEG"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
#                if im.mode in ("RGBA", "P"):
#                    im = im.convert("RGB")
                out = im.convert("RGB")
                out.rotate(90).resize((128,128)).save(r'/opt/icons/{0}'.format(outfile))
        except OSError:
            print("cannot convert", infile)
