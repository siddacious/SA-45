#!/usr/bin/env python
#
import struct

import sys
from binascii import hexlify

def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    #result.reverse()
    return bytearray(result)

def bytes_to_int(bts, length):
    return struct.unpack("<I", bytes(bts))[0]

def bytes_to_int_r(bts, length):
    bts_ba = bytearray(bts)
    bts_ba.reverse()
    bts = bytes(bts_ba)
    return struct.unpack("<I", bts)[0]

infile = sys.argv[1] 
outfile = sys.argv[2] 

# loop over all memory
with open(infile, 'r+b') as data_in:
  with open(outfile, 'w+b') as data_out:
    for addr in range(0, 0x40000, 4):
    
      h_addr = hex(addr)
      buf = data_in.read(4)
      if len(buf) == 0:
        break
    
      reversed_buf_i = bytes_to_int_r(buf, 4) 
      norm_reversed = int_to_bytes(reversed_buf_i, 4) 
      data_out.write(norm_reversed)
  
  
print("Done")
