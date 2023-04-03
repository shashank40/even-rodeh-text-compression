import logging
from even_rodeh_code import generate_even_rodeh_table, count_bits, encode_text


def run():
    text = "hello world"
    table = generate_even_rodeh_table()
    encoded_text, num_bits = encode_text(text, table)
    string_bits = count_bits(text)
    percentage = round((num_bits/string_bits) * 100,2)
    print(f"Original text: {text}")
    print(f"Encoded text: {encoded_text}")
    print(f"Number of bits in original text: {string_bits}")
    print(f"Number of bits in encoded text: {num_bits}")
    print("percentage compression = " + str(100-percentage) + "%")
    


run()