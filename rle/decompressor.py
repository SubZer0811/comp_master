def decompress(filename,output_path):
    enc = open(filename, 'rb')
    dec = open(output_path+'decomp.txt', 'wb')

    count = int(enc.read(1).decode('utf-8'))
    item = enc.read(1)

    while count:
        # print(count)
        while count:
            dec.write(item)
            # print(item)
            count -= 1
        try:
            count = int(enc.read(1).decode('utf-8'))
            item = enc.read(1)
        except:
            break
    return output_path+'decomp.txt'