import binascii

def to_bin(data):
    #print bin(int(binascii.hexlify(data),16))
    return bin(int(binascii.hexlify(data),16))

def to_text(data):
    n = int(data,2)
    return binascii.unhexlify('%x' %n)

 
