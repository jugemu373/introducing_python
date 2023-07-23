import struct
import unicodedata
import re
import binascii


# 12.1
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))


# 12.2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)


# 12.3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)


# 12.4
mammoth = """
We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from balloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.
"""


# 12.5
pat = r'\bc\w*'
print(re.findall(pat, mammoth))


# 12.6
pat = r'\bc\w{3}\b'
print(re.findall(pat, mammoth))


# 12.7
pat = r'\b\w*r\b'
print(re.findall(pat, mammoth))


# 12.8
pat = r'\b\w[aeiou]{3}[^aeiou\s]*\w*\b'
print(re.findall(pat, mammoth))


# 12.9
hex_str = '47494638396101000100800000000000ffffff21f9' + \
    '04010000000002c0000000001000100000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))


# 12.10
print(gif[:6] == b'GIF89a')


# 12.11
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)
