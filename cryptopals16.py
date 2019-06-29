# Cryptopals Set1: Challenge 6
from crypto_aux import *


# Step by step encryption method:

# Step 1: Plaintext string ---> plaintext list.
# Step 2: Plaintext list ---> binary list.
# Step 3: Binary list ---> list of bytes (pad the short binary numbers).
# Step 4: List of bytes ---> one binary string (concatenate bytes).
# Step 5: Binary string ---> cipher binary string (XOR'd with a repeated key).
# Step 6: Cipher binary string ---> list of 6-bit bytes.
# Step 7: list of 6-bit bytes ---> base 64 representation.

# In order to decrpyt the file, I will need to undo each of these steps.

# ---------------------------------------------------------------------------
#                    Step 0: Get the data from the file.
# ---------------------------------------------------------------------------

# Note: when reading the file one naturally obtains a new-line command "\n"
#       which has to be removed in order to decrypt the ciphertext properly.
#       This may be due to the way I am reading. Or, due to some formatting
#       which happened post encryption.

# Import text from the file given with the exercise.
file = open("cpals16.txt", "r")
file_lines = []
for i in range(0,64):
    file_lines.append(file.readline())
# Close file to save memory
file.close()

# Turn the given file into a string.
file_string = ''
for part in file_lines:
    # This removes the final character from each line. This seems necessary.
    file_string = file_string + part[:-1]


# Note: each line in the file ends with a newline ( \n ) command.
#       These need to be removed before decryption. Or else the algorithm
#       outlined by this script will not work.

# ---------------------------------------------------------------------------
#                       Step 1: Base64 ---> 6-bit binary
# ---------------------------------------------------------------------------

file_list_base64 = list(file_string)
file_list_decimal = [base64_to_decimal(x) for x in file_list_base64]
#file_list_ASCII = [ord(x) for x in file_list_base64]
file_list_binary = [decimal_to_binary(x) for x in file_list_decimal]

# Note: Not all of these binary numbers are 6-bits long.
#       So we pad them to 6-bits. Technically, the first entry does not need
#       to be padded. Padding it does not change anything.

L = len(file_list_binary)
for i in range(0,L):
    l_string = len(file_list_binary[i])
    file_list_binary[i] = ((6 - l_string)* '0') + file_list_binary[i]


# ---------------------------------------------------------------------------
#                   Step 2: 6-bit binary ---> binary string
# ---------------------------------------------------------------------------

ciphertext_binary = ''
for x in file_list_binary:
    ciphertext_binary += x


# ---------------------------------------------------------------------------
#                     Step 3: Undo the XOR Encryption...
# ---------------------------------------------------------------------------

# First we need to determine the key!
ciphertext_bytes = binary_to_bytes(ciphertext_binary)
#print len(ciphertext_bytes)
# For some reason there is an empty string in the first entry...
del ciphertext_bytes[0]
number_of_bytes = len(ciphertext_bytes)

# ---------------------------------------------------------------------------
#   Aside: Sanity Check...
# ---------------------------------------------------------------------------

# So, I know the key length is 29. In order to test whether or not I have
# done my bit/byte manipulation correctly I will use the known key to check.
# key = "Terminator X: bring the noise"
# key = list(key)
# key = [ord(x) for x in key]
# key = key * number_of_bytes
# #print 'Key length: ', len(key)
#
# text = [chr((binary_to_decimal(x) ^ y)) for x,y in zip(ciphertext_bytes,key)]

# What this "sanity check" showed me is that an error entered when reading
# the file into the script. Lesson: be mindful of newline (or other invisible?)
# commands in .txt files. Frustrating!

# ---------------------------------
#  Step 3a: Find the key length
# ---------------------------------

# Note: key difference to cryptopals solution is that this script considers
#       all pairs of key-size many bytes. Not just the first few.

key_size = XOR_keysize(ciphertext_binary)

print "The key size with smallest hamming distance score is: %s" % key_size
print "Therefore, we should expect the key size to be %s\n" % key_size

# This predicts the key size is 29. It has the lowest score. It is significantly
# different from all of the others.

# ----------------------------
#  Step 3b: Break into blocks
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
#  Step 3c: Break blocks as single character XOR and assemble key.
# ----------------------------------------------------------------

XOR_key = ''
for block in transposed_blocks:
    XOR_key += one_character_letterfreq_XOR_decipher(block)
print '\nThe key is: %s\n' % XOR_key

# ---------------------------------
#  Step 3d: Decrpyt the .txt file!
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

print decrypted_message
