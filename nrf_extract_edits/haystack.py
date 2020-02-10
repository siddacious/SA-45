#!/usr/bin/env python2
# to run: python2 pickup.py
#
# OpenOCD library: https://github.com/screwer/OpenOCD
# change line 193
#	if not self.Name:
#

# Use the OpenOCD library
from OpenOCD import OpenOCD
import sys

def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return bytearray(result)

# create connection to running instance of OpenOCD 
ocd = OpenOCD()

# reset and halt the processor
ocd.Reset(Halt=True)

# create a variable for the program counter register
pc = ocd.Reg("pc")

# the address found with drop.py that contains the instruction 
# that will copy the contents of memory and store it in a register


########## GOODIES ########################
# found possible instruction at 0x000006D6
# r4 = 0x000006D1, pc = 0x000006D0
# 
# found possible instruction at 0x000006DE
# r3 = 0x000006D1, pc = 0x000006D0
###########################################


# Instruction for BB units?
#pc_pickup_val = 0x6DC

pc_pickup_val = 0x6DE

# the regsiter where to write the memory address to be read
write_reg = ocd.Reg("r4")

# the register to read the value stored at the specified memory
read_reg = ocd.Reg("r3")

# the size of the the chip's flash memory
#flash_size = 0x40000
flash_size = 0x1000

# the output filename
outfile = "dump2.bin"

# reset all registers to 0 (do we really need this ??)
reg = []
for i in range(0,13):
	reg.append(ocd.Reg("r%d" % i))
for i in range(len(reg)):
	reg[i].Write(0)

# create output file
data = open(outfile, 'w+b')

# loop over all memory
for addr in range(0,flash_size,4):

	# write the address of the memory copy instruction to the program counter
	pc.Write(pc_pickup_val)


  # reset all registers to 0 (do we really need this ??)
  reg = []
  for i in range(0,13):
  	reg.append(ocd.Reg("r%d" % i))
  for i in range(len(reg)):
  	reg[i].Write(0)
  



	# write the memory address to be read
	write_reg.Write(addr)

	# execute the instruction
	ocd.Step()

	# read the memory contents back
	buf = read_reg.Read()

	# convert the int value to bytes and write that to the output file
	#data.write(int_to_bytes(buf,4))

	# create some sort of output so we know the program is still running (it takes a while)
	sys.stdout.write('.')
	sys.stdout.flush()
	print("[0x%08X] 0x%08X" % (addr, buf))

data.close()
	
print()
print("Done")
