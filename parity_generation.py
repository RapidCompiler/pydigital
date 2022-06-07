def EncodeLRC(arr):
    # print(arr)
    lrc_parity = ""
    for j in range(len(arr[0])):
        parity_check = ''
        for i in range(len(arr)):
            parity_check += arr[i][j]
        lrc_parity += str(parity_check.count('1') % 2)
    return [lrc_parity, " ".join(arr) + " " + lrc_parity]


def EncodeVRC(arr):

    arr = list(map(parseItemEncodeVRC, arr))
    vrc_parity = "".join([item[-1] for item in arr])

    return [vrc_parity, " ".join(arr)]


def EncodeCRC(key, dataString):
    dataToAppend = '0' * (len(key) - 1)
    dividend = dataString + dataToAppend
    remainder = mod2div(dividend, key)
    return [remainder, dataString + remainder]


def EncodeChecksum(data1):
    # print("THIS IS DATA",data1)
    data = data1.copy()
    # data = list(map(int, data))
    remainderLen = len(data[0])
    while len(data) != 1:
        firstElem = data.pop(0)
        secondElem = data.pop(0)
        maxLen = max(len(firstElem), len(secondElem))
        firstNum = int(firstElem, 2)
        secondNum = int(secondElem, 2)
        # print(firstNum, secondNum)
        sum = firstNum + secondNum
        # print(sum)
        binSum = bin(sum)
        if len(binSum) - 2 != maxLen:
            # print("THIS IS LEN : ",len(binSum), maxLen)
            binSum = bin(int(binSum[2:-maxLen], 2) + int(binSum[-maxLen:], 2))
            
        data.insert(0, binSum[2:].zfill(remainderLen))
    # print(data)
    checksum = "".join(list(map(lambda x: '1' if x == '0' else '0', data[0])))
    # print(checksum)
    return [checksum, " ".join(data1) + " " + checksum]

# def DecodeLRC(arr):
#     lrc_parity = EncodeLRC(arr[:-1])[0]
#     # print(lrc_parity, arr[-1])
#     if arr[-1] == lrc_parity: return "THE DATA TRANSMITTED IS CORRECT"
#     return "THERE IS AN ERROR IN THE DATA"
    
    
# def DecodeVRC(arr):
#     vrc_parity_arr = "".join([dataString[-1] for dataString in arr])
#     newArr = [dataString[:-1] for dataString in arr]
#     vrc_parity = EncodeVRC(newArr)[0]
#     if vrc_parity_arr == vrc_parity:
#         return "THE DATA TRANSMITTED IS CORRECT"
#     return "THERE IS AN ERROR IN THE DATA"


# def DecodeCRC(key, dataString):
#     remainder = mod2div(dataString, key)
#     if not remainder.count('1'): return "THE DATA TRANSMITTED IS CORRECT"
#     return "THERE IS AN ERROR IN THE DATA"


# def DecodeChecksum(arr):
#     checksum = EncodeChecksum(arr)
#     # print(checksum)
#     if not checksum[0].count('1'): return "THE DATA TRANSMITTED IS CORRECT"
#     return "THERE IS AN ERROR IN THE DATA"
#     pass

def DecodeLRC(arr):
    lrc_parity = EncodeLRC(arr[:-1])[0]
    # print(lrc_parity, arr[-1])
    if arr[-1] == lrc_parity:
        print("DATA TRANSMITTED : "," ".join(arr[:-1]))
        return "THE DATA TRANSMITTED IS CORRECT"
    return "THERE IS AN ERROR IN THE DATA"
    
    
def DecodeVRC(arr):
    vrc_parity_arr = "".join([dataString[-1] for dataString in arr])
    newArr = [dataString[:-1] for dataString in arr]
    vrc_parity = EncodeVRC(newArr)[0]
    if vrc_parity_arr == vrc_parity:
        print("DATA TRANSMITTED : "," ".join(newArr))
        return "THE DATA TRANSMITTED IS CORRECT"
    return "THERE IS AN ERROR IN THE DATA"


def DecodeCRC(key, dataString):
    remainder = mod2div(dataString, key)
    if not remainder.count('1'):
        print("DATA TRANSMITTED : ","".join(dataString[:-(len(key)-1)]))
        return "THE DATA TRANSMITTED IS CORRECT"
    return "THERE IS AN ERROR IN THE DATA"


def DecodeChecksum(arr):
    checksum = EncodeChecksum(arr)
    # print(checksum)
    if not checksum[0].count('1'):
        print("DATA TRANSMITTED : "," ".join(arr[:-1]))
        return "THE DATA TRANSMITTED IS CORRECT"
    return "THERE IS AN ERROR IN THE DATA"
    pass


def parseItemEncodeVRC(item):
    parity_bit = str(item.count('1') % 2)
    item += parity_bit
    return item


def xor(a,b):
    result = []

    for i in range(1,len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    val = "".join(result)
    # print("THIS IS XOR : ", a, b, val)
    
    return val
    #return val.lstrip('0')


def mod2div(dividend, divisor):
    # print(dividend, divisor)
    pick = len(divisor)

    tmp = dividend[:pick]

    while pick < len(dividend):
        # print("THIS IS TEMP : ", tmp)
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]

        else:
            tmp = xor('0'* pick, tmp) + dividend[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)

    else:
        tmp = xor('0' * pick, tmp)

    return tmp


