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


def pad_fullbyte(binary_string):

    L = len(binary_string)

    if L == 8:
        return binary_string
    else:
        return (('0')*(8-L) + binary_string)

x = '1110101'
print(pad_fullbyte(x))

# ---------------------------------------------------------------------------
#                                  Padding
# ---------------------------------------------------------------------------

def padding_pkcs7(string,blocksize):

    """
        This function pads a message to a specified size by appending
        entire bytes (i.e. two digit hexadecimal) until the required blocksize
        is obtain.

        Due to the way PKCS#7 is specifed, this seems to only make sense
        if the number of bytes to be added is at most 255 = FF. Otherwise
        the hexadecimal representation would be larger than two-bytes.

    """

    pad_size = blocksize - len(string)
    pad = '0'


    if pad_size < 0:
        print("String length longer than the required block length.")
        return string
    elif pad_size < 10:
        pad += str(pad_size)
    elif pad_size < 16:
        pad += decimal_to_hex(pad_size)
    else:
        pad = decimal_to_hex(pad_size)

    string_padded = string
    i = 0
    for i in range(0,pad_size):
        string_padded += pad
        i += 1


    return string_padded

#print(padding_pkcs7("YELLOW SUBMARINE",20))
# ---------------------------------------------------------------------------
#                              Hamming Distance
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
        ----- | --------        This differs from 'or' in the first row
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
    repeated_key = key*repeat + key[0:buff]

    # With the key the appropiate length, we can now XOR the plaintext with key.
    ciphertext_ASCII = [x^y for x,y in zip(plaintext,repeated_key)]
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

# This function scores keysizes and returns the smallest score. The smallest
# score is the "most likely" to be the keysize for an XOR encryption.
def XOR_keysize(binary_data):

    '''
        Input: binary string (type str)
        Output: key length (type int)

        This function takes a binary string input (assumed to be the binary
        data of an XOR encrypted file) and outputs an integer corresponding
        to the most likely keysize that was used to encrypt the data.

        Note: This function does more than it needs to. It could easily be
              made more efficient.

    '''

    # We calculate the scores for a number of key lengths.
    key_scores = []

    # This loop dictates the number of key lengths test.
    for s in range(1,41):

        # Determine how many chunks of bytes of a given keysize there are.
        N = (len(binary_data)/8)/s

        # Collect the chunks.
        chunks = []
        for i in range(0,N):
            chunk = binary_data[(8*s)*i:(8*s)*(i+1)]
            chunks.append(chunk)

        # Now we calculate the hamming distances of pairs of chunks. Scaled by
        # the keysize in order to normalize the scores across keysizes.
        hamming_distances_chunks = []
        for j in range(0, (N/2)-1):
            ham_chunk = (hamming_binary(chunks[2*j],chunks[(2*j)+1])/float(s))
            hamming_distances_chunks.append(ham_chunk)

        # Now average all of the hamming distances for the chunks.
        score = sum(hamming_distances_chunks)/N
        key_scores.append([s,score])

    # Now it remains to pick the smallest.
    key_size = 0
    min_key_ham = 1000

    for k in key_scores:
        if k[1] < min_key_ham:
            min_key_ham = k[1]
            key_size = k[0]
        else:
            pass

    return key_size

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

            print("Key is: %s \nPlaintext is: %s\n" % (key,readable_message))


            return True
            # We are told there is only one line of ciphertext, so we can
            # stop the function once we have found one.
            break

        else:
            pass

# The next instance of the XOR decipher function simply returns the key.
# Also the first to employ character frequency rather than word frequency.
def one_character_letterfreq_XOR_decipher(cipher_text_bytes):

    '''
        Input: List of bytes of binary data corresponding to data encrypted with
               single character XOR (type list)

        Output: One character key used to encrypt.

        Note: This uses letter frequency analysis to detect the key.

    '''

    max_score = 0
    max_score_key = ''

    keys = range(0,255)

    for key in keys:

        data_XOR_key = [(binary_to_decimal(x) ^ key) for x in cipher_text_bytes]
        message = ''
        for x in data_XOR_key:
            message += chr(x)

        score = is_english_letterfreq(message)
        #print score
        if score > max_score:
            max_score = score
            max_score_key = chr(key)
        else:
            pass

    return max_score_key



