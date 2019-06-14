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

print XOR_encryption(plaintext, 'ICE') == "b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
