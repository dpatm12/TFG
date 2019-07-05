import constants
from gpiozero import DigitalOutputDevice
from time import sleep
import time

class Port:
	global out
	def __init__(self, pin):
		global out
		out = DigitalOutputDevice(pin)
	def transmit(self, data):
		global out
		if	int(data) == 1:
			out.on()
		else:
			out.off()
	def stop(self):
		out.off()
	def value(self):
		return out.value
		
class Receiver:
	global port
	def __init__(self, pin):
		global port
		port = Port(pin)
	
	def waitSignal(self):
		global port
		lastvalue = 0
		while True:
			# if port.value() == 1 and lastvalue == 1:
				# print("waitSignal")
				# sleep(constants.SLEEP_TIME)
				# break
			if port.value() == 1:
				print("Detected")
				sleep(constants.SLEEP_TIME)
				break
			lastvalue = port.value()
			sleep(constants.SLEEP_TIME/float(100))
	
	def read(self):
		global port
		self.waitSignal()
		total = ""
		t = time.time()
		for j in range(125):
			b = ''
			for i in range(8):
				b = b + str(port.value())
				sleep(constants.SLEEP_TIME - ((time.time()-t)))		
				t = time.time()
			total = total + str(b)
			
		return total

class Transmitter:
	global port
	def __init__(self, pin):
		global port
		port = Port(pin)
	
	def connect(self):
		global port
		port.transmit(0b1)
		sleep(constants.SLEEP_TIME/float(10))
		port.stop()
		sleep(constants.SLEEP_TIME/float(4.5))
		
	def transmitData(self, data):
		global port
		self.connect()	
		t = time.time()	
		total = ''
		for x in data:
			b = format(ord(x), '08b')
			total = total + b
			
			for c in b:
				port.transmit(c)
				sleep(constants.SLEEP_TIME - ((time.time()-t)))
				port.stop()
				t = time.time()
		return total