# HELPER METHODS FOR PARITY GENERATION
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