# Even better is a function which takes a string and measures the difference
# between the frequency of the string and the expected frequency of the
# english language.
def isit_english(string):

    '''
        Measures frequency of letters in string, compares them to expected
        frequency of the english language.


    '''

    # This dictionary stores the expected frequencies of the letters of
    # the english language.
    expected = {'e': 0.1202, 't': 0.0910, 'a': 0.0812, 'o': 0.0768,
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
                          'X': 0.0017, 'Q': 0.0011, 'J': 0.0010, 'Z': 0.0007}


    # Alphabet
    alphabet = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m',
                  'f', 'y', 'w', 'g','p', 'b', 'v', 'k','x','q','j','z']

    # Now we need to measure the frequency of the string.
    L = len(string)

    # Store the measured frequncies.
    measured = {}

    # Measure the frequencies of the string.
    for letter in alphabet:

        count = 0

        # Count the instances of letter.
        for i in range(0,L):
            if (string[i] == letter) or (string[i] == letter.upper()):
                count += 1
            else:
                pass

        # Calculate frequency of letter.
        letter_measure = count / float(L)

        # Appened the measured values.
        measured[letter] = letter_measure

    # With the relative frequencies measured, we need to score the string
    # depending upon it's  "Englishness" ...
    score = 0

    for letter in alphabet:

        score += (expected[letter] ** 2) - (measured[letter] ** 2)

    # This scoring method says an string is "more english" than another
    # string if the score is closer to 0.

    return score

# x = 'This cipher is the most widely used symmetric-cipher. It is applied by the USgovernment to encrypt SECRET and TOP-SECRET data. As of May 2009 the only'
# print(isit_english(x))
# print(isit_english('fuck a duck a'))
# print(isit_english('asdjfkhnwlar23'))



# government to encrypt SECRET and TOP-SECRET data. As of May 2009 the only
# attacks against AES have been side channel attacks. That is, attacks which
# have used flaws in the implementation, rather than flaws in the algorithm
# itself. Nothing better than brute-force has been (publically) done.








# ---------------------------------------------------------------------------
#                   Advanced Encryption Standard (AES)
# ---------------------------------------------------------------------------

# This cipher is the most widely used symmetric-cipher. It is applied by the US
# government to encrypt SECRET and TOP-SECRET data. As of May 2009 the only
# attacks against AES have been side channel attacks. That is, attacks which
# have used flaws in the implementation, rather than flaws in the algorithm
# itself. Nothing better than brute-force has been (publically) done.

# Snowden documents stated that the NSA were considering the use of "Tau
# statistics" in their efforts to test AES.

# Although a lot of theoretical research has been done on attacking AES, none
# of this research has yielded anything better than > billion year run time.

# Ultimately, the belief in the security of AES comes from the fact that it has
# so far passed the extensive testing to which it has been subjected by the
# crypto community.

# ----------------------------------------------
#   Detecting AES in Electronic Code Book (ECB)
# ----------------------------------------------

# One of the primary weaknesses of AES-ECB is that it encodes four-byte blocks
# seperately. Therefore any repeated four-byte block in the text will be appear
# as a repeated four-byte block in the cipher text. Gibberish is unlikely to
# have repeated four-byte blocks. But english plaintext could well have
# repeated four-byte blocks. This simple obeservation can allow us to detect
# AES in the ECB mode of operation.

# --------------------------
#   Encrpytion with AES-128
# --------------------------

# Encrypting data with the AES requires a block of three steps repeated a
# number of times. In the case of AES-128 the block of three steps will be
# repeated ten times.

# For now we will discuss how to encrypt 16-byte strings. Once we know how to
# do this, there are a number of options (Modes of Operation) for AES to
# encrypt longer strings of plaintext. We will also assume the key is 128-bits
# i.e. the key length is 16-byte = length of plaintext block.

# ---------------------------------------------------
#   AES-128  Step 1: Byte Substitution Layer (S-Box)
# ---------------------------------------------------

