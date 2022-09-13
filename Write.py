import sys
import time
import serial
import time
from datetime import datetime, date
import codecs
import re
from smartcard.System import readers
from smartcard.util import toHexString


class WriteC:

    def WC(self, mssv, name, lop):
        self.lop = lop
        self.mssv = mssv
        self.name = name
        try:
            #def WC(self, lop, mssv, name):
            self.inp= self.lop + '' + "|" + '' + self.mssv + '' + '|' + self.name
            self.Data=self.inp.encode('utf-8')
            self.Hex_Data=self.Data.hex()
            self.list_hex = re.split("(\w\w)", self.Hex_Data[:])[1::2]
            for i in range(48-len(self.list_hex)):
                self.list_hex.append('00')
            for i in range(48):
            #if i == 0:
                #list_hex[i] = '00'
                self.list_hex[i] = '0x'+ self.list_hex[i]
            #print(list_hex)
            #CaculateXOR
            self.lenl = 0x1a
            self.cmd = 0x38
            self.block4 = 0x04
            self.block5 = 0x05
            self.block6 = 0x06
            self.result = int(self.list_hex[0],16) ^ int(self.list_hex[1],16)

            for i in range(2,16,1):
                self.result = int(self.list_hex[i], 16) ^ self.result

            self.result = int(self.lenl) ^ self.result
            self.result = int(self.cmd) ^ self.result
            self.result = int(self.block4) ^ self.result

            self.result2 = int(self.list_hex[16],16) ^ int(self.list_hex[17],16)

            for i in range(18,32,1):
                self.result2 = int(self.list_hex[i], 16) ^ self.result2
            self.result2 = int(self.lenl) ^ self.result2
            self.result2 = int(self.cmd) ^ self.result2
            self.result2 = int(self.block5) ^ self.result2

            self.result3 = int(self.list_hex[32],16) ^ int(self.list_hex[33],16)

            for i in range(34,48,1):
                self.result3 = int(self.list_hex[i], 16) ^ self.result3

            self.result3 = int(self.lenl) ^ self.result3
            self.result3 = int(self.cmd) ^ self.result3
            self.result3 = int(self.block6) ^ self.result3

            self.WRITEKEY4command = bytearray()
            self.WRITEKEY4command.append(0x02)  # STX
            self.WRITEKEY4command.append(0x00)  # LEN-H
            self.WRITEKEY4command.append(0x1A)  # LEN-L
            self.WRITEKEY4command.append(0x38)  # CMD
            self.WRITEKEY4command.append(0x00)  # R-Mode
            self.WRITEKEY4command.append(0x00)  # A-Mode
            self.WRITEKEY4command.append(0x04)  # Block 4
            for i in range(6):  # Key0-5
                self.WRITEKEY4command.append(0xFF)
            self.WRITEKEY4command.append(int(self.list_hex[0],16))  # Data 0-15
            self.WRITEKEY4command.append(int(self.list_hex[1],16))
            self.WRITEKEY4command.append(int(self.list_hex[2],16))
            self.WRITEKEY4command.append(int(self.list_hex[3],16))
            self.WRITEKEY4command.append(int(self.list_hex[4],16))
            self.WRITEKEY4command.append(int(self.list_hex[5],16))
            self.WRITEKEY4command.append(int(self.list_hex[6],16))
            self.WRITEKEY4command.append(int(self.list_hex[7],16))
            self.WRITEKEY4command.append(int(self.list_hex[8],16))
            self.WRITEKEY4command.append(int(self.list_hex[9],16))
            self.WRITEKEY4command.append(int(self.list_hex[10],16))
            self.WRITEKEY4command.append(int(self.list_hex[11],16))
            self.WRITEKEY4command.append(int(self.list_hex[12],16))
            self.WRITEKEY4command.append(int(self.list_hex[13],16))
            self.WRITEKEY4command.append(int(self.list_hex[14],16))
            self.WRITEKEY4command.append(int(self.list_hex[15],16))
            self.WRITEKEY4command.append(self.result)  # LRC

            # Command no.38 for Block 5
            self.WRITEKEY5command = bytearray()
            self.WRITEKEY5command.append(0x02)  # STX
            self.WRITEKEY5command.append(0x00)  # LEN-H
            self.WRITEKEY5command.append(0x1A)  # LEN-L
            self.WRITEKEY5command.append(0x38)  # CMD
            self.WRITEKEY5command.append(0x00)  # R-Mode
            self.WRITEKEY5command.append(0x00)  # A-Mode
            self.WRITEKEY5command.append(0x05)  # Block 5
            for i in range(6):  # Key0-5
                self.WRITEKEY5command.append(0xFF)
            self.WRITEKEY5command.append(int(self.list_hex[16],16))  # Data 0-15
            self.WRITEKEY5command.append(int(self.list_hex[17],16))
            self.WRITEKEY5command.append(int(self.list_hex[18],16))
            self.WRITEKEY5command.append(int(self.list_hex[19],16))
            self.WRITEKEY5command.append(int(self.list_hex[20],16))
            self.WRITEKEY5command.append(int(self.list_hex[21],16))
            self.WRITEKEY5command.append(int(self.list_hex[22],16))
            self.WRITEKEY5command.append(int(self.list_hex[23],16))
            self.WRITEKEY5command.append(int(self.list_hex[24],16))
            self.WRITEKEY5command.append(int(self.list_hex[25],16))
            self.WRITEKEY5command.append(int(self.list_hex[26],16))
            self.WRITEKEY5command.append(int(self.list_hex[27],16))
            self.WRITEKEY5command.append(int(self.list_hex[28],16))
            self.WRITEKEY5command.append(int(self.list_hex[29],16))
            self.WRITEKEY5command.append(int(self.list_hex[30],16))
            self.WRITEKEY5command.append(int(self.list_hex[31],16))
            self.WRITEKEY5command.append(self.result2)  # LRC

            # Command no.38 for Block 6
            self.WRITEKEY6command = bytearray()
            self.WRITEKEY6command.append(0x02)  # STX
            self.WRITEKEY6command.append(0x00)  # LEN-H
            self.WRITEKEY6command.append(0x1A)  # LEN-L
            self.WRITEKEY6command.append(0x38)  # CMD
            self.WRITEKEY6command.append(0x00)  # R-Mode
            self.WRITEKEY6command.append(0x00)  # A-Mode
            self.WRITEKEY6command.append(0x06)  # Block 6
            for i in range(6):  # Key0-5
                self.WRITEKEY6command.append(0xFF)
            self.WRITEKEY6command.append(int(self.list_hex[32],16))  # Data 0-15
            self.WRITEKEY6command.append(int(self.list_hex[33],16))
            self.WRITEKEY6command.append(int(self.list_hex[34],16))
            self.WRITEKEY6command.append(int(self.list_hex[35],16))
            self.WRITEKEY6command.append(int(self.list_hex[36],16))
            self.WRITEKEY6command.append(int(self.list_hex[37],16))
            self.WRITEKEY6command.append(int(self.list_hex[38],16))
            self.WRITEKEY6command.append(int(self.list_hex[39],16))
            self.WRITEKEY6command.append(int(self.list_hex[40],16))
            self.WRITEKEY6command.append(int(self.list_hex[41],16))
            self.WRITEKEY6command.append(int(self.list_hex[42],16))
            self.WRITEKEY6command.append(int(self.list_hex[43],16))
            self.WRITEKEY6command.append(int(self.list_hex[44],16))
            self.WRITEKEY6command.append(int(self.list_hex[45],16))
            self.WRITEKEY6command.append(int(self.list_hex[46],16))
            self.WRITEKEY6command.append(int(self.list_hex[47],16))
            self.WRITEKEY6command.append(self.result3)  # LRC


                # initialize serial python, framework for reading serial USB
            ser = serial.Serial(
                port="COM3",
                baudrate=115200,
                timeout=0.05)

                # print(f"valid check readable: {ser.readable()}, writeable: {ser.writable()}")

            #while (True):
                #command = input("Please insert 1 of following commands:\n"
                                    #"- rk4: read block 4 of Mifare card with Key included\n")
                        #inp = input("Nhap du lieu: \n").encode('utf-8')
                #if command == "writekey":
            ser.write(self.WRITEKEY4command)
            print("Now write key 4")
            in_hexB4 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                            #print(f"list hex B4 {in_hexB4}")
                            #print(f"command4 {WRITEKEY4command}")
                            #print(in_hexB4[2:9])
            if in_hexB4[2:9] == '2000500':
                print("Now write key 5")
                ser.write(self.WRITEKEY5command)
                in_hexB5 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                                    #print(f"list hex {in_hexB5}")
                if in_hexB5[2:9] == '2000500':
                    print("Now write key 6")
                    ser.write(self.WRITEKEY6command)
                    in_hexB6 = hex(int.from_bytes(ser.read(size=32), byteorder='big'))
                    if in_hexB6[2:9] == '2000500':
                        ser.write(self.BUZZ2command)
                        time.sleep(0.15)
                        ser.write(self.BUZZ3command)
        except:
            card_present = False
            r = readers()
            try:
                connection = r[0].createConnection()
                connection.connect()
                card_present = True
            except:
                connection = r[1].createConnection()
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

                    self.inp= self.lop + '' + "|" + '' + self.mssv + '' + '|' + self.name
                    Data = self.inp.encode('utf-8')
                    Hex_Data = Data.hex()
                    list_hex = re.split("(\w\w)", Hex_Data[:])[1::2]
                    for i in range(48 - len(list_hex)):
                        list_hex.append('00')
                    for i in range(48):
                        # if i == 0:
                        # list_hex[i] = '00'
                        list_hex[i] = '0x' + list_hex[i]
                    #print(list_hex)

                    print("Now write block 4")
                    WRITE4 = [0xFF, 0xD6, 0x00, 0x04, 0x10, int(list_hex[0], 16), int(list_hex[1], 16),
                            int(list_hex[2], 16), int(list_hex[3], 16), int(list_hex[4], 16), int(list_hex[5], 16),
                            int(list_hex[6], 16), int(list_hex[7], 16), int(list_hex[8], 16), int(list_hex[9], 16),
                            int(list_hex[10], 16), int(list_hex[11], 16), int(list_hex[12], 16), int(list_hex[13], 16),
                            int(list_hex[14], 16), int(list_hex[15], 16)]
                    card_response = connection.transmit(WRITE4)
                    #print(card_response[1])
                    if card_response[1] == 144:
                        print("Now write block 5")
                        WRITE5 = [0xFF, 0xD6, 0x00, 0x05, 0x10, int(list_hex[16], 16), int(list_hex[17], 16),
                                    int(list_hex[18], 16), int(list_hex[19], 16), int(list_hex[20], 16), int(list_hex[21], 16),
                                    int(list_hex[22], 16), int(list_hex[23], 16), int(list_hex[24], 16), int(list_hex[25], 16),
                                    int(list_hex[26], 16), int(list_hex[27], 16), int(list_hex[28], 16), int(list_hex[29], 16),
                                    int(list_hex[30], 16), int(list_hex[31], 16)]
                        card_response = connection.transmit(WRITE5)
                        if card_response[1] == 144:
                            print("Now write block 6")
                            WRITE6 = [0xFF, 0xD6, 0x00, 0x06, 0x10, int(list_hex[32], 16), int(list_hex[33], 16),
                                            int(list_hex[34], 16), int(list_hex[35], 16), int(list_hex[36], 16), int(list_hex[37], 16),
                                            int(list_hex[38], 16), int(list_hex[39], 16), int(list_hex[40], 16), int(list_hex[41], 16),
                                            int(list_hex[42], 16), int(list_hex[43], 16), int(list_hex[44], 16), int(list_hex[45], 16),
                                            int(list_hex[46], 16), int(list_hex[47], 16)]
                            card_response = connection.transmit(WRITE6)
                            BUZZ = [0xFF, 0x00, 0x04, 0x01, 0x03, 0x19, 0x19, 0x02]
                            card_response = connection.transmit(BUZZ)
                            # print(f"write res: if sw1 is 144 then is correct: {card_response}")
                except:
                    return "cant write data"
            time.sleep(3)

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
            # Command no.38 for Block 4

if __name__ == "__main__":
     WriteC().WC()