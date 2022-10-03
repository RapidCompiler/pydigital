# Encodes an array of binary numbers using LRC
def EncodeLRC(arr):
    arrElemLen = arrElemLenCheck(arr)
    if not arrElemLen[0]:
        print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS FOR LRC")
        raise ValueError("Entered data has inconsistent number of bits for LRC. All data strings must contain the same number of bits")

    lrc_parity = ""
    for j in range(arrElemLen[1]):
        lrc_parity += str(parityCalculator(arr, j))

    return [lrc_parity, " ".join(arr) + " " + lrc_parity]

# Encodes an array of binary numbers using VRC
def EncodeVRC(arr):
    # Check if all elements of same size
    arrElemLen = arrElemLenCheck(arr)
    if not arrElemLen[0]:
        print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS FOR VRC")
        raise ValueError("Entered data has inconsistent number of bits for VRC. All data strings must contain the same number of bits")

    # Calculate parity for each data string and append to item
    arr = list(map(parityCalculator, arr))
    
    # Getting the VRC bits alone
    vrc_parity = "".join([item[-1] for item in arr])

    # Returning the final VRC transmitted string and VRC bits
    return [vrc_parity, " ".join(arr)]

# Encodes a dataString using CRC with a key
def EncodeCRC(dataStream, key):
    dataToAppend = '0' * (len(key) - 1)
    dividend = dataStream + dataToAppend
    remainder = mod2div(dividend, key)
    return [remainder, dataStream + remainder]

# Encodes a array of binary numbers using Checksum technique
def EncodeChecksum(dataArr):
    dataArrCopy = dataArr.copy()
    remainderLen = len(dataArrCopy[0])
    
    while len(dataArrCopy) != 1:
        # Using an array as a stack
        firstElem = dataArrCopy.pop(0)
        secondElem = dataArrCopy.pop(0)
        maxLen = max(len(firstElem), len(secondElem))

        # Converting binary number to decimal integer
        firstNum = int(firstElem, 2)
        secondNum = int(secondElem, 2)

        # Summing up the numbers and converting sum to binary
        sum = firstNum + secondNum
        binSum = bin(sum)

        # Adding binary numbers
        if len(binSum) - 2 != maxLen:
            binSum = bin(int(binSum[2:-maxLen], 2) + int(binSum[-maxLen:], 2))
            
        dataArrCopy.insert(0, binSum[2:].zfill(remainderLen))

    checksum = "".join(list(map(lambda x: '1' if x == '0' else '0', dataArrCopy[0])))
    return [checksum, " ".join(dataArr) + " " + checksum]

# Decodes an LRC binary dataStream given the number of data strings and the number of bits per data string
def DecodeLRC(dataStream, bits, bytes, retType=0):
    dataStream = dataStream.replace(" ", "")
    # Create array of data strings from dataStream
    arr = arrGen4VRCLRCChecksum(dataStream, bits, bytes)

    # No need to calculate LRC bit string here because it is already available in the last element of arr
    # Calculating LRC parity using EncodeLRC function
    lrc_parity = EncodeLRC(arr[:-1])[0]

    # Checking if parity bits are correct
    if arr[-1] == lrc_parity:
        return ReturnArgument(True, retType, " ".join(arr[:-1]))
    
    return ReturnArgument(False, retType)
    
# Decodes a VRC binary dataStream given the number of data strings and the number of bits per data string
def DecodeVRC(dataStream, bits, bytes, retType=0):
    dataStream = dataStream.replace(" ", "")

    # Create array of data strings from dataStream
    arr = arrGen4VRCLRCChecksum(dataStream, bits, bytes, True)

    # Create VRC bit string
    vrc_parity_arr = "".join([dataString[-1] for dataString in arr])
    dataArr = [dataString[:-1] for dataString in arr]

    # Calculating VRC parity using EncodeVRC function
    vrc_parity = EncodeVRC(dataArr)[0]

    # Checking if parity bits are correct
    if vrc_parity_arr == vrc_parity:
        return ReturnArgument(True, retType, " ".join(dataArr))

    return ReturnArgument(False, retType)

