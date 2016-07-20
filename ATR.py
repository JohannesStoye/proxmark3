#! /usr/bin/env python
"""
Sample script that displays the ATR of inserted cards.

__author__ = "http://www.gemalto.com"

Copyright 2001-2012 gemalto
Author: Jean-Daniel Aussel, mailto:jean-daniel.aussel@gemalto.com
Copyright 2010 Ludovic Rousseau
Author: Ludovic Rousseau, mailto:ludovic.rousseau@free.fr

This file is part of pyscard.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from smartcard.Exceptions import NoCardException
from smartcard.System import readers
from smartcard.util import toHexString

SUCCESS = (0x90, 0x00)

SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
DF_TELECOM = [0x7F, 0x10]

GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x04]

#KEY_0 = [0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5]
KEY_0 = [0x00, 0x09, 0x25, 0x00, 0x0, 0x05]
LOAD_KEY_0 = [0xFF, 0x82, 0x00, 0x00, 0x06]
LOAD_KEY_1 = [0xFF, 0x82, 0x00, 0x01, 0x06]

AUTH_A_0 = [0xFF, 0x86, 0x00, 0x00, 0x05]
AUTH_A_0_DataBytes = [0x01, 0x00, 0x00, 0x60, 0x00]

READ_MFC = [0xFF, 0xB0, 0x00]
BLK_0 = 0x00
BLK_1 = 0x01
BLK_2 = 0x02
BLK_3 = 0x03

for reader in readers():
    try:
        connection = reader.createConnection()
        connection.connect()

        print reader, toHexString(connection.getATR())

        #data, sw1, sw2 = connection.transmit( SELECT + DF_TELECOM )
        #print "%x %x" % (sw1, sw2)

        data, sw1, sw2 = connection.transmit( GET_UID )
        print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS

        data, sw1, sw2 = connection.transmit( LOAD_KEY_0 + KEY_0 )
        #print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS

        data, sw1, sw2 = connection.transmit( AUTH_A_0 + AUTH_A_0_DataBytes )
        #print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS

        data, sw1, sw2 = connection.transmit( READ_MFC + [BLK_0, 16] )
        print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS
        data, sw1, sw2 = connection.transmit( READ_MFC + [BLK_1, 16] )
        print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS
        data, sw1, sw2 = connection.transmit( READ_MFC + [BLK_2, 16] )
        print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS
        data, sw1, sw2 = connection.transmit( READ_MFC + [BLK_3, 16] )
        print data, ": %x %x" % (sw1, sw2), (sw1, sw2) == SUCCESS
    except NoCardException:
        print reader, 'no card inserted'

import sys
if 'win32' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)
