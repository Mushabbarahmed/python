def EncodeQR(pd_name):
    pad_binary = lambda s, length:"1"+ "0" * (length) + s

    encode_qr = ""
    for char in pd_name:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]  #  remove 0b
        # print(len(binary_value))
        print((binary_value))
        binary_value = pad_binary(binary_value, 8)
        encode_qr += binary_value
    return (encode_qr)
