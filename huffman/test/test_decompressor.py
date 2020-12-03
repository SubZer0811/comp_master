from huffman import decompressor, compressor
import collections
import os
from helpers import utility


class TestDecompressor(object):
    ''' Test functions in decompress module '''

    def test_decompress(self):
        input_file = os.path.join(
            os.getcwd(), 'data', 'compressed', 'demo.huffman')
        output_path = os.path.join(os.getcwd(), 'data', 'uncompressed')
        output_file = decompressor.decompress(input_file, output_path)
        assert os.path.exists(output_file)
        assert os.path.isfile(output_file)