# Here is some plaintext from Edgar Allan Poe:
plain_text = 'Quoth the raven1'                 # plaintext of length 16-bytes.
# The AES protocol works on the bytes.
plain_text_bytes = text_to_bytes(plain_text)    # These are the bytes.
# Some the AES protocol works on the following matrix presentation of the bytes.
plain_text_matrix = []
for i in range(0,4):
    plain_text_matrix.append(plain_text_bytes[4*i:4*(i+1)])

# print plain_text
# print plain_text_bytes
# print plain_text_matrix


# The byte substitution layer does two things to each byte of the plaintext
#           1. It swaps the byte for the inverse of the corresponding element
#              of the finite field GF(256).
#           2. Performs an affine mapping on each of the resulting bytes.
#              First the string is multiplied by the matrix:
#
#                  M = [[1,0,0,0,1,1,1,1],
#                        [1,1,0,0,0,1,1,1],
#                        [1,1,1,0,0,0,1,1],
#                        [1,1,1,1,0,0,0,1],
#                        [1,1,1,1,1,0,0,0],
#                        [0,1,1,1,1,1,0,0],
#                        [0,0,1,1,1,1,1,0],
#                        [0,0,0,1,1,1,1,1]]
#
#               Finally, each byte is shifted by the following vector
#
#                   V = [1,1,0,0,0,1,1,0]
#
# Note: the "vector" representation of the byte has the highest degree term
#       as the last entry of the vector.

# First we determine the inverse of each element of the block.
def AES_sbox_inverse(block):

    '''
        Input: block of 16-bytes (Type, list)
        Output: block of 16-bytes (Type, list)

        This function interprets each byte as an element of GF(256) and
        maps it to the inverse in that field. The byte 00000000 does not
        have an inverse in GF(256). It is defiend to be sent to itself.

        This function performs one of the two stages of the byte substitution
        layer of the AES encryption scheme.

    '''

    output_bytes = []
    for x in block:

        # In order to use the GF(256) function from the number theory library
        # we need to remove any leading zeroes on the bytes.
        x = list(x)
        leading_zeroes = True
        while leading_zeroes == True:
            if len(x) == 1:
                leading_zeroes = False
            elif x[0] == '0':
                del x[0]
            else:
                leading_zeroes = False

        # Return to Type string.
        x_cleaned = ''
        for i in x:
            x_cleaned += i

        # Calculate the inverse
        x_inverse = GF256_inverse(x_cleaned)

        # Pad the inverse to a full 8-bit byte.
        x_inverse = '0'*(8 - len(x_inverse)) + x_inverse

        # Append the new byte to the output.
        output_bytes.append(x_inverse)

    return output_bytes

# ------------------------------------------------
# Aside: Matrix scaling a column vector over GF(2)
# ------------------------------------------------
# In order to perform the affine transformation, we need to perform matrix
# multiplication. We only require the specific case of nxn acting on nx1.
def GF2_matrix_multiply_column(matrix,column):

    '''
        Input: An nxn matrix (Type, list) and an nx1 column vector (Type, list)
        Output: An nx1 column vector (Type, list)

        Note: The matrix is assumed to be a list containing n lists, each of
              which contains n entries.
    '''

    n = len(column)
    m = len(matrix[0])

    if not n == m:
        print('Dimensions do not match.')
        return None

    output = []

    # Index over the rows.
    for i in range(0,n):

        output_entry = 0

        # Index over the columns.
        for j in range(0,n):

            output_entry = ((output_entry + matrix[i][j]*column[j])%2)

        output.append(output_entry)

    return output

