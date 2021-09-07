#!/usr/bin/env python3

from pyftdi.spi import SpiController

my_spi = SpiController()

my_spi.configure('ftdi://ftdi:2232:FT4IKI36/2')
test_loop = my_spi.get_port(cs=0,freq=12E6, mode=0)

p = test_loop.exchange(b'Hello SPI',duplex=True)

print (p)


