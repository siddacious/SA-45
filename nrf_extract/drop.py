#
#
# OpenOCD library: https://github.com/screwer/OpenOCD
#
# change line 193
#	if not self.Name:
#
# to run: python2 drop.py
#

from OpenOCD import OpenOCD

ocd = OpenOCD()
ocd.Reset(Halt=True)

pc = ocd.Reg('pc')
reg = []

# create r0 through r12 register objects to read
for i in range(0,13):
	reg.append(ocd.Reg("r%d" % i))

# Read() returns a number
pc_reset_val = pc.Read()

# run first 10 instructions trying to find a suitable instruction
for run in range(10):

	# loop over all registers, calling Write(4) to set all registers to a value of 4
	for i in range(len(reg)):
		reg[i].Write(4)

	print("Step %d, [pc:0x%08X]" % (run, pc.Read()))
	ocd.Step()
	
	for i in range(len(reg)):
		reg_val = reg[i].Read()
		if abs(reg_val - pc_reset_val) < 2:
			print("found possible instruction at 0x%08X" % (pc.Read()))
			print("r%d = 0x%08X, pc = 0x%08X" % (i, reg_val, pc_reset_val))
			break
