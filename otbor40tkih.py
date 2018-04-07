import os
import chetkost as ch
import sys

#INPUT : dir name
dir = sys.argv[1]
try:
    outdir = sys.argv[2]
except:
    # outdir = dir+'/out'
    outdir = os.path.join(dir,'out')

# get all files from folder
l = os.listdir(dir)
# create output folder (if it doesn't exist)
os.makedirs(outdir, exist_ok=True)
# iterate over files
for ff in l:   #fn = filename
    fn = os.path.join(dir,ff)
    #reject bad files
    if not os.path.isfile(fn):
        continue
    try:
        im = ch.loadImage(fn)
    except:
        print("chetkost could not open {}".format(fn))
        continue
    mc = ch.meraChetkosti(ch.colorToGrey(im))
    #save to filename=mc (rounded to 5 digits)
    ofn = os.path.join(outdir, '{:5f}'.format(mc*1000))
    ch.saveImage(ofn, im, 'jpg')



