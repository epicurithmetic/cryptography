# Cryptopals Set 1.
from crypto_aux import *

# ---------------------------------------------------------------------------
#                                 Challenge 1
# ---------------------------------------------------------------------------
print '\n'
print '-'*35
print 'Challenge 1: Convert hex to base64'
print '-'*35
print '\n'

challenge11 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f697'
challenge12 = '36f6e6f7573206d757368726f6f6d'

challenge1 = challenge11 + challenge12
print challenge1
print hex_to_base64(challenge1)


# ---------------------------------------------------------------------------
#                                 Challenge 2
# ---------------------------------------------------------------------------
print '\n'
print '-'*23
print 'Challenge 2: Fixed XOR'
print '-'*23
print '\n'

challenge21 = '1c0111001f010100061a024b53535009181c'
challenge22 = '686974207468652062756c6c277320657965'

print hex_XOR(challenge21, challenge22)


# ---------------------------------------------------------------------------
#                                 Challenge 3
# ---------------------------------------------------------------------------
print '\n'
print '-'*36
print 'Challenge 3: Single-byte XOR cipher'
print '-'*36
print '\n'

# First really interesting problem. Decrypt a message automatically. This
# requires the use of a function that can 'detect english'. Of course one could
# sift through all the deciphered texts and see the actual plaintext. This surely
# defeats the purpose. This should be done automatically.

challenge3 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Always act on raw bits/bytes...
challenge3_bytes = hex_to_bytes(challenge3)
challenge3_ASCII = []
for x in challenge3_bytes:
    challenge3_ASCII.append(binary_to_decimal(x))

# We are told that the plaintext has been XOR'd against a single character.
# This means the key is one of the following: x in range(65,123). These
# Consist of the upper and lower case english letters.

print one_character_XOR_decipher(challenge3_ASCII)

# ---------------------------------------------------------------------------
#                            Challenge 4
# ---------------------------------------------------------------------------
print '\n'
print '-'*41
print 'Challenge 4: Detect single-character XOR'
print '-'*41
print '\n'
# In this exercise we are to find which of 326 lines of hex have been
# encoded with a single character/byte XOR cipher.

# First we import the lines as a list.
file = open("cpals14.txt", "r")
file_lines = []
for i in range(0,327):
    file_lines.append(file.readline())
# Close file to save memory
file.close()
# Next piece removes the \n command from each string.
for i in range(0,327):
    file_lines[i] = file_lines[i][:-1]

# The following will loop through each line and attempt to decipher it.
for line in file_lines:

    # Each line of the file is hex encoded. So we need to get the corresponding
    # ASCII encoding before we can work on it. Always go to bytes/bits first!
    line_bytes = hex_to_bytes(line)
    line_deci = [binary_to_decimal(x) for x in line_bytes]

    if one_character_XOR_search_decipher(line_deci) == True:
        print "The text was on line %s." % str(file_lines.index(line) + 1)
        break
    else:
        pass

# ---------------------------------------------------------------------------
#                            Challenge 5
# ---------------------------------------------------------------------------
print '\n'
print '-'*41
print 'Challenge 5: Implement repeating-key XOR'
print '-'*41
print '\n'


print 'Plaintext to be encrypted:'
# Text to be encrypted.
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
print plaintext
print 'Key: ICE'

ciphertext_test = XOR_encryption(plaintext, 'ICE')
goal = 'b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
print ciphertext_test == goal

# ---------------------------------------------------------------------------
#                            Challenge 6
# ---------------------------------------------------------------------------
print '\n'
print '-'*41
print 'Challenge 6: Break repeating-key XOR'
print '-'*41
print '\n'

text1 = 'this is a test'
text2 = 'wokka wokka!!!'
print hamming_plaintext(text1, text2)
print 'This was a test to see if my hamming distance function works.'
print 'It returns 37, the correct value.\n'
# 37! Test passed.

# ---------------------
#  Stage 0: Read file
# ---------------------

# Note: due to formatting of the file, there are '\n' commands which
#       must be removed from the lines before the algorithm can be
#       applied.

# Import text from the file given with the exercise.
file = open("cpals16.txt", "r")
file_lines = []
for i in range(0,64):
    file_lines.append(file.readline())
file.close()

# Turn the given file into a string.
file_string = ''
for part in file_lines:
    # This removes the final character from each line. This seems necessary.
    file_string = file_string + part[:-1]

# --------------------------------------------
#  Stage 1: Data manipulation - bits n bytes
# --------------------------------------------

file_list_base64 = list(file_string)
file_list_decimal = [base64_to_decimal(x) for x in file_list_base64]
file_list_binary = [decimal_to_binary(x) for x in file_list_decimal]

# Note: Not all of these binary numbers are 6-bits long.
#       So we pad them to 6-bits. Technically, the first entry does not need
#       to be padded. Padding it does not change anything.
L = len(file_list_binary)
for i in range(0,L):
    l_string = len(file_list_binary[i])
    file_list_binary[i] = ((6 - l_string)* '0') + file_list_binary[i]

# This stores the data as a binary string.
ciphertext_binary = ''
for x in file_list_binary:
    ciphertext_binary += x

