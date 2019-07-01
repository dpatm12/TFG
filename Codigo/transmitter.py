from time import sleep
import constants
from port import Transmitter
import random

t = Transmitter(26)
for j in range(100):
	t.transmitData(constants.MESSAGE)
	sleep(random.random())