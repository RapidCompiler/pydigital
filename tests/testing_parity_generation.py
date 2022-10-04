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