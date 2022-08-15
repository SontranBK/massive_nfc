import serial
import sys
import time
from datetime import datetime, date
import codecs
import re
class ReadKey:
    def __init__(self):
        self.BUZZ2command = bytearray()
        self.BUZZ2command.append(0x02)  # STX
        self.BUZZ2command.append(0x00)  # LEN-H
        self.BUZZ2command.append(0x02)  # LEN-L
        self.BUZZ2command.append(0x13)  # BUZZ2 CMD
        self.BUZZ2command.append(0x00)  # BUZZ2 On
        self.BUZZ2command.append(0x11)  # LRC

        self.BUZZ3command = bytearray()
        self.BUZZ3command.append(0x02)  # STX
        self.BUZZ3command.append(0x00)  # LEN-H
        self.BUZZ3command.append(0x02)  # LEN-L
        self.BUZZ3command.append(0x13)  # BUZZ3 CMD
        self.BUZZ3command.append(0x01)  # BUZZ3 Off
        self.BUZZ3command.append(0x10)  # LRC
    # Command no.36 for block 4
        self.READKEY4command = bytearray()
        self.READKEY4command.append(0x02)  # STX
        self.READKEY4command.append(0x00)  # LEN-H
        self.READKEY4command.append(0x0A)  # LEN-L
        self.READKEY4command.append(0x36)  # REQA CMD
        self.READKEY4command.append(0x00)  # R mode
        self.READKEY4command.append(0x00)  # A mode
        self.READKEY4command.append(0x04)  # Block number of the card
        for i in range(6):
            self.READKEY4command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
        self.READKEY4command.append(0x38)  # LRC

    # Command no.36 for block 5
        self.READKEY5command = bytearray()
        self.READKEY5command.append(0x02)  # STX
        self.READKEY5command.append(0x00)  # LEN-H
        self.READKEY5command.append(0x0A)  # LEN-L
        self.READKEY5command.append(0x36)  # REQA CMD
        self.READKEY5command.append(0x00)  # R mode
        self.READKEY5command.append(0x00)  # A mode
        self.READKEY5command.append(0x05)  # Block number of the card
        for i in range(6):
            self.READKEY5command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
        self.READKEY5command.append(0x39)  # LRC

    # Command no.36 for block 6
        self.READKEY6command = bytearray()
        self.READKEY6command.append(0x02)  # STX
        self.READKEY6command.append(0x00)  # LEN-H
        self.READKEY6command.append(0x0A)  # LEN-L
        self.READKEY6command.append(0x36)  # REQA CMD
        self.READKEY6command.append(0x00)  # R mode
        self.READKEY6command.append(0x00)  # A mode
        self.READKEY6command.append(0x06)  # Block number of the card
        for i in range(6):
            self.READKEY6command.append(0xFF)  # Key[0]..[5], The key data to be stored into the secret key buffer
        self.READKEY6command.append(0x3a)  # LRC
    def RKey(self):
        # initialize serial python, framework for reading serial USB
        ser = serial.Serial(
            port="COM3",
            baudrate=115200,
            timeout=0.05)

        # print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")
        while (True):
                try:
                    dataB4 = ""
                    dataB5 = ""
                    dataB6 = ""
                    ser.write(self.READKEY4command)
                    in_hexB4 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                    print(in_hexB4)
                    print (in_hexB4[2:9])
                    if in_hexB4[2:9] == '2001500':
                        dataB4 = str(codecs.decode(in_hexB4[17:49], "hex"), 'utf-8')
                        ser.write(self.READKEY5command)
                        in_hexB5 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                        if in_hexB5[2:9] == '2001500':
                            dataB5 = dataB4 + str(codecs.decode(in_hexB5[17:49], "hex"), 'utf-8')
                            ser.write(self.READKEY6command)
                            in_hexB6 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                            if in_hexB6[2:9] == '2001500':
                                dataB6 = dataB5 + str(codecs.decode(in_hexB6[17:49], "hex"), 'utf-8')
                                print(f"data: {dataB6}")
                                ser.write(self.BUZZ2command)
                                time.sleep(0.15)
                                ser.write(self.BUZZ3command)
                            try:
                                class_name = dataB6[:dataB6.index("|")]
                                rest = dataB6[dataB6.index("|") + 1:]
                                student_id = rest[:rest.index("|")]
                                # print(f"class name: {class_name}; student ID: {student_id}")
                                return class_name, student_id
                            except:
                                return "Wrong data format"
                except:
                    return "Hexa not valid"

