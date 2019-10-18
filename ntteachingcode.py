# Example code for Math3301/6114
import timeit
import matplotlib.pyplot as plt

# Currently trying to move this from Python2 to Python3. However, this seems to
# introduce a lot of syntax errors. Some sections of the code may not work
# as a result.

# These are just examples of how you can do these exercises. I make no
# claim that these are efficient in any sense. I would appreciate any tips
# to make these functions more efficient!

# ------------------
# Exercise Sheet 1:
# ------------------

# Before we write any of these functions, we will first need a function which
# calculates (approximates) the square-root of an integer. This function will
# use the Newton-Raphson method to appoximate square roots. You can treat it
# like a black-box if you have not heard of this before. Note: this function
# does not return a (type integer); it returns a (type float). So we may have
# to round when want to use it.

# Newton-Raphson is used to calculate (approximate) the squareroot.
def newton_sqrt(x):

    '''
        Input: a number (Type, int or float) whose squareroot is sought
        Output: Squareroot of input (Type, float)

        Squareroot is approximated using Newton-Raphson.

    '''

    x_initial = 1
    # Delta is the difference between iterations. Used to say how accurate
    # we want the squareroot.
    delta = 1

    while delta > 0.001:
        x_new = x_initial - ( ((x_initial ** 2) - x ) / float((2 * x_initial)))
        delta = abs(x_new - x_initial)
        x_initial = x_new

    return x_initial

# Exercise 1: Divisors.
# This function outputs the list of divisors of an integer n.
def divisors(n):

    '''
        Input: Integer (Type, int)
        Output: List of integers (Type, list)

        Output is the list of divisors of the input n.

    '''


    divisors = [1,n]

    for i in range(2,int(newton_sqrt(n))+1):

        if (n%i) == 0:
            divisors.append(i)
            if not (i == n/i):
                divisors.append(n/i)
        else:
            pass

    return divisors

# Exercise 2: Exponent.
# This function outputs the exponent of a divisor d in an integer n.
def exponent_of_divisor(n,d):

    '''
        Input: Integers (Type, int).
        Output: (Type, int)

        This function returns the highest power of d that divides n.

    '''

    count = 0

    while ((n%d)==0):
        n = n/d
        count +=1

    return count

# Exercise 3: Sieve of Eratosthenes.
# This is slow. Not sure how to make it much faster.
def sieve_eratosthenes(n):

  primes = range(2,n+1)

  count = 0

  while count < newton_sqrt(n):
    for x in primes:
      if primes[count] == x:
        pass
      elif (x%primes[count]==0):
        primes.remove(x)
      else:
        pass
    count +=1
  return primes

# ------------------
# Exercise Sheet 2:
# ------------------

# Exercise 1: Naive Prime Test.
# We only need to check upto the square root. We also only have to check odd
# divisors. Are there other methods for speeding it up? Probably!
def isit_prime(n):

    '''
        Input: an integer (Type, int)
        Output: whether or not input is prime (Type, Boolean)

        This function tests divisiblity for each integer upto the squareroot
        of the input.

        Time taken to execute noticeable near the prime n = 1000000000039

    '''
    # We need only test divisiblity upto and including the squareroot.
    divisor_bound = int(newton_sqrt(n))+1

    # Boolean used to determine the output of the function.
    has_divisor = False

    d = 3
    while d <= divisor_bound:
        if (n % d) == 0:
            has_divisor = True
            break
        else:
            d = d + 2

    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    elif n == 1:
        return False
    elif has_divisor == True:
        return False
    else:
        return True

# Exercise 2: Prime Factorisation.
# This function pulls out the divisors which are prime.
def prime_divisors(n):

     ''' Input: Integer (Type, int) whose prime divisors are sought
         Output: List (Type, list) of prime divisors
     '''

     divisors_list = divisors(n)
     prime_divisors = []
     for d in divisors_list:
         if isit_prime(d) == True:
             prime_divisors.append(d)
         else:
             pass

     return prime_divisors

# This function returns the factorisation in a string.
def prime_factorisation(n):

    '''
        Input: Integer (Type, integer) whose prime factorisation is sought.
        Output: Prime factorisation (Type, str) of input integer.


        Okay upto n = 3000235347293732ish (Quadrillions = 1000s of Trillion)
        It takes, approximately, 17 seconds to factor the following integer.
            Example: Prime factorisation of 3 Quadrillion ...
        3000235347293732 = 2^2 x 31 x 137 x 42643 x 4141573

        Another factor of 10 yields a memory error on my laptop.

    '''

    prime_divisor_list = prime_divisors(n)
    exponents = []
    for i in prime_divisor_list:
        exponents.append(exponent_of_divisor(n,i))

    prime_factorisation = ''
    for i,j in zip(prime_divisor_list,exponents):
        prime_factorisation += ('%s^%s x ' % (str(i),str(j)))

    #print('\n')
    return ('%s = ' % str(n)) + prime_factorisation[:-3]

# Exercise 3: Binary and Hex Representation.
# The first thing we need to do is write a function which determines the
# maximum power of a number k which is less than a number n.
# For example: we need to know how many powers of 2 go into an integer n
#              in order to find the binary representation for n.

# Max power less than...
def max_power_lessthan(n,m):

    '''
        This function returns the max power of an integer n that is less than
        or equal to an integer m.

    '''

    count = 0
    powerlessthan = True

    while powerlessthan == True:

        if (n ** (count + 1)) <= m:
            count += 1
        else:
            powerlessthan = False

    return count

# The four functions below allow us to switch between any 3 of these
# representations of integers.

# Decimal to binary...
def decimal_to_binary(n):

    # We will store the binary number as a string.
    binary_representation = ''

    # Find the max power of 2 less than n.
    max = max_power_lessthan(2,n)

    # Starting at max...
    for i in range(max,-1,-1):

        # Either append a 1 to the string in the ith place...
        if (2**i) <= n:
            binary_representation += '1'
            n = n - (2**i)
        # or append a 0.
        else:
            binary_representation += '0'

    return binary_representation

# Decimal to hexadecimal...
def decimal_to_hex(n):

    """
        This function inputs an integer (type int) and out puts the hexadecimal
        representation (type str)
    """

    hexadecimal_representation = ''
    max = max_power_lessthan(16,n)

    for i in range(max, -1, -1):

        x = n // (16 ** i)
        n = (n % (16 ** i))

        if x == 10:
            hexadecimal_representation += 'a'
        elif x == 11:
            hexadecimal_representation += 'b'
        elif x == 12:
            hexadecimal_representationp += 'c'
        elif x == 13:
            hexadecimal_representation += 'd'
        elif x == 14:
            hexadecimal_representation += 'e'
        elif x == 15:
            hexadecimal_representation += 'f'
        else:
            hexadecimal_representation += str(x)

    return hexadecimal_representation

