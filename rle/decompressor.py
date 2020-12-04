def decompress():
    enc = open("comp.txt", 'rb')
    dec = open('decomp.txt', 'wb')

    count = int(enc.read(1).decode('utf-8'))
    item = enc.read(1)

    while count:
        print(count)
        while count:
            dec.write(item)
            print(item)
            count -= 1
        try:
            count = int(enc.read(1).decode('utf-8'))
            item = enc.read(1)
        except:
            break