from . import utils

class ParityEncDec:
    # Encodes an array of binary numbers using LRC
    def encode_lrc(self, dataArr):
        arrElemLen = utils.arrElemLenCheck(dataArr)
        if not arrElemLen[0]:
            print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS FOR LRC")
            raise ValueError("Entered data has inconsistent number of bits for LRC. All data strings must contain the same number of bits")

        lrc_parity = ""
        for j in range(arrElemLen[1]):
            lrc_parity += str(utils.parityCalculator(dataArr, j))

        return [lrc_parity, " ".join(dataArr) + " " + lrc_parity]

    # Encodes an array of binary numbers using VRC
    def encode_vrc(self, dataArr):
        # Check if all elements of same size
        arrElemLen = utils.arrElemLenCheck(dataArr)
        if not arrElemLen[0]:
            print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS FOR VRC")
            raise ValueError("Entered data has inconsistent number of bits for VRC. All data strings must contain the same number of bits")

        # Calculate parity for each data string and append to item
        dataArr = list(map(utils.parityCalculator, dataArr))
        
        # Getting the VRC bits alone
        vrc_parity = "".join([item[-1] for item in dataArr])

        # Returning the final VRC transmitted string and VRC bits
        return [vrc_parity, " ".join(dataArr)]

    # Encodes a dataString using CRC with a key
    def encode_crc(self, dataStream, key):
        dataToAppend = '0' * (len(key) - 1)
        dividend = dataStream + dataToAppend
        remainder = utils.mod2div(dividend, key)
        return [remainder, dataStream + remainder]

    # Encodes a array of binary numbers using Checksum technique
    def encode_checksum(self, dataArr):
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
    def decode_lrc(self, dataStream, bits, bytes, retType=0):
        dataStream = dataStream.replace(" ", "")
        # Create array of data strings from dataStream
        arr = utils.arrGen4VRCLRCChecksum(dataStream, bits, bytes)

        # No need to calculate LRC bit string here because it is already available in the last element of arr
        # Calculating LRC parity using EncodeLRC function
        lrc_parity = self.encode_lrc(arr[:-1])[0]

        # Checking if parity bits are correct
        if arr[-1] == lrc_parity:
            return utils.ReturnArgument(True, retType, " ".join(arr[:-1]))
        
        return utils.ReturnArgument(False, retType)
        
    # Decodes a VRC binary dataStream given the number of data strings and the number of bits per data string
    def decode_vrc(self, dataStream, bits, bytes, retType=0):
        dataStream = dataStream.replace(" ", "")

        # Create array of data strings from dataStream
        arr = utils.arrGen4VRCLRCChecksum(dataStream, bits, bytes, True)

        # Create VRC bit string
        vrc_parity_arr = "".join([dataString[-1] for dataString in arr])
        dataArr = [dataString[:-1] for dataString in arr]

        # Calculating VRC parity using EncodeVRC function
        vrc_parity = self.encode_vrc(dataArr)[0]

        # Checking if parity bits are correct
        if vrc_parity_arr == vrc_parity:
            return utils.ReturnArgument(True, retType, " ".join(dataArr))

        return utils.ReturnArgument(False, retType)

    # Decodes a CRC binary dataStream given the number of data strings and the number of bits per data string
    def decode_crc(self, dataStream, key, retType=0):
        dataStream = dataStream.replace(" ", "")
        remainder = utils.mod2div(dataStream, key)

        if not remainder.count('1'):
            return utils.ReturnArgument(True, retType, "".join(dataStream[:-(len(key)-1)]))        

        return utils.ReturnArgument(False, retType)

    # Decodes a Checksum binary dataStream given the number of data strings and the number of bits per data string
    def decode_checksum(self, dataStream, bits, bytes, retType=0):
        dataStream = dataStream.replace(" ", "")
        arr = utils.arrGen4VRCLRCChecksum(dataStream, bits, bytes)

        checksum = self.encode_checksum(arr)
        if not checksum[0].count('1'):
            return utils.ReturnArgument(True, retType, " ".join(arr[:-1]))

        return utils.ReturnArgument(False, retType)

