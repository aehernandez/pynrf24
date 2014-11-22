from nrf24 import NRF24 
import time

pipes = [ [0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2] ]

radio = NRF24()
radio.begin(0,0,"P9_15", "P9_16") #Set CE and IRQ pins
radio.setRetries(15,15)
radio.setPayloadSize(8)

radio.setChannel(10)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.openWritingPipe(pipes[1])
radio.openReadingPipe(1,pipes[0])

radio.startListening()
radio.stopListening()

radio.printDetails()

buffer = ['P','I','N','G']
while True:
	status = radio.write(buffer)
	print("Writing %s with status %s" % (buffer,status))
	time.sleep(3)

