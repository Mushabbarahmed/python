def EncodeQR(pd_name):
    pad_binary = lambda s, length: '0' * (length - len(s)) + s

    encode_qr = ""
    for char in pd_name:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]  # Convert to binary, remove '0b' prefix
        # print(len(binary_value))
        print((binary_value))
        binary_value = pad_binary(binary_value, 8)  # Pad to 8 bits
        encode_qr += binary_value
    return (encode_qr)
