# Cryptography related functions.
from crypto_numbertheory import *

# ---------------------------------------------------------------------------
#                       Bits n Bytes of Information
# ---------------------------------------------------------------------------

# This function takes plaintext (type str) and outputs the list of bytes
# which encode that plaintext (type str) i.e. list of binary bytes.
def text_to_bytes(plaintext):

    """
        This function takes plaintext (type str) and returns the corresponding
        list of bytes.

        Recall: Byte = 8-bits. This function accounts for this by padding the
                binary encodins from the ASCII integers.

    """

    plaintext = list(plaintext)

    # ord function gives the ASCII (unicode) integer for the character in the
    # plain text...
    plaintext = [ord(x) for x in plaintext]
    # This integer can be converted into binary.
    plaintext_binary = [decimal_to_binary(x) for x in plaintext]

    for i in range(0, len(plaintext_binary)):
        l = len(plaintext_binary[i])
        # The ASCII encoded integers may not have 8-bit binary representation
        # so we pad the binary numbers before we add them into the list of
        # bytes. Byte = 8-bits.
        plaintext_binary[i] = ('0'*(8-l)) + plaintext_binary[i]

    return plaintext_binary

# This function takes plaintext and returns a list of the individual bits
def text_to_bits(plaintext):

    """
        This function takes in plaintext (type str) and outputs a list
        of the corresponding bits.

        Output: list (type list) of bits that encode the plaintext.

    """
    # Use the previos function to get the bytes.
    plaintext_bytes = text_to_bytes(plaintext)
    # Tease each byte apart into its component bits.
    plaintext_bits = []
    for string in plaintext_bytes:

        string = list(string)
        plaintext_bits = plaintext_bits + string

    return plaintext_bits

# ---------------------------------------------------------------------------
#                           Hamming Distance
# ---------------------------------------------------------------------------

# This function calculates the hamming distance of two plaintexts (type str).
# Note: This function passed the test on Cryptopals.
def hamming_plaintext(text1,text2):

    """
        Returns the hamming distance of two strings (type str) of plaintext.
        If the strings aren't of equal length, then it returns an error message.

    """

    l1 = len(text1)
    l2 = len(text2)

    text1_binary_bits = text_to_bits(text1)
    text2_binary_bits = text_to_bits(text2)

    text1_XOR_text2 = [((int(x) + int(y)) % 2) for x,y in zip(text1_binary_bits,text2_binary_bits)]

    sum = 0
    for x in text1_XOR_text2:
        sum += x

    if l1 == l2:
        return sum
    else:
        return "Strings aren't the same length."


# ---------------------------------------------------------------------------
#                               XOR Functions
# ---------------------------------------------------------------------------

def binary_XOR(binary_string1, binary_string2):

    '''
        This function XORs two binary strings together i.e. it outputs a binary
        string which is the bitwise XOR ('exclusive or') of the two input strings

        s | t | s XOR t
        ----- | --------        This differs from 'or' in the first column
        1 | 1 |    0            where both being true returns false, rather
        1 | 0 |    1            than true. Hence EXCLUSIVE-or.
        0 | 1 |    1
        0 | 0 |    0

        'Exclusive or' can also be understood as component wise addition
        modulo 2. While 'or' is addition in the other semifield of size two,
        the Booleans.
    '''

    # Turn the strings into a list.
    bin1 = list(binary_string1)
    bin2 = list(binary_string2)

    # If they are of different length, then we pad the shorter string on the
    # left with 0s. We pad on the left as this does not change the number.
    # padding on the right changes the number!
    l1 = len(bin1)
    l2 = len(bin2)

    if l1 < l2:

        # Pad start of short binary with zeroes
        diff = l2 - l1
        zeroes = '0'*diff
        zeroes = list(zeroes)
        bin1 = zeroes + bin1

    elif l2 < l1:

        # Pad start of short binary with zeroes
        diff = l1 - l2
        zeroes = '0'*diff
        zeroes = list(zeroes)
        bin2 = zeroes + bin2

    else:
        pass

    XOR_binary = [((int(a) + int(b)) % 2) for a, b in zip(bin1, bin2)]

    XOR_binary_string = ''
    for x in XOR_binary:
        XOR_binary_string += str(x)

    return XOR_binary_string

def hex_XOR(hex_string1, hex_string2):

    bin1 = hex_to_binary(hex_string1)
    bin2 = hex_to_binary(hex_string2)

    binary_XOR_string = binary_XOR(bin1,bin2)

    deci_XOR = binary_to_decimal(binary_XOR_string)
    hex_XOR_string = decimal_to_hex(deci_XOR)

    return hex_XOR_string