# Binary to decimal...
def binary_to_decimal(binary):

    """
        This function inputs a binary string and outputs the corresponding
        integer.

    """

    # First turn the binary number into a list.
    binary = list(binary)
    l = len(binary)

    # Turn the elements of the list to integers.
    binary = [int(i) for i in binary]
    decimal_representation = 0
    exp = l - 1
    i = 0

    while exp >=0:
        decimal_representation = decimal_representation + (binary[i] * (2 ** exp))
        i = i + 1
        exp = exp - 1

    return decimal_representation

# Hexadecimal to decimal...
def hex_to_decimal(hexstring):

    """ This function inputs hexadecimal (type str) and out puts the decimal
        representation (type int)
    """

    hexnum = list(hexstring)
    L = len(hexnum)

    for i in range(0,L):
        if hexnum[i] == 'a':
            hexnum[i] = 10
        elif hexnum[i] == 'b':
            hexnum[i] = 11
        elif hexnum[i] == 'c':
            hexnum[i] = 12
        elif hexnum[i] == 'd':
            hexnum[i] = 13
        elif hexnum[i] == 'e':
            hexnum[i] = 14
        elif hexnum[i] == 'f':
            hexnum[i] = 15
        else:
            pass

    hexnum = [int(i) for i in hexnum]
    decimal_representation = 0
    exp = L - 1
    i = 0

    while exp >= 0:
        decimal_representation = decimal_representation + (hexnum[i] * (16 ** exp))
        i = i + 1
        exp = exp - 1

    return decimal_representation

# Exercise 4: Bit Manipulation.
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

# ------------------
# Exercise Sheet 3:
# ------------------

# Exercise 1: Euclidean Algorithm (Recursion).
def euclid_gcd(a,b):

    '''
        This function implements the ancient algorithm of Euclid in order
        to determine the greatest common divisor (gcd) of two integers.

        Input: integers a,b
        Output: greatest common divisor of a,b (type integer)

    '''

    r = (a%b)

    if r == 0:
        return b
    else:
        a = b
        b = r
        return euclid_gcd(a,b)

# Exercise 2: Extended Euclidean Algorithm (Not Recursion).
def extended_euclid_gcd(a,b):

    '''
        Input: Integers m,n (Type, int)
        Output: Integers a,b such that am + bn = gcd(m,n) (Type, int)

    '''

    # Initialize the outputs.
    s = 0           # s (old_s) will be the multiple of a.
    old_s = 1
    t = 1           # t (old_t) will be the multiple of b.
    old_t = 0
    r = b           # r (old_r) will be the greatest common divisor.
    old_r = a

    while (not (r == 0)):
        q = old_r // r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)


    # I have commented out three print statements because I call this
    # function in the linear_diophantine function. You can uncomment them
    # if you want to use this function by itself.

    #print("Bezout coefficients: ", (old_s, old_t))
    #print("[%s]*%s + [%s]*%s = gcd(%s,%s) = %s" % (old_s,a,old_t,b,a,b,old_r))
    #print("Greatest common divisor: ", old_r)
    return old_s, old_t

# Exercise 3: Linear Diophantine Equations.
def linear_diophantine(a,b,c):

    '''
        Returns solutions (if they exist) to the linear Diophantine equation:
            ax + by = c.

        All variable names match those in the notes of Week 1 and Week 2.

    '''

    solution_exists = False

    # First check if gcd(a,b)|c
    if (c % euclid_gcd(a,b)) == 0:
        solution_exists = True
        n,m = extended_euclid_gcd(a,b)
        d = c/euclid_gcd(a,b)
    else:
        pass


    # Return the information
    if solution_exists == False:
        return 'No solution exists'
    else:
        x = d*n
        y = d*m
        return 'x = %d and y = %d is a solution to the equation.' % (x,y)

# Exercise 4: Search for Solutions to Non-Linear Diophantine Equations.
# Search for x in [0,100]
# for x in range(0,101):
#     # For each value of x try y in [0,100]
#     for y in range(0,101):
#
#         # For each pair check if the equation holds...
#         if (x**3)+(y**3) == 1729:
#             # If x,y is a solution, then print x,y
#             print(x,y)
#
#         # If x,y aren't solutions, then do nothing.
#         else:
#             pass

# Exercise 5: XOR-binary strings.
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


