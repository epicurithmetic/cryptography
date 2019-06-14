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
#                       Step 0: Get the data from the file.
# ---------------------------------------------------------------------------

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
    file_string = file_string + part

# Note: each line in the file ends with a newline ( \n ) command.

# ---------------------------------------------------------------------------
#                       Step 1: Base64 ---> 6-bit binary
# ---------------------------------------------------------------------------

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

# For some reason there is an empty string in the first entry...
del ciphertext_bytes[0]

# ---------------------------------
#  Step 3a: Find the key length
# ---------------------------------

min_hamming_distance = 100
min_keysize = 100

for keysize in range(2,40):

    chunks = []

    # Obtain 2 chunks...
    for i in range(0,2):
        chunk = ciphertext_binary[8*i*keysize: 8*i*keysize + 8*keysize]
        chunks.append(chunk)

    if (hamming_binary(chunks[0],chunks[1]) / float(keysize)) < min_hamming_distance:
        min_hamming_distance = (hamming_binary(chunks[0],chunks[1])/float(keysize))
        min_keysize = keysize
        #print min_keysize
    else:
        pass

    print "Keysize: ", keysize
    print "Hamming distance: ", hamming_binary(chunks[0],chunks[1])

print min_hamming_distance
print min_keysize

print '\n'
print 'Judging by this the key is probably of length: 2,3, or 5.'
print 'As there is only a smaller number of options, we can try them all.'

# ----------------------------
#  Step 3b: Break into blocks
# ----------------------------

# As it is unlikely a keyword will have length 2, let us first try and see
# if the keyword is length 3.
size_of_blocks = len(ciphertext_bytes)/3

### ERROR HERE! This does not produce the right blocks. They have a lot
###   BELOW     overlap as I have written the code. They don't partition
###             as required by the algorithm specified by the cryptopals.

# Blocks is the list of bytes three (keysize) apart.
blocks = []
for i in range(0,3):
    block = []
    for j in range(0, size_of_blocks):
        block.append(ciphertext_bytes[i+j])
    blocks.append(block)

# ---------------------------------------------------
#  Step 3c: Solve each block as single character XOR
# ---------------------------------------------------

# For this, we want to score each choice of character. The highest score
# should be the corresponding character of the key.

block_one = blocks[0]
block_two = blocks[1]
block_three = blocks[2]

key_one = ''
key_two = ''
key_three = ''

score_one = 0
score_two = 0
score_three = 0

character_block_one = ''
character_block_two = ''
character_block_three = ''

block_one_decimal = [binary_to_decimal(x) for x in block_one]

for key in range(65,127):

    XOR_one = [x^key for x in block_one_decimal]

    text_one = ''

    for x in XOR_one:
        text_one += chr(x)

    score = is_english_letterfreq(text_one)

    if score > score_one:
        score_one = score
        #print text_one
        #print score_one
        key_one = chr(key)
        #print key_one
    else:
        pass

#print key_one
