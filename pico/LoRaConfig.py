
class LoRaConfig:
    '''
    Utility class to store required parameters for LoRaWAN connection
    All values are stored in MSB byte order
    '''
    # ABP
    DevAddrABP = [0x26, 0x01, 0x11, 0x5f]
    NwkSKeyABP = [0xc3, 0x24, 0x64, 0x98, 0xde, 0x56, 0x5d, 0x8c, 0x55, 0x88, 0x7c, 0x05, 0x86, 0xf9, 0x82, 0x26]
    AppSKeyABP = [0x15, 0xf6, 0xf4, 0xd4, 0x2a, 0x95, 0xb0, 0x97, 0x53, 0x27, 0xb7, 0xc1, 0x45, 0x6e, 0xc5, 0x45]

    # OTAA
    DevEUI = [0x01, 0x69, 0x04, 0xb1, 0xce, 0x46, 0x57, 0x7e]
    JoinEUI = [0x18, 0x90, 0x2d, 0x2f, 0xa5, 0xb6, 0xc5, 0x89]
    AppKey = [0x83, 0x42, 0x34, 0x94, 0xba, 0xa2, 0x66, 0x2d, 0xd2, 0xfd, 0x89, 0x8a, 0xc0, 0x27, 0x06, 0x4c]

