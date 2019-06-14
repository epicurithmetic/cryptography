# Cryptopals Set 1.
from crypto_aux import *

# ---------------------------------------------------------------------------
#                                 Challenge 1
# ---------------------------------------------------------------------------

print '\nChallenge 1: \n'

challenge11 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f697'
challenge12 = '36f6e6f7573206d757368726f6f6d'

challenge1 = challenge11 + challenge12
print challenge1
print hex_to_base64(challenge1)


# ---------------------------------------------------------------------------
#                                 Challenge 2
# ---------------------------------------------------------------------------
print '\nChallenge 2: \n'
challenge21 = '1c0111001f010100061a024b53535009181c'
challenge22 = '686974207468652062756c6c277320657965'

print hex_XOR(challenge21, challenge22)


# ---------------------------------------------------------------------------
#                                 Challenge 3
# ---------------------------------------------------------------------------
print '\nChallenge 3: \n'
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
#                                 Challenge 4
# ---------------------------------------------------------------------------
print '\nChallenge 4: \n'
