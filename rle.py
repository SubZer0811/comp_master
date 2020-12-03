def encode():
    inp = open("source.txt", 'rb')
    out = open("comp.txt", 'wb')

    byte = inp.read(1)
    item = byte
    count = 0

    while byte:
        if(item == byte):
            count += 1
            if(count > 9):
                out.write(bytes(str(9), encoding='utf-8'))
                out.write(item)
                print(9, item)
                count = 1
        else:
            out.write(bytes(str(count), encoding='utf-8'))
            out.write(item)
            print(count, item)
            item = byte
            count = 1
        byte = inp.read(1)

    out.write(bytes(str(count), encoding='utf-8'))
    out.write(item)
    print(count, item)

    out.close()
    inp.close()

def decode():
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

encode()
decode()