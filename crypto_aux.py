# Cryptography related functions.
from crypto_numbertheory import *

# ---------------------------------------------------------------------------
#                       Bits n Bytes of Information
# ---------------------------------------------------------------------------

# NOTE:
#       Always operate on raw bytes, never on encoded strings.
#       Only use hex and base64 for pretty-printing.

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

# This function takes plaintext and returns a list of the individual bits.
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

# The following functions allow us to go to and from a binary string to
# the corresponding collection of 8-bit bytes.

def binary_to_bytes(binary_string):

    '''
        Input: binary string (type string)
        Output: list of 8-bit bytes (type list)

        This function returns the collection of 8-bit bytes of a given
        binary string.

        The collection of bytes is from the right. Imagine the binary string
        being feed into a reader-head from the left. This is the convention
        used throughout these files.

    '''

    binary_list = list(binary_string)
    length_binary = len(binary_list)
    binary_list.reverse()

    # The binary string may not have length divisible by 8. So we may have
    # to pad accordingly.
    fullbytes = (length_binary / 8)
    #remainder = length_cipher_bin % 8

    bytes = []

    for i in range(0,fullbytes):
        byte = binary_list[(8*i) : ((8*i)+8)]
        bytes.append(byte)
    bytes.append(binary_list[fullbytes*8 : ])
    bytes.reverse()

    # Each byte is a list at the moment. We now turn them into strings.
    bytes_string = []
    for byte in bytes:
        byte.reverse()
        str_byte = ''
        for i in byte:
            str_byte = str_byte + i
        bytes_string.append(str_byte)

    return bytes_string

def hex_to_bytes(hex_string):

    '''
        Input: hex string (type string)
        Output: list of bytes of the hex string (type string)

    '''

    return binary_to_bytes((hex_to_binary(hex_string)))

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

def hamming_binary(binary1, binary2):

    '''
        Input: two binary strings.
        Output: return Hamming distance between strings.

    '''

    binary1 = list(binary1)
    binary2 = list(binary2)

    XOR_binary = [((int(x)+int(y)) % 2) for x,y in zip(binary1, binary2)]

    if len(binary1) == len(binary2):
        return sum(XOR_binary)
    else:
        return 'Binary strings not equal length.'


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

# ---------------------------------------------------------------------------
#                        English Detection Functions
# ---------------------------------------------------------------------------

# There are a number of ways to detect whether a given piece of text is
# actually english and not gibberish. First, one could simply count the number
# of instances of common english words:
def is_english_wordfreq(ct):

    '''
        Input: a list of integers (ASCII encoded characters)

        Output: Boolean (True, if enough english words counted)

        This function uses the following common words:

        common words = ['the', 'be ', 'to ', 'of ', 'and', 'for', 'in ', 'not',
                        'you', ' a ']

        In order to determine whether or not the sentence is english. Notice
        we make all of these strings length three with spaces in order
        to get around the obstacle of looking for different length words.
        Looking for words of different lengths would require multiple loops.

    '''

    # We will count the number of instances of the following words.
    # We need to calibrate the threshold for "is english" depending
    # upon the length of the text.
    count = 0
    common_words = ['the', 'be ', 'to ', 'of ', 'and', 'for', 'in ', 'not',
                    'you', ' a ', 'is ', 'Now']

    # We loop through the text looking for any instance of the these
    # three character words. Increasing our count whenever one is found.
    for i in range(len(ct)-2):
        if chr(ct[i])+chr(ct[i+1])+chr(ct[i+2]) in common_words:
            count+=1

    # This next statement dictates the number of instances required to
    # determine whether the sentence is English. In long texts one might
    # expect some words to arise by chance in gibberish, so the count
    # should be higher for longe texts. Smaller for shorter texts.
    if count > 1:
        return True
    else:
        return False

# In order to break XOR (Vignere cipher) we need to break the cipher text
# into blocks. Blocks which will not contain any words when decrypted.
# Therefore we need another metric in order to detect english. For this we
# will use letter frequency scores rather than word frequency.
def is_english_letterfreq(ct):

    """
        This function takes in a string and assigns it a score based on the
        frequency of the individual characters in the string. Higher scorer
        should correspond to "more likely to be english".

        It is intended that this function will be used to score a whole bunch of
        of different texts, to help determine which of them is actually english.

        It employs the following dictionary to obtain the scores for each pair:

        letter_frequencies = {'e': 0.1202, 't': 0.0910, 'a': 0.0812, 'o': 0.0768,
                              'i': 0.0731, 'n': 0.0695, 's': 0.0628, 'r': 0.0602,
                              'h': 0.0592, 'd': 0.0432, ' ': 0.2918,
                              'l': 0.0398, 'u': 0.0288, 'c': 0.0271, 'm': 0.0261,
                              'f': 0.0230, 'y': 0.0211, 'w': 0.0209, 'g': 0.0203,
                              'p': 0.0182, 'b': 0.0149, 'v': 0.0111, 'k': 0.0069,
                              'x': 0.0017, 'q': 0.0011, 'j': 0.0010, 'z': 0.0007,
                              'E': 0.1202, 'T': 0.0910, 'A': 0.0812, 'O': 0.0768,
                              'I': 0.0731, 'N': 0.0695, 'S': 0.0628, 'R': 0.0602,
                              'H': 0.0592, 'D': 0.0432,
                              'L': 0.0398, 'U': 0.0288, 'C': 0.0271, 'M': 0.0261,
                              'F': 0.0230, 'Y': 0.0211, 'W': 0.0209, 'G': 0.0203,
                              'P': 0.0182, 'B': 0.0149, 'V': 0.0111, 'K': 0.0069,
                              'X': 0.0017, 'Q': 0.0011, 'J': 0.0010, 'Z': 0.0007
                              }
        These frequencies were taken from wikipedia.
    """

    letter_frequencies = {'e': 0.1202, 't': 0.0910, 'a': 0.0812, 'o': 0.0768,
                          'i': 0.0731, 'n': 0.0695, 's': 0.0628, 'r': 0.0602,
                          'h': 0.0592, 'd': 0.0432, ' ': 0.1918,
                          'l': 0.0398, 'u': 0.0288, 'c': 0.0271, 'm': 0.0261,
                          'f': 0.0230, 'y': 0.0211, 'w': 0.0209, 'g': 0.0203,
                          'p': 0.0182, 'b': 0.0149, 'v': 0.0111, 'k': 0.0069,
                          'x': 0.0017, 'q': 0.0011, 'j': 0.0010, 'z': 0.0007,
                          'E': 0.1202, 'T': 0.0910, 'A': 0.0812, 'O': 0.0768,
                          'I': 0.0731, 'N': 0.0695, 'S': 0.0628, 'R': 0.0602,
                          'H': 0.0592, 'D': 0.0432,
                          'L': 0.0398, 'U': 0.0288, 'C': 0.0271, 'M': 0.0261,
                          'F': 0.0230, 'Y': 0.0211, 'W': 0.0209, 'G': 0.0203,
                          'P': 0.0182, 'B': 0.0149, 'V': 0.0111, 'K': 0.0069,
                          'X': 0.0017, 'Q': 0.0011, 'J': 0.0010, 'Z': 0.0007
                          }


    l = len(ct)
    score = 0
    for i in range(0,l):

        if ct[i] in letter_frequencies:
            score = score + letter_frequencies[ct[i]]
        else:
            pass

    return score