# Exercise 6: XOR Single-Byte Encryption.
def XOR_cipher(plaintext, key):

    '''
        Input: plaintext (type str) and key (type str).

        Output: Plaintext XOR'd against the (repeated) key printed in
                hex encoding to "look pretty".

        Note: This does not need a "mode" argument as it is perfectly
              symmetric. Encryption is exactly the same algorithm as
              decryption.

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
    ciphertext_ASCII = [x^ord(y) for x,y in zip(plaintext,repeated_key)]
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

# ------------------
# Exercise Sheet 4:
# ------------------

# Exercise 1: Algebraic Equations Modulo m.
#... coming soon.

# Exercise 2: Modular Inverse.
# This is the same code as the extended Euclidean algorithm above. Except it
# returns a different value.
def euclid_modular_inverse(a,p):

    '''
        Input: Integers a,p (Type, int)
        Output: Inverse of a mod p. (Type, int).

        Note: This code assumes a < p and that the inverse exists. Note the
        function will return "None" if a is not invertible mod p.

        Note: This function employs the extended Euclidean algorithm to find
        the gcd and inverse.

        Note: This function assuemes neither input is 0.


    '''

    # Initialize the outputs.
    s = 0
    old_s = 1       # old_s will be the inverse of a.
    t = 1
    old_t = 0
    r = p
    old_r = a       # old_r is the greatest common divisor of a,p

    while (not (r == 0)):
        q = old_r // r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)

    # We want a representative for the inverse of a in [0,p-1]. In the case
    # that old_s is negative, we have to add p to it in order to get a positive
    # representative for the coset.
    if old_s < 0:
        old_s += p
    else:
        pass

    # Return value depends on whether a is invertible.
    if old_r == 1:
        return old_s
    else:
        print("%s not invertible mod %s" % (a,p))
        return None

# Exercise 3: Pollard's (p-1) Algorithm.
def pollard_prime_hunter(n):

    '''
        This function employs Pollard's algorithm to find a prime divisor
        of an integer. See the notes for Week 4 for an explanation of
        Pollard's algorithm.

        Note: this algorithm has infinite loops! If we don't change the base
              over which we are calculating, then the algorithm will not stop
              when the input is (for example) 65 or 85.

              In order to fix this, I have written the code to change base
              if this loop is detected. I am not sure of the extent to which
              this algorithm will find a divisor in finite time. Does every base
              have numbers for which this infinite loop will happen? Will it
              happen on multiple bases?

              I imagine something along the following lines is known:

                Given an input n. There exists a finite set of primes and
                and integer k_max such that a prime-divisor of n will be found
                with this test using all choices of paramters from the list
                of primes (for the base) and k<k_max for the exponent.

    '''

    # Rather than calculating the factorial every iteration, we can simply
    # update the value L by raising it to the kth power. Reducing mod n
    # at each stage as this keeps the numbers below n.

    # We need some initial parameters to start the test:

    # Primes to choose the base from.
    primes = sieve_eratosthenes(300)

    # Some counter to say we have run out of primes.
    i = 0
    i_break = len(primes)-1

    # Pick the first base.
    base = primes[i]
    L = base

    # An exponent to start on.
    k = 1

    # Set a Boolean to decide when to stop the algorithm.
    prime_found = False

    # While no prime divisor has been found we loop.
    while prime_found == False:

        # Do the precalculation for the GCD
        L = (L ** k) % n
        M_k = (L - 1) % n

        # Calculate the GCD
        G_C_D = euclid_gcd(M_k,n)

        # Print the data of each stage. As presented in the notes.
        #print 'k = %d, %d^(%d!) - 1 = %d mod %d, gcd(%d,%d) = %d' % (k, base, k, M_k,n,M_k,n,G_C_D)

        # Check if a prime divisor has been found.
        if isit_prime(G_C_D) == True:
            prime_found = True
            return G_C_D

        # If G_C_D is composite, then we can simply run the test again with
        # n = G_C_D; as a prime divisor of G_C_D will be a prime divisor of n.

        elif ((G_C_D > 1) and (i < i_break)):

            # Which numbers go into this part of the code?
            print(n,k,base)

            # In order to run the test with n = G_C_D, we just reset the
            # initial parameters. However, this time we change the base of
            # the exponentiation.
            n = G_C_D

            # Go to the next base:
            i = i + 1
            base = primes[i]
            L = base
            k = 1

        else:
            k += 1

        # Break if loop goes on for too long...
        if k > 100:
            return 'No prime divisor. Note: this does not mean the integer is prime.'
            quit()

# Exercise 4: Frequency Analysis
def character_frequency_score(text):

    """
        Input: Text to be scored. Type, string.

        Output: Score of the text. Type, float.

        This function can be used to compare the "english-ness" of strings
        with equal length. The highest possible score, for a fixed length
        string, is a string of all ' ' spaces. Obviously, this is not English.

        In theory this function will be used to pick an english string out of random
        noise; that is, out of a collection of strings of apparently random character
        distribution. Thus strings of constant characters should not arise; as they
        are extremely unlikely to result from encryption of an english sentence.

        Among these strings, English should score highest; as a string written
        in English will have more letters of higher weight and thus have
        a higher score.

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


    l = len(text)
    score = 0
    for i in range(0,l):

        if text[i] in letter_frequencies:
            score = score + letter_frequencies[text[i]]
        else:
            pass

    return score

# Exercise 5: Break Single-Byte XOR
def XOR_cipher_break(ciphertext):

    """
        Input: Ciphertext presented in HEX (type string)

        Output: key and plaintext (type string)

        This function brute forces all 256 single-byte keys. Scoring each
        decryption according to the "English-ness" of the text. This function
        returns the text and key with the highest score.

        Note: this function assumes the ciphertext is given in hexadecimal
              representation. If this is not true, then some massaging of the
              data will have to be done before this function can be applied.

    """

    # First we need to turn the ciphertext from HEX into a list of bytes.
    ciphertext_binary = decimal_to_binary(hex_to_decimal(ciphertext))
    ciphertext_bytes = binary_to_bytes(ciphertext_binary)

    # Initialize some parameters to keep track of highest score decryption.
    max_score = 0
    max_score_key = 257
    max_score_plaintext = ''

    # Brute force each possible key.
    for key in range(0,256):

        key_byte = decimal_to_binary(key)

        plaintext = []

        for x in ciphertext_bytes:

            XOR_decrypt_byte = binary_XOR(x,key_byte)
            XOR_decrypt_deci = binary_to_decimal(XOR_decrypt_byte)
            XOR_decrypt = chr(XOR_decrypt_deci)

            plaintext.append(XOR_decrypt)

        plaintext_string = ''
        for x in plaintext:
            plaintext_string += x

        # Score this guess
        key_score = character_frequency_score(plaintext_string)

        # Check this score against previous max. Update accordingly.
        if key_score > max_score:
            max_score = key_score
            max_score_key = key
            max_score_plaintext = plaintext_string
        else:
            pass

    return max_score_plaintext, 'Key: This text was encrypted with key %s' % chr(max_score_key)


# x = '0a3c26733b3632373a3d74733c262773273c7320362773373c243d73203c3e36733c3573273b3a20733d32272621323f7320233f363d373c216c'
#
# print(XOR_cipher_break(x))

# ------------------
# Exercise Sheet 5:
# ------------------

# Note: the computational difficulty in the implementation of the Miller-Rabin
#       test is the difficulty in calculating the large exponentials required.
#       You can try to write your own function. Or you can use the in-built
#       pow() function of the Python standard library.
#       This function uses "binary exponentiation" in order to get the
#       speeds that it achieves.

# Exercise 0: Exponentiation Modulo m.
def binary_exponentiation(a,e,m):

    '''
        Calculate a**e mod m using binary exponentiation. Same input/output
        as pow() from the Python standard library.

        Speed of Python standard library function is siginficantly better than
        my own implementation.

    '''

    exponent_binary = list(decimal_to_binary(e))
    exponent_binary.reverse()
    L = len(exponent_binary)

    # Initialize the product
    product = 1

    # Set a counter for the while-loop
    i = 0
    while i < L:

        # Update product according to the current bit of the exponent.
        if exponent_binary[i] == '1':
            product = (product * a) % m
        else:
            pass

        # Now square a
        a = ((a**2) % m)

        # Move to the next bit
        i += 1

    return product

# Exercise 1: Fermat Primality/Composite Test.
def fermat_composite_test(n,a):

    '''
        Perform Fermat primality test on integer n with base a.

        This functions returns Boolean True if n is deemed to be composite
        Otherwise it returns None.

    '''

    # Check that n,a are coprime
    if euclid_gcd(n,a) == 1:
        pass
    else:
        raise NameError('%d and %d are not coprime. Fermat does not apply' % (a,n))
        return None

    # Carry on with the test.
    test_integer = pow(a,n-1,n)
    #print(test_integer)

    if test_integer == 1:
        return 'The integer %d is a base %d pseudoprime. \nFermat Test inconclusive; %d maybe prime or a Fermat-liar.' % (n,a,n)
    else:
        return True

# Exercise 2: Miller-Rabin.
def miller_composite_test(n,a):

    '''
        Performs Miller's test for compositeness of n by testing at base a.

    '''

    # Check that n,a are coprime.
    if euclid_gcd(n,a) == 1:
        pass
    else:
        raise NameError("%d and %d are not coprime. Miller's Test does not apply" % (a,n))
        return None

    # If we show n to be composite, we want to stop the function. We can use
    # this Boolean to do that.
    composite = False

    # Until we have either (i) shown n to be composite or (ii) run out of
    # square-roots to calculate, we want to keep running the test.

    # The number of square-roots allowed is
    k = exponent_of_divisor(n-1,2)

    # Let's introduce a variable to count the number of square-roots.
    j = 0

    # We can use an 'and' to get the correct "break logic"
    while (composite == False) and (j <= k):

        # Print statement to see how many steps were needed.
        #print "Miller test at base %d running %d th time." % (a,j)

        # Exponent of a for this round of the test.
        e = ((n-1)/(2**j))
        #print "Exponent has been calculated."
        #print "Now calculating the square root."

        # Calculate the test integer.
        test_integer = pow(a,e,n)       # Note: Python standard library pow()
                                        # is optimized much more than my custom
                                        # implementation of binary exponentiation.
                                        # Speed difference is significant for
                                        # large i.e. > 2^64 integers.

        print test_integer
        # Now we to decide whether or not to continue running the test:
        if test_integer == 1:

            # In this case we can't determine the compositeness.
            # So we move onto the next round.
            j = j + 1

        elif test_integer == (n-1):

            # In this case we can do nothing. We can't take another square root.
            # We set j > k as this breaks the while-loop i.e. stops the test.
            j = k+1

        else:

            # If we get anything other than +1 or -1 = n-1 (mod n), then we
            # may conclude that n is composite
            composite = True

    # With the test complete, we need to decide what to return.
    if composite == True:
        #print('%d is composite.' % n)
        return True
    else:
        #print "Miller's Test is inconclusive: %d was not shown to be composite with base %d." % (n,a)
        # Even though the test is inconclusive, I still choose to return False
        # as we will refer to this value in the Miller-Rabin prime test function.
        return False

# Finding examples where Miller's test fails to detect compositeness.
# primes = [2,3,5,7,11]
#
# for x in range(20,10000):
#
#     for p in primes:
#
#         if not euclid_gcd(x,p) == 1:
#             pass
#         elif (miller_composite_test(x,p) == False) and (isit_prime(x)==False):
#             print "Miller's Test is inconclusive: %d was not shown to be composite with base %d." % (x,p)
#         else:
#             pass


# Exercise 3: Deterministic Miller-Rabin.
def miller_rabin(n):


    '''
        This function determines whether the input integer is prime.

        It is deterministic for integers less than 64-bits.
        That is, deterministic for integers smaller than 2^64.

        In the paper "Strong Pseudoprimes to the First Eight Prime Bases"
        Yupeng Jiang and Yingpu Deng give us a sufficient set of primes
        on which we can give a DETERMINISTIC primality test using the
        Miller-Rabin test.

    '''

    # Jiang and Deng prove it suffices to check the following bases, in the
    # case that the input n < 2^64.
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]

    # Run a check for n in the list primes.
    if n in primes:
        return True
    else:
        pass

    # Again we set a Boolean and counter for use in stoping the test.
    composite = False

    # This time the counter will index the element of the list primes that
    # we are currently using as the base for the test.
    i = 0

    # Run the test while composite still false and there are bases left to check.
    while ((composite == False) and (i < len(primes))):

        #print 'Base test = ', primes[i]

        # In order to run the test, we must first check whether or not
        # the base is coprime to the integer.
        if euclid_gcd(n,primes[i]) == 1:
            # In this case, the test can run.
            pass
        else:
            # If they share a divisor, then either n = primes[i]
            # or n is composite. We have already checked for n in primes[i]
            # so we may conclude n is composite.
            composite = True
            break

        #print "Now running Miller's test at base %d" % primes[i]
        # Now we can run Miller's test.
        miller_test_value = miller_composite_test(n,primes[i])

        if miller_test_value == True:

            # This means the number is composite.
            composite = True

        else:
            # In this case we don't yet know about the primality.
            i = i + 1

    # Decide what to return
    if composite == True:
        # In this case number is NOT prime.
        return False
    else:
        return True

# Speed test of naive prime test vs. miller-rabin prime test.

# Note: 2**64 = 18446744073709551616.
#       The prime nearest to 2**64 is 18446744073709551629
#       Miller-Rabin determines this in 0.0003seconds.
#       I don't want to wait for the naive test.

# x = 18446744073709551629
# y = 1217 * 1151
# z = 1003349 * 1002653
# w = 100002059 * 100003721 # < 2**64
# a = 100002059
#
# # Miller-Rabin
# start = timeit.default_timer()
# print miller_rabin(x)
# finish = timeit.default_timer()
# time = finish - start
# print time
#
# # Naive
# start = timeit.default_timer()
# isit_prime(x)
# finish = timeit.default_timer()
# time = finish - start
# print time

# Observation: Miller-Rabin test is significantly better than the naive test
#              when the input integer has large prime factors. If the input
#              has small prime factors, then the guess check method will come
#              across them fast enough. If the input only has large prime factors
#              it takes longer to find them; whereas, the Miller-Rabin method
#              is not sensitive to the size of the factors; only the congruences
#              the integer satisfies.


# # Searching for examples of Elliptic Curves over small primes.
#
# # Primes for testing:
# base = [5,7,11]
#
# # Define the coefficients
# for a in range(0,5):
#     for b in range(0,5):
#
#         # Next choose the prime we are working over
#         for p in base:
#
#             # Check the descriminant non-zero
#             if not (((4*(a**3) + 27*(b**2)) % p) == 0):
#
#                 # Count points
#                 count = 1
#
#                 # Store points
#                 points = ['infinity']
#
#                 # Find points
#                 for x in range(0,p):
#                     for y in range(0,p):
#
#                         # Reduce coefficients mod p
#
#                         if ((y**2)%p) == (((x**3)+ a*x + b) % p):
#                             count += 1
#                             points.append((x,y))
#                         else:
#                             pass
#
#                 print 'On the elliptic curve: y^2 = x^3 + %dx + %d modulo %d' % (a,b,p)
#                 print 'There are %d points' % count
#                 print 'They are the following: '
#                 print points
#
#                 print '\n\n\n'


# ------------------
# Exercise Sheet 6:
# ------------------

# Exercise 1: Caesar Cipher

# We can assign the letters to the alphabet according to the index of the
# letter in the following list:
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar_cipher(plaintext,key,mode):

    '''
        Inputs:   (i) Plaintext: type string
                 (ii) Key for encryption: type string - one integer in the
                      range [0,25]
                (iii) Mode: either 'e' (encryption) or 'd' (decryption)

        Output: Depends on the value of mode. Either encrypted or decrypted
                text. Encryption scheme: Caesar (i.e. shift) cipher. Shifted
                by the input key.


    '''
    # Need the alphabet to make the change between letters and numbers.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Take the plaintext string and turn it into a list:
    plaintext_list = list(plaintext)
    L = len(plaintext_list)

    # Substitute letters for numbers
    for i in range(0,L):
        number_substitution = alphabet.index(plaintext_list[i])
        plaintext_list[i] = number_substitution

    # Depending upon mode: encryption or decryption
    if mode == 'e':
        for i in range(0,L):
            plaintext_list[i] = (plaintext_list[i] + key) % 26

    elif mode == 'd':
        for i in range(0,L):
            plaintext_list[i] = (plaintext_list[i] - key) % 26

    else:
        return 'Incorrect mode specified. Do you want to encrypt or decrypt? ("e"/"d")'

    # Substitute back into letters from the ciphertext numbers.
    ciphertext = ''
    for x in plaintext_list:
        ciphertext += alphabet[x]

    return ciphertext

# Exercise 2: Affine Cipher
def affine_cipher(plaintext,key,mode):

    '''
        Inputs:   (i) Plaintext: type string
                 (ii) Key for encryption: type list - pair of integers
                      [a,b]: where gcd(a,26)=1 and b in [0,25]
                (iii) Mode: either 'e' (encryption) or 'd' (decryption)

        Output: Depends on the value of mode. Either encrypted or decrypted
                text. Encryption scheme: Caesar (i.e. shift) cipher. Shifted
                by the input key.

    '''
    # Need the alphabet to make the change between letters and numbers.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Set the required parameters:
    a = key[0]
    b = key[1]
    a_inverse = 1

    # Check if key is valid:
    if euclid_gcd(a,26) == 1:
        a_inverse = euclid_modular_inverse(a,26)
    else:
        return 'Key is not valid. The first element of the key must be coprime to 26.'

    # decryption shift
    c = (a_inverse*b) % 26

    # Take the plaintext string and turn it into a list:
    plaintext_list = list(plaintext)
    L = len(plaintext_list)

    # Substitute letters for numbers
    for i in range(0,L):
        number_substitution = alphabet.index(plaintext_list[i])
        plaintext_list[i] = number_substitution

    # Depending upon mode: encryption or decryption
    if mode == 'e':
        for i in range(0,L):
            plaintext_list[i] = ((a*plaintext_list[i] + b) % 26)

    elif mode == 'd':
        for i in range(0,L):
            plaintext_list[i] = ((a_inverse*plaintext_list[i] - c) % 26)

    else:
        return 'Incorrect mode specified. Do you want to encrypt or decrypt? ("e"/"d")'



    # Substitute back into letters from the ciphertext numbers.
    ciphertext = ''
    for x in plaintext_list:
        ciphertext += alphabet[x]

    return ciphertext

# Exercise 3: Vigenere Cipher
def vigenere_cipher(plaintext,key,mode):

    '''
        Input:      (i) Plaintext: type string
                   (ii) Key: type string
                  (iii) Mode: type string. If encrypting, then 'e'.
                              If decrypting, then 'd'.

        Output: type string. Plaintext or ciphertext depending upon the mode.

        Encryption method: Vigenere cipher. If they key is shorter than the
                           message, then it is repeated as many times as
                           necessary in order to be equal to the length of the
                           plaintext(message).

    '''
    # Need the alphabet to make the change between letters and numbers.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # We need to repeat the key as many times as required to cover the
    # entire plaintext.
    plaintext = list(plaintext)
    key = list(key)

    L_message = len(plaintext)
    L_key = len(key)

    q = L_message/L_key
    r = L_message % L_key
    # repeat the key...
    repeated_key = q*key + key[0:r]

    # Encrypt or decrypt depending upon the mode
    ciphertext = []

    # If encrypting...
    if mode == 'e':

        for i in range(0,L_message):

            plaintext_index = alphabet.index(plaintext[i])
            key_index = alphabet.index(repeated_key[i])
            cipher_index = (plaintext_index + key_index) % 26

            ciphertext.append(alphabet[cipher_index])

    # elif decrypting...
    elif mode == 'd':

        for i in range(0,L_message):

            plaintext_index = alphabet.index(plaintext[i])
            key_index = alphabet.index(repeated_key[i])
            cipher_index = (plaintext_index - key_index) % 26

            ciphertext.append(alphabet[cipher_index])

    # else error...
    else:
        return 'You did not specifiy a correct mode of operation ("e"/"d")'

    # Substitute back into letters from the ciphertext numbers.
    ciphertext_string = ''
    for x in ciphertext:
        ciphertext_string += x

    return ciphertext_string


# Exercise 4: Break Them All

# Note: due to the statistical nature of the "English-ness" test these
#       functions do not work well if the plaintext is short. Roughly speaking
#       these functions will work if the plaintext is greater than 50 characters.
#       Otherwise, they may not return the correct plaintext.
#       One remedy for this is to write a function that looks for common
#       words in the strings; rather than focusing on the letter frequency.
#       This should return English in short strings; but you have to
#       import an (English) dictionary.

# This function will break the Caesar cipher.
def caesar_cipher_break(ciphertext):

    '''
        Input: ciphertext written in the English alphabet. Type, string.

        Output: plaintext. Type, string.

        Note: due to the statistical nature of the "English-ness" test, the plaintext
              needs to be sufficiently large in order for this to work.

    '''


    # Initialize some parameters to keep track of highest score decryption.
    max_score = 0
    max_score_key = 0
    max_score_plaintext = ''

    # Brute force all the keys.
    for key in range(0,26):

        # Decrypt with this key...
        plaintext = caesar_cipher(ciphertext,key,'d')
        # ... score the decryption.
        score = character_frequency_score(plaintext)
        if score > max_score:
            max_score = score
            max_score_key = key
            max_score_plaintext = plaintext
        else:
            pass

    return max_score_plaintext, max_score_key

# Break the affine cipher
def affine_cipher_break(ciphertext):


    # Initialize some parameters to keep track of highest score decryption.
    max_score = 0
    max_score_key = 0
    max_score_plaintext = ''

    # Brute force all keys:
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for j in range(0,26):

            # Define the key.
            key = [i,j]

            # decrypt with this key
            plaintext = affine_cipher(ciphertext,key,'d')

            # score the decryption
            score = character_frequency_score(plaintext)

            if score > max_score:
                max_score = score
                max_score_key = key
                print key[0],key[1]
                max_score_plaintext = plaintext
            else:
                pass

    return max_score_plaintext, 'Key: a = %d and c = %d' % (max_score_key[0],max_score_key[1])

# ------------------
# Exercise Sheet 7:
# ------------------

# Exercise 1: Fast Exponentiation
# Code written as Exercise 0 of Sheet 5.

# Exercise 2: Pseudo-Randon Number Generator.
# This code will implement the Linear Congruential PRNG.
def lcprng():

    '''
        This function uses a seed obtained from the time at time to of exectution
        to generate a sequence of 10 random numbers. The process of generating the
        numbers is known as Linear Congruential Generation.

    '''


    # We need to determine a seed value to start the process. I will use the
    # timeit module to access the time and use some of the digits from that
    # number as the seed value.
    seed_time = timeit.default_timer()
    seed = int((seed_time - int(seed_time))* (10 ** 10))

    # Store the sequence
    random_numbers = []

    # Use the LCPRNG algorithm with the following paramters:
    a = 6364136223846793005
    c = 1442695040888963407         # These parameters were used by Knuth.
    m = (2**63)                     # No sense arguing with him!

    # Set a counter for the loop.
    k = 1

    # Loop through the algorithm.
    while k < 10:

        seed = (a*seed + c) % m
        random_numbers.append(seed)
        k += 1

    return random_numbers

# In order to get a prime number large enough for RSA to be secure, we need to
# generate primes of at least 1000bits or 150 (decimal) digits.
def rng():

    # Use the previous function to obtain our random sequence
    random_numbers = lcprng()

    # Build our large number from random numbers generated.
    large_number = ''

    for x in random_numbers:
        large_number += str(x)

    large_integer = int(large_number[0:100])
    return large_integer

#Exercise 3: Finding Large Prime Numbers.
# Now we have a way of producing large integers. But we want large primes
# not just large integers.
def random_prime_generator():

    '''
        This function returns a random prime number which is 100 digits long.
        These primes are around the correct length for the lowest security of
        public-key crypto schemes like RSA and DHKE.

        Since the Miller-Rabin primality test is probablistic and the number
        is too large for a deterministic test; the primality is only
        guaranteed with a particular probablity. We run Miller-Rabin for 12
        different bases so the probablity of a false prime is (1/4) ^ 12. This
        is approximately (but not exactly) zero.

        The Prime Number Theorem gives us an estimate on the distribution of
        primes. When we are out this far a long the number line, the PNT
        suggests we will come across a prime number (on average) once every
        twenty odd-numbers i.e. 5% of the time. So we can pick a random number
        and increment until we get a prime; assured by the PNT that we will
        not have to do too many increments until we find a prime number.

    '''
    # Seed our prime search with a random number.
    seed = rng()

    # Set the prime boolean to break the search loop.
    prime = False

    # The count is just to know how many increments are needed to find
    # a prime from the seed.
    count = 0

    # Increment the seed until the prime is found.
    while prime == False:

        # Use Miller-Rabin to test for primality.
        if miller_rabin(seed) == False:
            seed += 1
            count += 1
        else:
            prime = True
    #print(count)
    return seed



# ----------------------------------------
# Exercise Sheet 8: Primitive Roots mod p
# ----------------------------------------

# Exercise 1: Primitive Roots
def primitive_root(prime):

    """
        This function returns the least primitive root
        modulo the input prime number. Make sure the
        input is prime.

        This algorithm relies on the ability to factor
        phi(p) = p-1. Therefore it will become in effective
        if the prime becomes too large.

        Note: for some reason this does not interact
              well with the miller_rabin test.
              The prime_divisors function needs a primality
              test; it doesn't like my implementation of
              Miller-Rabin.

        Note: the output is a generator for the group of
              multiplicative units modulo the input prime.

    """

    # Edge case
    if prime == 2:
        return 1

    # Euler totient.
    phi = prime - 1

    # Prime divisors of phi(p) = p-1
    prime_divisor_list = prime_divisors(phi)

    # Exponents to test.
    exponents = []
    for p in prime_divisor_list:
        e = (phi/p)
        exponents.append(e)
    L = len(exponents)

    # Test 2 first
    a = 2
    # and then increment until primitive found
    primitive_found = False

    # Note: Gauss proved this while-loop will stop!
    while primitive_found == False:

        # Don't yet know a is NOT primitive...
        a_primitive = True
        i=0
        while (a_primitive == True) and (i < L):

            # Test the exponents
            for e in exponents:

                # Calculate the test integer
                test = binary_exponentiation(a,e,prime)


                if test == 1:
                    a_primitive = False
                    # In this case, we can break out of the for-loop
                    break

                i+= 1


        if a_primitive == True:
            primitive_found = True
        else:
            a = a + 1

    # Return the current a
    return a


# Plot phi(x)/x to get a sense of the asymptotic behaviour of the density of
# primitive roots.

# start = timeit.default_timer()
# x = sieve_eratosthenes(100000)
#
# def phi(a):
#     b=a-1
#     c=0
#     while b:
#         if not euclid_gcd(a,b)-1:
#             c+=1
#         b-=1
#     return c
#
# y = [(phi(i-1)/float(i-1)) for i in x]
# finish = timeit.default_timer()
# print int(finish - start)
#
# plt.title("Ratio of primitive roots mod p: phi(p-1)/(p-1)")
# plt.ylabel("phi(p-1)/(p-1)")
# plt.xlabel("p: prime")
# plt.plot(x,y, 'o')
# plt.ylim((0,1))
# plt.xlim((-0.5,100000))
# plt.show()

# Exercise 2: Calculate the order of a mod p
def order(a,p):

    count = 1
    a_new = a

    order_obtained = False

    while order_obtained == False:

        if a_new == 1:
            order_obtained = True
        else:
            a_new = (a_new * a) % p
            count = count + 1

    return count

# for i in range(1,7):
#     print i,order(i,7)

# Exercise 3: Calculate the index of an integer modulo a prime.
def discrete_logarithm(a,p,*g):


    """
        This function returns the smallest integer x which solves the
        equation:

                    r**x == a mod p

        where is a primitive root modulo p.

        The third argument is optional. If the user wants to pick the primitive
        root with which to calculate the discrete logarithm, then they can
        provide it in the optional third argument. If no primitive root
        is passed, then the least positive root is used to calculate the
        discrete logarithm.

    """

    # Make sure a is represented by the unique positive integer
    # less than p in the congruence class
    a = a % p

    # Check which primitive root we are using.
    r = primitive_root(p)
    r_new = r

    # If no argument is passed, use the least positive primitive root...
    if g == ():
        pass
    # ... if the least positive primitive root is passed, use that...
    elif g[0] == r:
        pass
    # ... if a primitive root is passed, we can use that...
    elif (order(g[0],p) == p-1):
        r = g[0]
        r_new = g[0]
    # ... Otherwise, not sure what to make of 3rd argument. Just use least positive primitive.
    else:
        print "The third argument is not a primitive root modulo %d. So we used the least primitive root %d" % (p,r)


    # Initialize variables
    index = 1
    index_found = False

    # Deal with a = r as an edge case
    if a == r:
        return 1
    else:
        pass

    while index_found == False:

        r_new = (r*r_new) % p

        if r_new == a:
            index += 1
            index_found = True
        else:
            index +=1

    return index


# -------------------------------------
# Exercise Sheet 9: Quadratic Residues
# -------------------------------------

# Exercise 1: Compute Legendre symbol.
def legendre_symbol(a,p):

    """
        This function uses the identity

                    (a|p) = a**((p-1)/2) mod p

        and binary exponentiation to calculate the Legendre symbol.

    """
    a = a % p
    e = ((p-1)/2)
    symbol = binary_exponentiation(a,e,p)

    if symbol == 1:
        return 1
    elif symbol == p-1:
        return -1
    else:
        return "Something went wrong. Sorry."

# --------------------------------------
# Exercise Sheet Aleph: Elliptic Curves
# --------------------------------------

class EllipticCurve:

    """
        An instance is determined by three integers: a,b,p.

            p must be a prime greater than 2
            a,b can be any integers which satisfy the following congruence

                4a^3 + 27b^2 =/= 0 mod p.

        Instances of this class are Elliptic curves of the form:

                y^2 = x^3 + ax + b

        over a fixed prime p.

        Examples:

            - E = EllipticCurve(0,-1,229)
            - E = EllipticCurve(0,-1,457)
            - E = EllipticCurve(-5,8,37)
            - E = EllipticCurve(-5,2,11)
            - E = EllipticCurve(133,811,929)



    """

    # Define the data which is required to create an instance of this class.
    def __init__(self,a,b,p):

        if (((4*(a**3) + 27*(b**2)) % p) == 0):
            print('This curve is singular and hence not an elliptic curve.')
            self.singular = True
        else:
            self.a = a
            self.b = b
            self.p = p
            self.field = ('This elliptic curve is defined over GF(%d)' % p)
            self.singular = False

    def Print(self):

        """
            This method prints the equation as a string.

        """



    def Points(self):

        """
            This method returns the list of points on the elliptic curve.

        """

        # Initialize the output.
        points = [float('inf')]

        # Set range of values to check.         # We can use the symmetry of
        y_range = ((self.p - 1)//2) + 1         # of the curve to cut-down on
                                                # the search.

        # Brute force search for points on the elliptic curve.
        for x in range(0,self.p):
            for y in range(0,y_range):

                if ((y**2)%self.p) == (((x**3)+ self.a*x + self.b) % self.p):

                     point = [x,y]
                     points.append(point)
                     if y == 0:
                         pass
                     else:
                        point_symmetry = [x,self.p-y]
                        points.append(point_symmetry)

        return points

    def GroupOrder(self):

        """
            This method returns the order of the group of points on
            the elliptic curve; it simply calculates all the points
            using the points method and measures the length of that
            list.

            Note: this count includes the point at infinity.

        """

        # If the curve is singular, then there is no group structure
        # to determine the order of.
        if self.singular == True:
            return None
        else:
            return len(self.Points())


    def Generator(self):

        """
            This method tries to find a generator for the group of points
            on the elliptic curve.

        """

        # Get the list of points without the point at infinity.
        points = (self.Points())[1:]
        L = len(points)

        # Set a counter to go through the points.
        i = 0

        # Set a boolean to stop the search.
        found_generator = False

        # Search for a generator.
        while (found_generator == False) and (i < L):

            p = points[i]
            P = EllipticCurvePoint(self,p[0],p[1])

            order = P.PointOrder()

            # If the order of the element matches the order of the group
            # then we have succeded in finding a generator.
            if order == (L+1):
                generator = P
                found_generator = True
            else:
                i = i + 1

        # Decide what to return.
        if found_generator == True:
            return generator
        else:
            return None

    def IsomorphismClass(self):

        """
            This function returns the isomorphism class of the group
            of points on the elliptic curve.

            It seems that the possible group structure is constrained a lot.
            There is a theorem saying there are only two distinct cyclic
            subgroups in the decomposition. Learn this and code it.

        """

        # The isomorphism class depends on the order:
        order = self.GroupOrder()

        # If the order is prime, it must be cyclic.
        if miller_rabin(order) == True:
            g = self.Generator()
            return 'The group of points is a cyclic group isomorphic to Z/%dZ. \n The point (%d,%d) generates the group.' % (order,g.x,g.y)
        else:
            pass

        # If we can find a generator, then we know the structure.
        g = self.generator()
        if g == None:
            pass
        else:
            return 'The group of points is a cyclic group isomorphic to Z/%dZ. \n The point (%d,%d) generates the group.' % (order,g.x,g.y)


        # When all else fails we can use the fundamental theorem of finite
        # Abelian groups in order to determine the structure of the group.

        # # First we need to find the prime factorisation of the order.
        # prime_divisor_list = prime_divisors(order)
        # exponents = []
        # for i in prime_divisor_list:
        #     exponents.append(exponent_of_divisor(order,i))
        #
        # prime_factorisation = zip(prime_divisor_list,exponents)


    def CyclicSubGroups(self):

        """
            Determine which subgroups arise in the group of points
            on the elliptic curve by considering the elements
            of the individual points.

            Unsurprisingly, this method takes a long time to run.
            Over the prime p = 4973; it didn't take long to find
            the order of the group, nor to determine the group is
            cyclic. But it did take a minute or so to find the
            order of all elements in the group.

        """

        points = self.Points()[1:]

        # This list contains the orders of elements in the group
        cyclic_subgroups = []

        for p in points:

            # Define the point on the elliptic curve and calculate the order
            P = EllipticCurvePoint(self,p[0],p[1])
            order = P.PointOrder()

            # Place in list; depending on whether element of this order
            # had been found previously.
            first_element = True

            for i in range(0,len(cyclic_subgroups)):
                if cyclic_subgroups[i][0] == order:
                    first_element = False
                    cyclic_subgroups[i][1].append(P)

            if first_element == True:
                cyclic_subgroups.append([order,[P]])

        return cyclic_subgroups


    @staticmethod
    def PointAddition(P,Q):

        """
            Input: P,Q as instances of EllipticCurvePoint.
            Output: P + Q as an instance of EllipticCurvePoint.

        """

        if not P.ec == Q.ec:
            return "These points are on different curves!"
        else:
            pass

        # First consider the case the points are equal.
        if (P.x == Q.x) and (P.y == Q.y):
            return P.PointDouble()

        # Next we deal with the case P = - Q
        elif (P.x == Q.x) and ((P.y == P.prime - Q.y) or (Q.y == P.prime - P.y)):
            return float('inf')

        # If they aren't equal and aren't inverses of each other then we just add them
        else:

            # We need some parameters for the addition formulae:
            D = euclid_modular_inverse(Q.x - P.x, Q.prime)
            s = (D*(Q.y - P.y)) % Q.prime

            x_sum = ((s**2) - P.x - Q.x) % P.prime
            y_sum = (s*(P.x - x_sum) - P.y) % P.prime

            return EllipticCurvePoint(P.ec,x_sum,y_sum)




    def CurveData(self):

        """
            This method presents all of the data about the elliptic curve
            in a human-reader friendly form.

            What else should I say?
                    - Isomorphism class of the group
                            -- E either cyclic or product of two cyclic
                    - j-invariant
                    - determinant
                    - Is it CM?
                    - add prompt for list of all points on curve

            This function performs a lot of work multiple times.
            So this can easily be made more efficient by doing the
            work once!

        """
        if self.singular == True:
            return "This curve is singular and hence not an Elliptic curve."

        # Look for a generator.
        g = self.Generator()

        print("\n\nThe elliptic curve defined by:\n")
        print("       E: y^2 = x^3 + %dx + %d mod %d\n" % (self.a,self.b,self.p))
        print("is a finite Abelian group of order %d.\n" % self.GroupOrder())

        # If Elliptic curve has only the point at infinity
        if self.GroupOrder() == 1:
            print("E is cyclic and generated by the point at infinity.")

        # If there is no generator
        elif g == None:
            print("The group E is not cyclic.")

        # If there is a generator
        else:
            print("The point (%d,%d) has order %d and hence generates E.\n" % (g.x,g.y,self.GroupOrder()))
            print("From this we may conclude that E is isomorphic to: Z/%dZ" % self.GroupOrder())

        element_order_data = self.CyclicSubGroups()
        L = len(element_order_data)
        print("\nE has elements of the following orders: \n")
        print("There is 1 element of order 1")
        for i in range(0,L):
            order = element_order_data[i][0]
            number_elements = len(element_order_data[i][1])
            print("There are %d elements of order %d" % (number_elements,order))

        return ''

class EllipticCurvePoint:


    """
        An instance of this class is a point on an elliptic curve.

        An instance is determined by:

            * an elliptic curve (i.e. instance of Class EllipticCurve)

            * the coordinates of the point given as (x,y)

        Things to add:

            - A method which "exponentiates" i.e. returns nP for an integer n.
            - Make the point at infinity an instance.
                    -- some methods will need to be adjusted once this is done.

    """

    # Define the data required to create an instance of this class.
    def __init__(self,ellipticcurve,x,y):

        self.ec = ellipticcurve
        self.x = x
        self.y = y
        self.prime = ellipticcurve.p
        self.a = ellipticcurve.a
        self.b = ellipticcurve.b

    def PointDouble(self):

        """
            Input: a point, P, on an elliptic curve E
            Output: the point 2P on the elliptic curve E

        """

        # Points with P(y) = 0 have order two.
        if self.y == 0:
            return float("inf")
        else:
            pass

        D = euclid_modular_inverse(2*self.y,self.prime)
        s = (D*(3*(self.x ** 2) + self.a)) % self.prime

        x_sum = ((s**2) - 2*self.x) % self.prime
        y_sum = (s*(self.x - x_sum) - self.y) % self.prime

        return EllipticCurvePoint(self.ec,x_sum,y_sum)


    def PointOrder(self):

        """
            Calculate the order of a point P on an elliptic curve
            by adding it to itself until the point at infinity is
            returned.

        """
        E = self.ec
        P = self
        P_fixed = self
        infinity = False

        count = 1

        while infinity == False:

            # Option: Print the sums as they are calculated.
            #print '%dP = (%d,%d)' % (count, P.x, P.y)

            P = E.PointAddition(P,P_fixed)

            if P == float("inf"):
                count = count + 1
                return count
            else:
                count = count + 1

    def PointInverse(self):

        """
            Returns the inverse of the given point. Note: the inverse of a
            point P = (a,b) can be calculated as -P = (a,p-1) where p is the
            prime over which the elliptic curve is defined.

        """
        x = self.x
        y = self.prime - self.y
        return EllipticCurvePoint(self.ec, x,y)

    def PointPrint(self):

        """
            This function simply returns the point as a string so that it
            can be read by a human.

        """

        return "(%d,%d)" % (self.x, self.y)
print sieve_eratosthenes(100)
