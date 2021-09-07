#!/usr/bin/env python3

import pyftdi.serialext

my_uart = pyftdi.serialext.serial_for_url('ftdi://ftdi:2232:FT4IHIJU/2',baudrate=3000000)

my_uart.write(b'Hello UART')
p=my_uart.read(10)

print (p)