# Decodes a CRC binary dataStream given the number of data strings and the number of bits per data string
def DecodeCRC(dataStream, key, retType=0):
    dataStream = dataStream.replace(" ", "")
    remainder = mod2div(dataStream, key)

    if not remainder.count('1'):
        return ReturnArgument(True, retType, "".join(dataStream[:-(len(key)-1)]))        

    return ReturnArgument(False, retType)

# Decodes a Checksum binary dataStream given the number of data strings and the number of bits per data string
def DecodeChecksum(dataStream, bits, bytes, retType=0):
    dataStream = dataStream.replace(" ", "")
    arr = arrGen4VRCLRCChecksum(dataStream, bits, bytes)

    checksum = EncodeChecksum(arr)
    if not checksum[0].count('1'):
        return ReturnArgument(True, retType, " ".join(arr[:-1]))

    return ReturnArgument(False, retType)

# Generate array for VRC and Checksum decoding
def arrGen4VRCLRCChecksum(dataStream, bits, bytes, flag=False):

    arr = []

    pointer = 0
    upperPointer = bytes if flag else bytes + 1
    while pointer + 1 <= upperPointer:
        newElem = dataStream[(pointer) * (bits + 1):(pointer + 1) * (bits + 1)] if flag else dataStream[pointer * bits:(pointer + 1) * bits]
        arr.append(newElem)
        pointer += 1

    return arr

# Checks if all elements of an array have the same length
def arrElemLenCheck(arr):
    # Retrieving a list of array element sizes.
    data_lens = set(map(len, arr))

    # Set length must be one as there must be only one size
    if len(data_lens) > 1:
        return [False]

    # Returning the length of the data streams
    return [True, data_lens.pop()]

# Calculates the LRC and VRC parity bits
def parityCalculator(item, j=None):
    # j variable is used for column number in LRC
    parity_bit = 0
    
    for i in range(len(item)):
        newItem = int(item[i][j]) if j != None else int(item[i])
        parity_bit = parity_bit ^ newItem

    if j == None:
        return item + str(parity_bit)
    return parity_bit

# Outputs the xor of two binary data strings A and B
def xor(a,b):
    result = []

    for i in range(1,len(b)):
        result.append(str(int(a[i]) ^ int(b[i])))

    return "".join(result)

# Modulo 2 division function used for CRC bits calculation
def mod2div(dividend, divisor):
    pick = len(divisor)

    tmp = dividend[:pick]

    while pick < len(dividend):
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

# Helper function to generate appropriate return values based on input retType
def ReturnArgument(status, retType, data=None):
    if status and data:
        if retType == 0:
            return True
        elif retType == 1:
            return data
        elif retType == 2:
            return "THE DATA TRANSMITTED IS CORRECT"
    elif not status and not data:
        if retType == 0:
            return False
        else:
            return "THERE IS AN ERROR IN THE DATA"

# Main function
def main():
    
    lrc = EncodeLRC(['10110', '10100'])
    print("LRC :", lrc[0])
    print("DATA TRANSMITTED :", lrc[1])

    lrc = DecodeLRC('10110 10100 00010', 5, 2, 0)
    print(lrc)
    

    vrc = EncodeVRC(['10110', '10100'])
    print("VRC :", vrc[0])
    print("DATA TRANSMITTED :", vrc[1])
            
    vrc = DecodeVRC('101101 101001', 5, 2, 2)
    print(vrc)
    

    crc = EncodeCRC('100100', '1101')
    print("CRC :", crc[0])
    print("DATA TRANSMITTED :", crc[1])

    crc = DecodeCRC('100100001', '1101', 0)
    print(crc)


    checksum = EncodeChecksum(['11001100', '10101010', '11110000', '11000011'])
    print("CHECKSUM :", checksum[0])
    print("DATA TRANSMITTED :", checksum[1])

    checksum = DecodeChecksum('11001100 10101010 11110000 11000011 11010011', 8, 4, 2)
    print(checksum)

main()