from time import sleep
import constants
from port import Receiver
import binascii


r = Receiver(26)
i = 0
for j in range(100):
	total = r.read()
	print(''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(total)]*8)))
	if	''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(total)]*8)) == constants.MESSAGE:
		print("OK")
		i = i+1

print(i)