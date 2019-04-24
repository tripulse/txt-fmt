# MIT License

# Copyright (c) 2019 nullptr

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import codecs
import io

#  ——————  \  /  ——————
#    ||     \/     ||    
#    ||     /\     ||      \  / /|
#    ||    /  \    ||       \/   |
# Text Encoding v1 offical implementation in Python 3.
# See: txt1enc.github.com/structs for more information.

class TXT1:
    _enc_dict = {
        'ascii':       1,
        'cp037':       2,
        'utf_7':       4,
        'utf_8':       6,
        'utf_16':      8,
        'utf_32':      10,
        'utf_16_le':   12,
        'utf_16_be':   14,
        'utf_32_le':   16,
        'utf_32_be':   18
    }
    _hdr_id = "TXT1"
    _max_enc_n = 18

    def encode(
        self, 
        file: io.BufferedWriter, 
        string: str, 
        encoding: str= 'utf-8'
    ):

        # Write the header ID as an identifier.
        file.write( bytes(self._hdr_id, 'utf-8') )

        # Write the encoding of the file to parse.
        file.write( bytes(chr(self._enc_dit), 'utf-8') )

        # Encode the string in specified encoding.
        # Write the data as bytes. In the file.
        file.write( codecs.encode(string, encoding) )

    def decode(
        self, 
        file: io.BufferedReader
    ):
        # Identify that the file is a TXT1 file.
        # If it's not the process would stop here.
        assert file.read(4) == bytes(self._hdr_i, 'utf-8')

        # An integer depecting the encoding of text.
        enc_r: int = ord(file.read(1))

        # Encoding as string representation/name of the encoding.
        enc_n: int = None

        # If it's not a valid encoding format.
        if enc_r == 0 or enc_r > self._max_enc_n:
            raise ValueError("Not a valid encoding format.")

        # Picks an encoding based on the integer provided.
        for enc_n, e_id in self._enc_dict.items():
            if enc_r == e_id:
                enc_s = enc_n

        # Reads rest of the file and decodes it.
        # Sends this data as string.
        return codecs.decode(file.read(), enc_name)