# This stores the data as a list of (8-bit) bytes.
ciphertext_bytes = binary_to_bytes(ciphertext_binary)
# For some reason there is an empty string in the first entry...
del ciphertext_bytes[0]
number_of_bytes = len(ciphertext_bytes)

# --------------------------------------------
#  Stage 2: Find the (most likely) key length.
# --------------------------------------------

key_size = XOR_keysize(ciphertext_binary)

print "The key size with smallest hamming distance score is: %s" % key_size
print  "Therefore, we should expect the key size to be %s" % key_size

# -----------------------------------------------------------
#  Stage 3: Break the transposed blocks and assemble the key.
# -----------------------------------------------------------
# ----------------------------
#  Step 3a: Break into blocks
# ----------------------------

# This step requires us to break the bytes into transposed blocks of 29
# and attack each of these with the single character key XOR attack.

# Number of transpositions.
T = number_of_bytes/key_size
# Initialize the collection of blocks.
transposed_blocks = []

# Collect each of the transposed blocks.
for i in range(0,key_size):
    block = []
    for j in range(0, T):
        block.append(ciphertext_bytes[i+(j*key_size)])
    transposed_blocks.append(block)

# ----------------------------------------------------------------
#  Step 3b: Break blocks as single character XOR and assemble key.
# ----------------------------------------------------------------

XOR_key = ''
for block in transposed_blocks:
    XOR_key += one_character_letterfreq_XOR_decipher(block)
#print XOR_key

# ---------------------------------
#  Step 3c: Decrpyt the .txt file!
# ---------------------------------

# Repeat the key along the length of the text.
XOR_key_list = list(XOR_key)
full_bytes_key = number_of_bytes/len(XOR_key)
remainder_key = number_of_bytes % len(XOR_key)
repeated_key = XOR_key_list*full_bytes_key + list(XOR_key[0:remainder_key])

decrypted_text_data = [(binary_to_decimal(x) ^ ord(y)) for x,y in zip(ciphertext_bytes, repeated_key)]

decrypted_message = ''
for x in decrypted_text_data:
    decrypted_message += chr(x)
print '\n'
print decrypted_message

# ---------------------------------------------------------------------------
#                            Challenge 7
# ---------------------------------------------------------------------------
print '\n'
print '-'*58
print 'Challenge 7: Decryption with Advanced Encryption Standard'
print '-'*58
print '\n'


print 'Not done yet.'


# ---------------------------------------------------------------------------
#                            Challenge 8
# ---------------------------------------------------------------------------
print '\n'
print '-'*57
print 'Challenge 8: Detecting AES in Electronic Code Book (ECB)'
print '-'*57
print '\n'

# Each of the modes of operation of the Advanced Encryption Standard have
# their weaknesses and strengths. One of the primary weaknesses of the ECB
# mode of operation is that it encodes all copies of the same plaintext
# in the same way.

# Gibberish is unlikely to have many repeated strings of bytes.
# Whereas english (or any other human-language) will have repeated bytes.
# This observation allows for a method of decting AES in ECB mode.

# In this exercise we have a number of lines of HEX encoded strings
# one of which has been encoded with AES-ECB and we are tasked with
# detecting which one it is.

# Read the file in.
file = open("cpals18.txt", "r")
file_lines = []
for i in range(0,204):
    file_lines.append(file.readline())
file.close()

# Next piece of code removes the \n command from each string.
for i in range(0,204):
    file_lines[i] = file_lines[i][:-1]

# global variables to store the max number of repeated 16-byte blocks.
max_repeated_block = 0
max_repeated_block_line = 0

# Now we turn the HEX data into the corresponding bytes.
for line in file_lines:
    line_bytes = hex_to_bytes(line)

    # The leading byte maybe empty. Or it may not be a full byte.
    if line_bytes[0] == '':
        del line_bytes[0]
    else:
        line_bytes[0] = '0'*(8 - len(line_bytes[0])) + line_bytes[0]

    # Now we have to group the bytes into 16-byte blocks.
    # In this case there are 160 bytes per line i.e. there are 10 blocks of
    # 16-bytes.
    sixteen_byte_blocks = []
    for i in range(0,10):
        sixteen_byte_blocks.append(line_bytes[i*16:(i+1)*16])

    repeated_block_count = 0
    for i in range(0,10):
        for j in range(i+1,10):

            if sixteen_byte_blocks[i] == sixteen_byte_blocks[j]:
                repeated_block_count += 1
            else:
                pass


    if repeated_block_count > max_repeated_block:
        max_repeated_block = repeated_block_count
        max_repeated_block_line = file_lines.index(line) + 1


print 'Line %s has the most repeated 16-byte blocks.' % max_repeated_block_line
print 'In fact, this code shows that it is the only line with repeated'
print '16-byte blocks. None of the other lines have any repeated blocks.'
print 'Thus highlighting the weakness of the ECB mode of operation - that it'
print 'can be very easy to detect this mode of encrpytion.'


# ---------------------------------------------------------------------------
#                   Cryptopals Challenge Set 1: Complete
# ---------------------------------------------------------------------------
print '\n'
print ' '+'-'*38
print '| Cryptopals Challenge Set 1: Complete |'
print ' '+'-'*38
print '\n'
