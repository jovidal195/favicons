import binascii
import itertools

iconfile = 'favicon.ico'
STR_LENGTH = 60
VARIABLE = 'iconhexdata ='
INDENT = ' ' * (len(VARIABLE)+1)

def grouper(n, iterable):
    "s -> (s0,s1,...sn-1), (sn,sn+1,...s2n-1), (s2n,s2n+1,...s3n-1), ..."
    return itertools.zip_longest(*[iter(iterable)]*n, fillvalue='')

with open(iconfile, 'rb') as imgfile:
    imgdata = imgfile.read()
    hexstr = binascii.b2a_hex(imgdata)

hexlines = (''.join(group) for group in grouper(STR_LENGTH, str(hexstr)))


print (VARIABLE)

with open("output_icon.txt","w") as f:
    f.writelines(VARIABLE)
    for line in hexlines:
        f.writelines(' \\\n' + INDENT+repr(line))