def TX():
    pass


def RX():
    pass


def main():
        
    input_validation = True
    input_count = False

    # RX or TX Choice
    choice = int(input("DO YOU WANT TO TRANSMIT OR RECEIVE DATA\n1. TRANSMIT\n2. RECEIVE\n\nYOUR CHOICE : "))
    print()

    # Error Detection Algorithm Choice
    while input_validation:
        option = input("WHICH ERROR DETECTION ALGORITHM DO YOU WANT TO USE?\n1. LRC\n2. VRC\n3. CRC\n4. CHECKSUM\n\nYOUR CHOICE : ")
        print()
        if option == '1' or option == '2' or option == '3' or option == '4': input_validation = not input_validation
        else: print("NON-EXISTENT OPTION! CHOOSE AGAIN")

    # Pre-defining input_count variable for RX and also for CRC and Checksum
    if option == '3' or choice == 2: input_count = 1

    # Data Input Count Block for TX (Applicable only to LRC and VRC)
    if not input_count:
        input_count = int(input("HOW MANY DATA STRINGS DO YOU WANT TO PROCESS? "))
        print()

    # Data Input Block for Transmission
    if choice == 1:
        data = []
        for i in range(input_count):
            a = input("ENTER INPUT DATA " + str(i+1) + " : ")
            print()
            data.append(a)

        data_lens = [len(data_string) for data_string in data]
        if len(set(data_lens)) > 1:
            print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS FOR LRC")
            input_validation = True
            
    # Data Input Block for Reception
    elif choice == 2:
        dataStream = input("ENTER THE RECEIVED DATA STREAM : ")
        if option == '1' or option == '2' or option == '4':
            bytes = int(input("ENTER THE NUMBER OF DATA STRINGS IN DATA STREAM : "))
            bits = int(input("ENTER THE NUMBER OF BITS IN EACH DATA STRING : "))
        if option == '2' and (len(dataStream) - int(bytes)) % bits or option == '1' and len(dataStream) != (bytes * bits) + bits: print("\nTHERE IS AN INCONSISTENCY IN THE DATA ENTERED\n", len(dataStream) - 1, bits); return

    
    print()

    # Encoding and Decoding Block Starts Here
    print("----------------------------------------------")
    if option == '1':
        # LRC TX
        if choice == 1:

            lrc = EncodeLRC(data)
            # print("----------------------------------------------")
            print("LRC :", lrc[0])
            print("DATA TRANSMITTED :", lrc[1])
            # print("----------------------------------------------")
        # LRC RX
        else:
            # Code to parse received data
            data = []
            pointer = 0
            while pointer + 1 <= bytes + 1:
                # print(pointer * bits, pointer + 1 * bits)
                dataString = dataStream[pointer * bits:(pointer + 1) * bits]
                data.append(dataString)
                pointer += 1
            
            lrc = DecodeLRC(data)
            print(lrc)
            
    if option == '2':
        # VRC TX
        if choice == 1:
            vrc = EncodeVRC(data)
            # print("----------------------------------------------")
            print("VRC :", vrc[0])
            print("DATA TRANSMITTED :", vrc[1])
            # print("----------------------------------------------")
        
        # VRC RX
        else:
            # Code to parse received data
            data = []
            pointer = 0
            while pointer + 1 <= bytes:
                dataString = dataStream[(pointer) * (bits + 1):(pointer + 1) * (bits + 1)]
                data.append(dataString)
                pointer += 1
            vrc = DecodeVRC(data)
            print(vrc)
    
    if option == '3':
        key = input("PLEASE ENTER POLYNOMIAL KEY FOR CRC : ")
        print()
        # CRC TX
        if choice == 1:
            crc = EncodeCRC(key, data[0])
            # print("----------------------------------------------")
            print("CRC :", crc[0])
            print("DATA TRANSMITTED :", crc[1])
            # print("----------------------------------------------")

        # CRC RX
        else:
            # Code to parse received data
            crc = DecodeCRC(key, dataStream)
            # print("----------------------------------------------")
            print(crc)

    if option == '4':
        if choice == 1:
            checksum = EncodeChecksum(data)
            print("CHECKSUM :", checksum[0])
            print("DATA TRANSMITTED :", checksum[1])

        else:
            data = []
            pointer = 0
            while pointer + 1 <= bytes + 1:
                dataString = dataStream[pointer * bits: (pointer + 1) * bits]
                data.append(dataString)
                pointer += 1
            # print(data)
            checksum = DecodeChecksum(data)
            print(checksum)

    print("----------------------------------------------")
    # Encoding and Decoding Block Ends Here
        
        # print()
        # option = input("TO EXIT,\nPRESS F TO KILL THE PROGRAM AND PAY RESPECTS f/(anything other than f): ")

        # if option in ['F', 'f']:
        #     print("PAYING RESPECTS....\nRESPECTS PAID")
        #     break
        
        # input_count = False
        # input_validation = True

main()

