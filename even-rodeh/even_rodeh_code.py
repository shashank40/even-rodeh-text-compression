import heapq
from collections import Counter
from typing import List, Tuple

from even_rodeh_table import evenRodeh_table

def generate_even_rodeh_table() -> List[str]:
    table = evenRodeh_table()
    return table

def sort_chars_by_frequency(text: str) -> List[Tuple[str, int]]:
    # count frequency of each character
    freq = Counter(text)
    # sort characters by frequency and alphabetically
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_chars

def encode_text(text: str, table: List[str]) -> Tuple[str, int]:
    # create a dictionary to map each character to its even-rodeh code
    char_codes = {char: table[i] for i, char in enumerate(sorted(set(text)))}
    # encode the text using even-rodeh codes
    encoded_text = "".join(char_codes[char] for char in text)
    # add padding bits according to the even-rodeh compression rules
    padding_bits = ""
    if len(encoded_text) % 8 == 0:
        padding_bits = "00000001"
    else:
        n = len(encoded_text) % 8
        padding_bits = "0" * (7 - n + 1) + bin(9 - n)[2:].zfill(3)
    encoded_text += padding_bits
    # convert the encoded text to bytes and return
    return ("".join([chr(int(encoded_text[i:i+8], 2)) for i in range(0, len(encoded_text), 8)]), len(encoded_text))


def count_bits(string):
    """
    This function counts the number of bits in a string
    """
    # Convert the string to binary representation
    binary_string = ''.join(format(ord(char), '08b') for char in string)
    
    # Return the length of the binary string
    return len(binary_string)

def even_rodeh_decompress(compressed_text):
    # Convert compressed text to binary form
    binary_text = ''
    for c in compressed_text:
        binary_text += bin(ord(c))[2:].zfill(8)
    
    # Read last 8 bits as decimal number to get n
    n = int(binary_text[-8:], 2)
    
    # Remove last 8 bits + n bits from the binary text
    binary_text = binary_text[:-8-n]
    
    # Convert binary text back to the original string
    decompressed_text = ''
    while binary_text:
        if binary_text.startswith('00'):
            # If the binary starts with '00', read the next 3 bits and convert it to decimal number
            num_bits = int(binary_text[2:5], 2)
            decompressed_text += chr(int(binary_text[5:5+num_bits], 2))
            binary_text = binary_text[5+num_bits:]
        else:
            # If the binary does not start with '00', read the next 8 bits and convert it to decimal number
            decompressed_text += chr(int(binary_text[:8], 2))
            binary_text = binary_text[8:]
    
    return decompressed_text