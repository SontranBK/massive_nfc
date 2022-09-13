import serial
import sys
import time
from datetime import datetime, date
import codecs
import re
from smartcard.System import readers
from smartcard.util import toHexString

class ReadKey:
    def RKey(self):
        try:
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
        except:
            card_present = False    
            r = readers()
            try:     
                connection = r[0].createConnection()
                #print(connection)
                connection.connect()
                card_present = True
            except:
                connection = r[1].createConnection()
                #print(connection)
                connection.connect()
                card_present = True  
            
            if card_present == True:
                try:
                    LOADKEY = [0xFF, 0x82, 0x00, 0x00, 0x06, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                    card_response = connection.transmit(LOADKEY)
                #print(f"loadkey res: if sw1 is 144 then is correct: {card_response}")

                    AUTH = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x04, 0x60, 0x00]
                    card_response = connection.transmit(AUTH)
                #print(f"auth res: if sw1 is 144 then is correct: {card_response[2]}")

                    READ4 = [0xFF, 0xb0, 0x00, 0x04, 0x10]
                    card_response = connection.transmit(READ4)
                #print(f"read4 res: if sw1 is 144 then is correct: {card_response}")
                #print(type(card_response[0]))
                    DATA4 = card_response[0]
                    if card_response[1] == 144:
                        READ5 = [0xFF, 0xb0, 0x00, 0x05, 0x10]
                        card_response = connection.transmit(READ5)
                    #print(f"read5 res: if sw1 is 144 then is correct: {card_response}")
                        DATA5 = card_response[0]
                    if card_response[1] == 144:
                        READ6 = [0xFF, 0xb0, 0x00, 0x06, 0x10]
                        card_response = connection.transmit(READ6)
                        #print(f"read6 res: if sw1 is 144 then is correct: {card_response}")
                        DATA6 = card_response[0]
                    if card_response[1] == 144:
                        DATA = DATA4 + DATA5 + DATA6
                        #print(type(DATA[0]))
                        DATA0 = []
                        for i in range (0,47,1):
                            DATA0.append(chr(DATA[i]))
                        #print(DATA0)
                        strDATA = "".join(DATA0)
                        for i in range(len(strDATA)):
                            if strDATA[i] == "|": 
                                count = i
                                data_0 = strDATA[0:count]
                                break
                        for i in range(len(strDATA)):
                            if strDATA[i] == "|":
                                count1 = i
                                data_1 = strDATA[count+1:count1]
                        mytuple = (data_0,data_1) 
                        return mytuple
                        BUZZ = [0xFF, 0x00, 0x04, 0x01, 0x03, 0x19, 0x19, 0x02]
                        card_response = connection.transmit(BUZZ)
                        #print(f"write res: if sw1 is 144 then is correct: {card_response}")
                except: 
                    return
            time.sleep(1.5)
    
    
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

        