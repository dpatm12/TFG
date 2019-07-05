from time import sleep
import constants
from port import Transmitter
import random

t = Transmitter(26)
for j in range(2):
	total = t.transmitData(constants.MESSAGE)
	print(''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(total)]*8)))
	sleep(random.random())