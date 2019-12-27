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
import struct
from enum import Enum

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
    _hdr_id = b"TXT1"
    _max_enc_n = 18

    @staticmethod
    def encode(
        self, 
        file: io.BufferedWriter,
        encoding: str= 'utf_8'
    ):
        file.write(self._hdr_id)
        file.write(struct.pack('b', self._enc_dict[encoding]))
        file.write(codecs.encode(string, encoding))
 
    @staticmethod
    def decode(file: io.BufferedReader):
        assert file.read(4) == self._hdr_id
        codec_id: int = struct.unpack('b', file.read(1))
        codec_name: str = None
 
        for name, id in self._enc_dict.items():
            if coded_id == id: enc_s = name
                
        if codec_name == None:
            raise Exception("Codec is undefined, cannot decode the file")
        return codecs.decode(file.read(), enc_s)