# Now we can perform the required affine transformation.
def AES_sbox_affine(block):

    '''
        Input: block of 16 bytes (Type, list)
        Output: block of 16 bytes (Type, list)

        This function perfoms an affine transformation on each byte of the
        block. Scaling by a matrix (determined by the AES) and then shifting
        by a vector i.e. XORing with a fixed-byte.

        Note: the algorithm requires the reversal of the bytes in order
              to multiply by the matrix in the correct manner.

    '''

    # S-Matrix and shift vector for the affine transformation.
    smatrix = [[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]
    v_shift = [1,1,0,0,0,1,1,0]

    # Initialize the output.
    substitution_layer_block = []

    # Work one byte at a time.
    for byte in block:

        # Change data type of bits to int for matrix multiplication.
        byte = list(byte)
        byte = [int(x) for x in byte]

        # Reverse the byte to match the matrix.
        byte.reverse()

        # Hit byte with the matrix.
        byte_smatrix = GF2_matrix_multiply_column(smatrix,byte)
        # Shift by the vector.
        byte_sbox = [((x+y)%2) for x,y in zip(byte_smatrix,v_shift)]

        # Undo reverse.
        byte_sbox.reverse()

        # Change data type to string.
        byte_sbox_string = ''
        for x in byte_sbox:
            byte_sbox_string += str(x)

        # Append the affine transformed block.
        substitution_layer_block.append(byte_sbox_string)

    return substitution_layer_block

# With the two components of the S-box defined we can put them together
# to complete the first step of the AES
def AES_sbox_encrypt(block):

    '''
        Input: 16-bytes (Type, list)
        Output: 16-bytes (Type, list)

        This function performs both the GF(256) inversion and affine
        transformation required of the S-box layer of the AES.

    '''

    block_inverse = AES_sbox_inverse(block)
    block_inverse_affine = AES_sbox_affine(block_inverse)

    return block_inverse_affine

# -----------------------------------
#   AES-128  Step 2: Diffusion Layer
# -----------------------------------

# The diffusion layer of AES consists of two sublayers: (i) Shiftrows sublayer
# and the (ii) Mixcolumn sublayer.

# The shift rows sublayer acts on each row of the 4x4 state matrix.
# First row:  No shift
# Second row: Three positions to the right (equiv. One to the left.)
# Third row:  Two positions to the right (equiv. Two to the left.)
# Fourth row: One positions to the right (equiv. Three to the left.)

def AES_diffusion_row(state_matrix):

    '''
        Input: 4x4 state matrix (Type, list)
        Output: 4x4 state matrix (Type,list)

        This function is part of the AES diffusion layer. Performs the
        following transformations on the rows:

                Row 1: No shift
                Row 2: Three positions to the right
                Row 3: Two positions to the right
                Row 4: One position to the right


    '''
    # Initialize the output.
    output_state_matrix = []

    # Row 1 has no shift.
    output_state_matrix.append(state_matrix[0])

    # Row 2 is shifted three positions to the right.
    output_row_two = []
    for i in range(0,4):
        output_row_two.append(state_matrix[1][(1+i)%4])

    output_state_matrix.append(output_row_two)

    # Row 3 is shifted three positions to the right.
    output_row_three = []
    for i in range(0,4):
        output_row_three.append(state_matrix[2][(2+i)%4])

    output_state_matrix.append(output_row_three)

    # Row 2 is shifted three positions to the right.
    output_row_four = []
    for i in range(0,4):
        output_row_four.append(state_matrix[3][(3+i)%4])

    output_state_matrix.append(output_row_four)

    return output_state_matrix

# The shift column sublayer is more complex in nature.
# Each *column* of the state matrix is multiplied by the following matrix
#
#       rijndael_matrix = [ [x, x+1, 1, 1],
#                           [1, x, x+1, 1],
#                           [1, 1, x, x+1],
#                           [x+1, 1, 1, x] ]
#
# All of the arithmetic is done in GF(256).

rijndael_matrix = [ ['10', '11', '1', '1'],
                    ['1', '10', '11', '1'],
                    ['1', '1', '10', '11'],
                    ['11', '1', '1', '10'] ]

test_input = ['11011011','00010011','01010011','01000101']
test_output = ['10001110','01001101','10100001','10111100']

def GF256_matrix_multiply_column(matrix,column):

    '''
        Input: An nxn matrix with entries in GF(256) and an nx1 column
               vector with entries in GF(256). (Type, list)
        Output: nx1 column vector with entries in GF(256). (Type, list)

        Note: elements of GF(256) are strings (Type, str) of binary with
              max length 8.

    '''

    n = len(column)
    m = len(matrix[0])

    if not n == m:
        print('Dimensions do not match.')
        return None

    output = []

    # Index over the rows.
    for i in range(0,n):

        output_entry = '0'

        # Index over the columns.
        for j in range(0,n):
            output_entry = GF2_polynomial_sum(output_entry, GF256_multiplication(matrix[i][j],column[j]))

        # Pad to full-byte
        output_entry = pad_fullbyte(output_entry)

        # Append to output
        output.append(output_entry)

    return output

#print GF256_matrix_multiply_column(rijndael_matrix,test_input) == test_output










































# ---------------------------------------------------------------------------
#                    Math 3301: Cryptography Exercises
# ---------------------------------------------------------------------------

# Here I collect a number of the cryptography exercies used in the cryptography
# part of Math3301: Number Theory and Cryptography.

# ----------------------------------------
# Caesar Cipher Encryption and Decryption
# ----------------------------------------

# This cipher encodes the english alphabet as [a,0] [b,1], [c,2], ..., [z,25].
# Adds a fixed number k (the key) to each number, reducdes mod 26 and turns
# reverses the alphabet-to-number dictionary.

# First let's create a dictionary to store the alphabet-to-number assignment.
# Lower-case letters are ASCII 97 - 122. Upper-case are 65 - 90
caesar_cipher_dict = {' ':26, 26:' '}
for i in range(0,26):
    # This maps alphabet to number.
    caesar_cipher_dict[chr(97+i)] = i

    # This maps number to alphabet.
    caesar_cipher_dict[i] = chr(97+i)

# This function does the work.
def caesar_cipher(string, key, MODE):

    '''
        Input: string of text (Type, string) and a key (Type, int). MODE tells
               the code whether or not to encrypt or decrypt. MODE takes
               values 'e' (encrypt) and 'd' for decrypt.
        Output: string of text encrypted using the Caeser cipher with the
                key input into the function.

        Note: We account for 'space' in the plaintext by adding another
              element to the dictionary. Thus we need to reduce mod 27.

        Note: this assumes only lower-case letters are used. If you want
        to include upper-case letters use a dictionary [0,51] and
        reduce mod 52.

    '''

    if not (MODE == 'e' or MODE == 'd'):
        x = 'Please say whether you would like to encrypt ("e") the data or'
        y = ' decrypt ("d") the data. Check doc-string for clarification.'
        return x+y
    else:
        pass

    # We refer to the length of the plaintext a number of times.
    l = len(string)

    # Change the data type of the plaintext. This is to avoid the problem of
    # encoded numbers having more than one digit - as they do in this case.
    string = list(string)

    # Turn each element of the string into the corresponding integer.
    for i in range(0, l):
        string[i] = caesar_cipher_dict[string[i]]

    # Encrypt or decrypt depending on mode:
    if MODE == 'e':
        for i in range(0,l):
            string[i] = ((string[i] + key) % 27)
    elif MODE == 'd':
        for i in range(0,l):
            string[i] = ((string[i] - key) % 27)

    # Map back to the alphabet.
    for i in range(0,l):
        string[i] = caesar_cipher_dict[string[i]]

    # Change data type back to string.
    encrypted_string = ''
    for x in string:
        encrypted_string += x

    return encrypted_string

test_plaintext = 'attack at dawn'
test_key = 7
test_ciphertext = caesar_cipher(test_plaintext,7,'e')

dylan_thomas = ['do not go gentle into that good night ',
'old age should burn and rave at close of day ',
'rage rage against the dying of the light ',

'though wise men at their end know dark is right ',
'because their words had forked no lightning they ',
'do not go gentle into that good night ',

'good men the last wave by crying how bright ',
'their frail deeds might have danced in a green bay ',
'rage rage against the dying of the light ',

'wild men who caught and sang the sun in flight ',
'and learn too late they grieve it on its way ',
'do not go gentle into that good night ',

'grave men near death who see with blinding sight ',
'blind eyes could blaze like meteors and be gay ',
'rage rage against the dying of the light ',

'and you my father there on the sad height ',
'curse bless me now with your fierce tears i pray ',
'do not go gentle into that good night ',
'rage rage against the dying of the light']

test_long_plaintext = ''
for line in dylan_thomas:
    test_long_plaintext += line
test_long_ciphertext = caesar_cipher(test_long_plaintext,7,'e')

# ---------------------------
# Breaking the Caesar Cipher
# ---------------------------

# There are two options when breaking this encryption, one more sophisticated
# than the other. We could simply loop over all keys and read all of the
# possible outputs - One of which will be readable.
# for k in range(0,27):
#     # Use MODE = decrypt
#     print caesar_cipher(test_long_ciphertext,k,'d'),'Key: ', k

# For long texts this can mean reading through a lot of gibberish. So it would
# be good to write a function which detects the plaintext among the gibberish.
# Each character of the alphabet has a known expected frequency for a large
# enough plaintext. So a function would be written which scores the text
# according to the difference between the letter frequency of the text and the
# expected letter frequency of an english text. This function should be
# minimised on the correct plaintext.
def letter_frequency_score(text):

    '''
        Input: string of english alphabet with spaces (Type, string)
        Output: a measure of the deviation from english (Type, float)

        Using the expected frequencies of letters in written english, we score
        the text by taking the absolute value of the difference between
        the measured and expected frequencies.

    '''

    # This will measure the "english-ness" of the text.
    score = 0

    expected_letter_frequencies = {'e': 0.1202, 't': 0.0910, 'a': 0.0812, 'o': 0.0768,
                                   'i': 0.0731, 'n': 0.0695, 's': 0.0628, 'r': 0.0602,
                                   'h': 0.0592, 'd': 0.0432, ' ': 0.1918,
                                   'l': 0.0398, 'u': 0.0288, 'c': 0.0271, 'm': 0.0261,
                                   'f': 0.0230, 'y': 0.0211, 'w': 0.0209, 'g': 0.0203,
                                   'p': 0.0182, 'b': 0.0149, 'v': 0.0111, 'k': 0.0069,
                                   'x': 0.0017, 'q': 0.0011, 'j': 0.0010, 'z': 0.0007,}

    # Now we measure the frequencies of the letters in the text.
    measured_letter_frequencies = {}
    alphabet = ['e','t','a','o','i','n','s','r','h','d',' ','l','u','c','m',
                'f','y','w','g','p','b','v','k','x','q','j','z']

    # We need the length to get the measured frequency.
    l = len(text)
    text = list(text)

    for character in alphabet:

        # Count number of instances of the character.
        count = 0
        for i in range(0,l):
            if text[i] == character:
                count+=1
            else:
                pass

        # Calculate fraction of total length.
        measured_frequency = float(count)/float(l)

        # Calculate the absolute value of the difference between the measured
        # and the expected frequency
        character_score = abs(expected_letter_frequencies[character] - measured_frequency)

        # Add this to the dictionary.
        score += character_score

    return score

# With the ability to score text in this way, we can now write a function
# which will break the Caesar cipher without us having to read through
# 26 blocks of gibberish.
def caesar_break(cipher_text):

    '''
        Input: cipher_text (Type, string) to be decrypted.
        Output: plaintext message (Type, string)

        This function picks the key with the smallest letter frequency
        difference to that of the expected frequency of written english.

    '''

    L = len(cipher_text)

    min_score = L
    min_score_key = 0
    plaintext = ''

    for k in range(0,27):
        k_plaintext = caesar_cipher(cipher_text,k,'d')
        score = letter_frequency_score(k_plaintext)
        print(score)
        if score < min_score:
            min_score = score
            min_score_key = k
            plaintext = k_plaintext
        else:
            pass

    return plaintext,min_score_key

# Example:
#print caesar_break(test_long_ciphertext)

# Notice: with the length of the poem by Dyaln Thomas, the frequency score
#         for the plaintext is significantly different with the correct key.
#         Nothing else comes close. In the smaller example, the text is
#         still recovered, even though the difference in score is not very
#         very significant.
