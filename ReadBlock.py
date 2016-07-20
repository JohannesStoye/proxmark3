#! /usr/bin/env python
from smartcard.Exceptions import NoCardException
from smartcard.System import readers
from smartcard.util import toHexString

# Rueckgabewerte bei Erfolg
SUCCESS = (0x90, 0x00)
# Blocknummer (0x00 - 0x3F) anpassen
BLK = 0x00
# mit 6 Bytes langem Key fuer Block ersetzen
KEY_0 = [0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5]

# APDU zum Laden des Keys in den Reader an Stelle 00h
LOAD_KEY_0 = [0xFF, 0x82, 0x00, 0x00, 0x06]
# APDU Teil a zum Laden der Keys
AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05]
# Teil b: Ver, 00h, Blockno, KeyTyp, Keyno
AUTH_DataBytes = [0x01, 0x00, BLK, 0x60, 0x00]
# APDU zum Lesen eines MF-Classic Blocks
READ_MFC = [0xFF, 0xB0, 0x00]

for reader in readers():
    try:
        connection = reader.createConnection()
        connection.connect()
        _, sw1, sw2 = connection.transmit( LOAD_KEY_0 + KEY_0 )
        assert SUCCESS == (sw1, sw2)
        _, sw1, sw2 = connection.transmit( AUTH + AUTH_DataBytes )
        assert SUCCESS == (sw1, sw2)
        for block in range(0,4):
            data, sw1, sw2 = connection.transmit( READ_MFC + [block, 16] )
            if SUCCESS != (sw1, sw2):
                print "Block", block, "nicht lesbar"
            else:
                print toHexString(data)
    except NoCardException:
        print reader, 'enthaelt keinen Tag'
