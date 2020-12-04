import os

def compress(input_path):
    inp = open(input_path, 'rb')
    output_file = os.path.basename(input_path) + ".rle"
    out = open(output_file, 'wb')

    byte = inp.read(1)
    item = byte
    count = 0

    while byte:
        if(item == byte):
            count += 1
            if(count > 9):
                out.write(bytes(str(9), encoding='utf-8'))
                out.write(item)
                # print(9, item)
                count = 1
        else:
            out.write(bytes(str(count), encoding='utf-8'))
            out.write(item)
            # print(count, item)
            item = byte
            count = 1
        byte = inp.read(1)

    out.write(bytes(str(count), encoding='utf-8'))
    out.write(item)
    # print(count, item)

    out.close()
    inp.close()

    return output_file