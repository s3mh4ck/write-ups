#!/usr/bin/python

import struct
import string

print "Hello World!"

fileName="xor_4904470ca4a0fb1b43e43dc67dbaf8dd"
with open(fileName, mode='rb') as file: # b is important -> binary
    fileContent = file.read()
    print len(fileContent)
    # data = struct.unpack("I" * (len(fileContent) // 4), fileContent[0:-3])
    data = struct.unpack("B" * len(fileContent), fileContent)

    # for x in data:
    #     print bin(x), "\t", hex(x)

    # print fileContent[1:2]
    # print type(fileContent)
    # x = fileContent[1:2]
    # print len(x)
    # print bin(x), "\t", hex(x)

    # x = data[0]
    # print bin(x), "\t", hex(x), bin(x ^ 16843009)
    # print bin(x ^ 16843009), "\t", hex(x ^ 16843009)

    key = 0
    step = 1    #16843009
    for x in range(0, 256):
    # for x in range(0, 5):
        
        # x = data[0]
        # print bin(x^key), "\t", hex(x^key), chr(x)
        # print type(x)
        # data = struct.unpack("B" * len(fileContent), fileContent)
        out = bytearray(len(data))
        for i in range(0, len(data)):
            out[i] = data[i]^key
            if out[i]<10 or (out[i]>10 and out[i]<32) or out[i]>126:
                break
            # print bin(x), "\t", hex(x), "\t", chr(x)
        
        # for x in out:
        #     if x>15 and x < 31:
        #         break
        # else:
        #     print out
        # if all(c in string.printable for c in set(out)):
        #     print out
        if 'pwn' in out:
            print "We're on time %d\t" % (x), bin(key)  
            print out
            print set(out)

        key = key + step




print "END"
