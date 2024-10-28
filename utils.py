"""
    Author: lefkovitj (https://lefkovitzj.github.io)
    File Last Modified: 10/27/2024
    Project Name: Python-64bit-signed-int-converter
    File Name: utils.py
"""

import math
import random
import sys

def dec_to_bin64s(dec_int):
    """ Convert a decimal value to a signed 64-bit integer returned as a string. """
    bin_str = ""

    sign_bit = "0"
    if dec_int < 0:
        sign_bit = "1"
        dec_int *= -1
    num_of_bits = math.ceil(math.log(dec_int, 2))
    for i in range(num_of_bits):
        remainder = dec_int % 2
        dec_int = int((dec_int - remainder)/2)
        bin_str = str(remainder) + bin_str
    for i in range(63-num_of_bits):
        bin_str = "0" + bin_str
    bin_str = sign_bit + bin_str
    return bin_str

def bin64s_to_dec(bin_str):
    """ Convert a signed 64-bit integer to a decimal value returned as an int. """
    bin64s_lenth = len(bin_str)
    assert bin64s_lenth == 64
    dec_int = 0
    sign_multiplier = -1 if bin_str[0] == "1" else 1
    rev_bin_str = bin_str[::-1]
    for bit_i in range(len(rev_bin_str)):
        bit = rev_bin_str[bit_i]
        if bit_i != 63:
            if bit == "1":
                dec_int += math.pow(2, (bit_i))

    dec_int = int(dec_int) * sign_multiplier
    return dec_int

def test_conversion(num_tests):
    """ Test the two functions  """
    print(f"Testing conversions {num_tests} times... ", end="")
    passes = 0
    fails = 0
    for i in range(num_tests):
        random_int = random.randint(-1000000000, 1000000000)
        bin64s = dec_to_bin64s(random_int)
        dec = bin64s_to_dec(bin64s)
        if dec != random_int:
            fails += 1
        else:
            passes += 1
    print("Done!\n")
    print(f">> {passes} tests passed.\n>> {fails} tests failed.\n\nConversion tests had a {passes/num_tests * 100}% success rate.")


if __name__ == "__main__":
    mode = ""
    while mode != "d" and mode != "t" and mode != "q":
        mode = input("Select an Action: [Demo (d), Test (t), Quit (q)]\n>> ").strip().lower()
    if mode == "d": # Demo.
        random_int = random.randint(-1000000000, 1000000000)
        bin64s = dec_to_bin64s(random_int)
        print(f"{random_int} <==> {bin64s}")
        print(f"{bin64s} <==> {bin64s_to_dec(bin64s)}")
    elif mode == "t": # Test.
        num_tests = int(input("Select a number of tests...\n>> "))
        test_conversion(num_tests)
    else: # Quit.
        sys.exit()