# ---------------------------------------------------------------------------
#                             XOR Encryption
# ---------------------------------------------------------------------------
def XOR_encryption(plaintext, key):

    '''
        Input: plaintext (type str) and key (type str).

        Output: Plaintext XOR'd against the (repeated) key printed in
                hex encoding to "look pretty".

    '''

    plaintext = list(plaintext)
    key = list(key)

    l_key = len(key)
    l_plaintext = len(plaintext)

    # Use ASCII encoding to get intger values for each character in plaintext.
    plaintext = [ord(x) for x in plaintext]

    # Since the key length may not divide the length of the plaintext, we have
    # to make sure we repeat the key the correct number of times.
    repeat = l_plaintext / l_key
    buff = l_plaintext % l_key
    key = key * repeat
    for i in range(0,buff):
        key.append(key[i])
    key = [ord(x) for x in key]

    # With the key the appropiate length, we can now XOR the plaintext with key.
    ciphertext_ASCII = [x^y for x,y in zip(plaintext,key)]
    ciphertext_binary = [decimal_to_binary(x) for x in ciphertext_ASCII]

    # Something needs to be done...
    for i in range(1, len(ciphertext_binary)):
        l_buff = 8 - len(ciphertext_binary[i])
        buff = '0'*l_buff
        ciphertext_binary[i] = buff + ciphertext_binary[i]

    # Now the ciphertext is in bytes. So we make one binary number for the
    # entire ciphertext.
    ciphertext_binary_string = ''
    for i in ciphertext_binary:
        ciphertext_binary_string += i

    # Now we want convert the ciphertext into HEX for printing.
    ciphertext_decimal_string = binary_to_decimal(ciphertext_binary_string)
    ciphertext = decimal_to_hex(ciphertext_decimal_string)

    return ciphertext

# ---------------------------------------------------------------------------
#                         Decipher XOR Encryption
# ---------------------------------------------------------------------------

# This function good to apply on cipher text all of which has been encrypted
# with single character XOR. If one were to search through a .txt file
# for parts that have been encrypted the output of this function would
# not be so useful.
def one_character_XOR_decipher(cipher_text):

    '''
        Input: Type list of integers. This function takes the cipher text after
               it has been put into bytes and then turned into the corresponding
               integers.

        Output: Plaintext message and the key.

        Note: This instance of the function is best used when applied to
              text that is known to be encrypted using XOR cipher.

    '''

    l_cipher = len(cipher_text)

    # This lists all possible single character keys.
    keys = [chr(x) for x in range(0,255)]

    for key in keys:

        plain_text_candidate = []

        for i in range(0, l_cipher):
            plain_text_candidate.append(cipher_text[i] ^ ord(key))

        if is_english_wordfreq(plain_text_candidate) == True:
            readable_message = ''
            for x in plain_text_candidate:
                readable_message += chr(x)

            return "Key is: %s. \nPlaintext is: %s.\n" % (key,readable_message)
            break
        else:
            pass

# Cryptopals Set 1 Challenge 4 requires us to do just that kind of search
# through a file for a section that has been encrypted.
def one_character_XOR_search_decipher(cipher_text):

    '''
        Input: Type list of integers. This function takes the cipher text after
               it has been put into bytes and then turned into the corresponding
               integers.

        Output: Boolean, as to whether or not the text has been deciphered
                into a proper english sentence.

        Note: This instance of the function is used to search for lines
              encrypted with XOR inside a file which is not entirely encrypted
              in this way. Looking for encrypted text among gibberish.

    '''

    keys = [chr(x) for x in range(0,255)]
    l_cipher = len(cipher_text)

    for key in keys:

        plain_text_candidate = []

        for i in range(0, l_cipher):
            plain_text_candidate.append(cipher_text[i] ^ ord(key))

        if is_english_wordfreq(plain_text_candidate) == True:
            readable_message = ''
            for x in plain_text_candidate:
                readable_message += chr(x)

            print "Key is: %s \nPlaintext is: %s\n" % (key,readable_message)


            return True
            # We are told there is only one line of ciphertext, so we can
            # stop the function once we have found one.
            break

        else:
            pass
