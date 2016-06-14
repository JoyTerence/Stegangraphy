from PIL import Image
import length
from encoder_decoder import to_bin
import sys

hidden = 'Hidden.png'
length = 0

def start1(filename,data):
    global path,hidden,length,bits
    im = Image.open(filename,'r')
    image_size = im.size

    im2 = Image.new('RGB',image_size,color=None)
    pix = im2.load()

    for x in range(0,image_size[0]):
        for y in range(0,image_size[1]):
            #print im.getpixel((x,y))
            im2.putpixel((x,y),im.getpixel((x,y)))
    
    im2.save(hidden)
    im2 = Image.open(hidden,'r')

    bits = to_bin(data)
    bits = bits[2:]
    #print bits

    file = open('secret.txt','w')
    length = len(bits)
    file.write(str(length))
    

    file.close()
    
    

    #Add the Pixel Values ( 3 Tupled) into List1
    list1 = []
    for x in range(0,length/2):
        for y in range(0,length/2):
            list1.append(list(im.getpixel((x,y))))

    #print "\nInitial List of pixels where data will be stored :\n" , list1

    #Add the 3rd Value of tuple from List1 into List2
    list2 = []
    for x,y,z in list1:
        list2.append(z)

    #print "\nThe 'B' value which will later contain Data\n" , list2 , "\n"

    list3 = []

    #print "The Binary Representation before and after data bit into 3rde value of tuples i.e. 'B'\n"
    #Add the Bits by replacing the last Tuple of List1 Stored now in List2 and put this into New List3
    for i in range(0,length):

        org_data = bin(list2[i])
        bin_pix = list(org_data[2:])

        #print "Before :" , bin_pix
        bin_pix[-1] = bits[i]

        #print "After : " , bin_pix
        #print

        list3.append(int(''.join(bin_pix),2))

    #Copy List1 into List4
    list4 = list1


    #print 'Initial List\n'
    #print list4
    
    #Get new List4 with modified 3rd Value of Tuple from list1
    for i in range(0,length):
        list4[i][2]=list3[i]
    
    #print "\nFinal List of RGB value \n" , list4 , "\n"

    i = 0

    for x in range(0,length/2):
        for y in range(0,length/2):
            im2.putpixel((x,y),(list4[i][0],list4[i][1],list4[i][2]))
            i = i + 1

    #print "\nValues of 2*2 Pixels After Manipulation\n"

    im2.save(hidden)


def end1():
    global hidden
    return hidden
    























    
    

    

    
    



