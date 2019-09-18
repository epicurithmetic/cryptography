# Cryptopals Set 2.
from crypto_aux import *

# ---------------------------------------------------------------------------
#                                 Challenge 1
# ---------------------------------------------------------------------------

print('\n')
print('-'*35)
print('Challenge 1: Implement PKCS#7 Padding')
print('-'*35)
print('\n')

blocksize = 20
string = "YELLOW SUBMARINE"

padded_string = padding_pkcs7(string,blocksize)
print(padded_string)

# ---------------------------------------------------------------------------
#                                 Challenge 2
# ---------------------------------------------------------------------------

print('\n')
print('-'*35)
print('Challenge 2: Implement CBC Mode')
print('-'*35)
print('\n')
