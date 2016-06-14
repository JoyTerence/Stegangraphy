#!/usr/bin/python
from PIL import Image
from Image1 import end1
from encoder_decoder import to_text 

path = end1()

im = Image.open(path,'r')
im.load()

file = open('Secret.txt','r')

length = int(file.readline())
list1 = []

for x in range(0,length/2):
    for y in range(0,length/2):
        list1.append(list(im.getpixel((x,y))))

list2 = []
for x,y,z in list1:
    list2.append(z)

list3 = []

for i in range(0,length):
    org_data = bin(list2[i])
    bin_pix = list(org_data[2:])
    list3.append(bin_pix[-1])

binary_extract = '0b' + ''.join(list3)
print "Hidden Text : " , to_text(binary_extract)

k = raw_input(" ")


        
