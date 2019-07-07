# Number theory related functions.

# ---------------------------------------------------------------------------
#                Primes, Primality Testing, and Factorisation
# ---------------------------------------------------------------------------

# List primes less than an upper-bound.
def sieve_eratosthenes(n):


    '''
        Input: Integer (type, int)
        Output: all primes less than input intger (type, list)

        Sloooooooow.
    '''

    # Inititally the sieve contains all numbers less than n.
    primes = range(2,n)

    # Now we remove multiples and iterate. We sieve out the composites.
    count = 0

    while count <  len(primes):
        for x in primes:
            if primes[count] == x:
                pass
            elif (x % primes[count] == 0):
                primes.remove(x)
            else:
                pass
        count += 1
    return primes

# Number of primes less than an upper-bound.
def landau_primecount(n):

    '''
        Input: Integer (type, int)
        Output: number of primes less than or equal to the input integer
        (type, int)

        Slow by n = 100,000.

    '''

    primes = sieve_eratosthenes(n+1)
    return len(primes)

# The functions above calculate a bunch of prime numbers. The next function
# takes an integer as input and returns (Boolean) whether or not it is prime.
# In order to check whether an integer is prime, it suffices to check for
# divisors upto and including it's squareroot.

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

# Now that we can calculate squareroots, we can write a primality test.
def isit_prime(n):

    '''
        Input: an integer (Type, int)
        Output: whether or not input is prime (Type, Boolean)

        This function tests divisiblity for each integer upto the squareroot
        of the input.

        Time taken to execute noticeable near the prime n = 1000000000039

    '''
    # We need only test divisiblity upto and including squareroot.
    divisor_bound = int(newton_sqrt(n))+1
    # Boolean which will stop loop if divisor found.
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

# Now that we can detect primes, we can begin to calculate the prime
# factorisation of an integer. For this we will need:
#               (i) Detect divisors
#              (ii) Calculate highest powers of divisors

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

def isit_divisor(n,d):

    '''
        Input: Two (Type, integers)
        Output: True or False (Type, Boolean)

        Output True if d divides n, False otherwise.
    '''

    if d == 0:
        return False
    elif (n%d) == 0:
        return True
    else:
        return False

def divisors(n):

    '''
        Input: Integer (Type, int)
        Output: List of integers (Type, list)

        Output is the list of divisors of the input n.

    '''

    divisors = [1,n]

    for i in range(2,int(newton_sqrt(n)+1)):

        if (n%i) == 0:
            divisors.append(i)
            if not (i == n/i):
                divisors.append(n/i)
        else:
            pass

    return divisors

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

    print '\n'
    return ('%s = ' % str(n)) + prime_factorisation[:-3]

# ---------------------------------------------------------------------------
#                          Euclidean Algorithm
# ---------------------------------------------------------------------------

# This is an ancient algorithm for determining the "greatest common divisor"
# i.e. GCD of two positive integers.
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

# With this function we can define Euler's totient (phi) function.
def euler_totient(n):

    '''
        Input: An integer (Type, int)
        Output: Number of integers less than that are coprime to n (Type, int)

        Note: this assumes input is greater than 1.

    '''

    count = 1
    # Increase count by 1 each time an integer is coprime to n.
    for x in range(2,n):
        if euclid_gcd(x,n) == 1:
            count +=1
        else:
            pass

    return count

# Extended Euclidean algorithm allows us to calculate inverses in modular
# arithmetic, when they exist.
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
        q = old_r / r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)


    print "Bezout coefficients: ", (old_s, old_t)
    print "[%s]*%s + [%s]*%s = gcd(%s,%s) = %s" % (old_s,a,old_t,b,a,b,old_r)
    print "Greatest common divisor: ", old_r
    return "What more could you want?"

# ... with the extended Euclidean algorithm implemented we can now calculate
# inverses in modular arithmetic.
def euclid_modular_inverse(a,p):

    '''
        Input: Integers a,p (Type, int)
        Output: Inverse of a mod p. (Type, int).

        Note: This code assumes a < p and that the inverse exists. Not the
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
        q = old_r / r
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
        print "%s not invertible mod %s" % (a,p)
        return None


# ---------------------------------------------------------------------------
#                          Base Change Functions
# ---------------------------------------------------------------------------

# Decimal to Binary to Decimal:

# This function determines the highest power of 2 that divides an integer.
def max_power_two(integer):

    """ This function inputs an integer (type int) and out puts the max power of
        2 that is less than or equal to the integer
    """

    count = 0
    powerlessthan = True

    while powerlessthan == True:

        if (2 ** (count + 1)) <= integer:
            count = count + 1
        else:
            powerlessthan = False

    return count

# This function turns decimals (type int) into binary (type str).
def decimal_to_binary(integer):

    """
    This function inputs integer (type int) and out puts the binary
        representation (type str)
    """

    binaryrep = ''

    max = max_power_two(integer)

    for i in range(max,-1,-1):

        if (2 ** i) <= integer:
            binaryrep = binaryrep + '1'
            integer = integer - (2 ** i)
        else:
            binaryrep = binaryrep + '0'

    return binaryrep

# ... and we can go back again from binary (type strings) to integers (type int).
def binary_to_decimal(binary):

    """
        This function inputs a binary string and outputs the corresponding
        integer.

    """

    binary = list(binary)
    l = len(binary)

    binary = [int(i) for i in binary]
    decirep = 0
    exp = l - 1
    i = 0

    while exp >=0:
        decirep = decirep + (binary[i] * (2 ** exp))
        i = i + 1
        exp = exp - 1

    return decirep

# Decimal to Hexadecimal to Decimal:

# This function determines the highest power of 16 that divides an integer.
def max_power_sixteen(integer):

    """
        This function inputs an integer (type int) and out puts the max power of
        16 that is less than or equal to the integer
    """
    count = 0
    powerlessthan = True

    while powerlessthan == True:

        if (16 ** (count+1)) <= integer:
            count = count + 1
        else:
            powerlessthan = False

    return count

# This function turns decimals (type int) into hexadecimal (type str).
def decimal_to_hex(integer):

    """
        This function inputs an integer (type int) and out puts the hexadecimal
        representation (type str)
    """

    hexrep = ''
    max = max_power_sixteen(integer)

    for i in range(max, -1, -1):

        x = integer // (16 ** i)
        integer = (integer % (16 ** i))

        if x == 10:
            hexrep += 'a'
        elif x == 11:
            hexrep += 'b'
        elif x == 12:
            hexrep += 'c'
        elif x == 13:
            hexrep += 'd'
        elif x == 14:
            hexrep += 'e'
        elif x == 15:
            hexrep += 'f'
        else:
            hexrep += str(x)

    return hexrep

# ... and we can go back again.
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
    decirep = 0
    exp = L - 1
    i = 0

    while exp >= 0:
        decirep = decirep + (hexnum[i] * (16 ** exp))
        i = i + 1
        exp = exp - 1

    return decirep

# Binary to Hex to Binary:

# This function turns binary (type str) into hexadecimal (type str).
def binary_to_hex(binarystring):

    """
        This function inputs binary (type str) and out puts the hexadecimal
        representation (type str)
    """

    decimal = binary_to_decimal(binarystring)
    hex = decimal_to_hex(decimal)

    return hex

# This function turns a hexadecimal (type str) into binary (type str).
def hex_to_binary(hexstring):

    """ This function inputs hexadecimal (type str) and out puts the binary
        representation (type str)
    """

    deci = hex_to_decimal(hexstring)
    binary = decimal_to_binary(deci)

    return binary

# Decimal to base64 to Decimal:

# Decimal to base64 is done as follows. But it only takes values 0 - 63. For
# larger integers, one needs to break the integer into 6-bit binary strings.
def decimal_to_base64(n):

    """
        This function inputs an integer [0,63] (type int) and returns the base64
        representation (type str)
    """
    if n == 0:
        return 'A'
    elif n == 1:
        return 'B'
    elif n == 2:
        return 'C'
    elif n == 3:
        return 'D'
    elif n == 4:
        return 'E'
    elif n == 5:
        return 'F'
    elif n == 6:
        return 'G'
    elif n == 7:
        return 'H'
    elif n == 8:
        return 'I'
    elif n == 9:
        return 'J'
    elif n == 10:
        return 'K'
    elif n == 11:
        return 'L'
    elif n == 12:
        return 'M'
    elif n == 13:
        return 'N'
    elif n == 14:
        return 'O'
    elif n == 15:
        return 'P'
    elif n == 16:
        return 'Q'
    elif n == 17:
        return 'R'
    elif n == 18:
        return 'S'
    elif n == 19:
        return 'T'
    elif n == 20:
        return 'U'
    elif n == 21:
        return 'V'
    elif n == 22:
        return 'W'
    elif n == 23:
        return 'X'
    elif n == 24:
        return 'Y'
    elif n == 25:
        return 'Z'
    elif n == 26:
        return 'a'
    elif n == 27:
        return 'b'
    elif n == 28:
        return 'c'
    elif n == 29:
        return 'd'
    elif n == 30:
        return 'e'
    elif n == 31:
        return 'f'
    elif n == 32:
        return 'g'
    elif n == 33:
        return 'h'
    elif n == 34:
        return 'i'
    elif n == 35:
        return 'j'
    elif n == 36:
        return 'k'
    elif n == 37:
        return 'l'
    elif n == 38:
        return 'm'
    elif n == 39:
        return 'n'
    elif n == 40:
        return 'o'
    elif n == 41:
        return 'p'
    elif n == 42:
        return 'q'
    elif n == 43:
        return 'r'
    elif n == 44:
        return 's'
    elif n == 45:
        return 't'
    elif n == 46:
        return 'u'
    elif n == 47:
        return 'v'
    elif n == 48:
        return 'w'
    elif n == 49:
        return 'x'
    elif n == 50:
        return 'y'
    elif n == 51:
        return 'z'
    elif n == 52:
        return '0'
    elif n == 53:
        return '1'
    elif n == 54:
        return '2'
    elif n == 55:
        return '3'
    elif n == 56:
        return '4'
    elif n == 57:
        return '5'
    elif n == 58:
        return '6'
    elif n == 59:
        return '7'
    elif n == 60:
        return '8'
    elif n == 61:
        return '9'
    elif n == 62:
        return '+'
    else:
        return '/'

# and back again
def base64_to_decimal(n):
    """ This function inputs n in base64 (type str) and returns the decimal
        representation (type int)
    """
    if n == 'A':
        return 0
    elif n == 'B':
        return 1
    elif n == 'C':
        return 2
    elif n == 'D':
        return 3
    elif n == 'E':
        return 4
    elif n == 'F':
        return 5
    elif n == 'G':
        return 6
    elif n == 'H':
        return 7
    elif n == 'I':
        return 8
    elif n == 'J':
        return 9
    elif n == 'K':
        return 10
    elif n == 'L':
        return 11
    elif n == 'M':
        return 12
    elif n == 'N':
        return 13
    elif n == 'O':
        return 14
    elif n == 'P':
        return 15
    elif n == 'Q':
        return 16
    elif n == 'R':
        return 17
    elif n == 'S':
        return 18
    elif n == 'T':
        return 19
    elif n == 'U':
        return 20
    elif n == 'V':
        return 21
    elif n == 'W':
        return 22
    elif n == 'X':
        return 23
    elif n == 'Y':
        return 24
    elif n == 'Z':
        return 25
    elif n == 'a':
        return 26
    elif n == 'b':
        return 27
    elif n == 'c':
        return 28
    elif n == 'd':
        return 29
    elif n == 'e':
        return 30
    elif n == 'f':
        return 31
    elif n == 'g':
        return 32
    elif n == 'h':
        return 33
    elif n == 'i':
        return 34
    elif n == 'j':
        return 35
    elif n == 'k':
        return 36
    elif n == 'l':
        return 37
    elif n == 'm':
        return 38
    elif n == 'n':
        return 39
    elif n == 'o':
        return 40
    elif n == 'p':
        return 41
    elif n == 'q':
        return 42
    elif n == 'r':
        return 43
    elif n == 's':
        return 44
    elif n == 't':
        return 45
    elif n == 'u':
        return 46
    elif n == 'v':
        return 47
    elif n == 'w':
        return 48
    elif n == 'x':
        return 49
    elif n == 'y':
        return 50
    elif n == 'z':
        return 51
    elif n == '0':
        return 52
    elif n == '1':
        return 53
    elif n == '2':
        return 54
    elif n == '3':
        return 55
    elif n == '4':
        return 56
    elif n == '5':
        return 57
    elif n == '6':
        return 58
    elif n == '7':
        return 59
    elif n == '8':
        return 60
    elif n == '9':
        return 61
    elif n == '+':
        return 62
    else:
        return 63

# With the functions above we can write a function which turns hex to base64
def hex_to_base64(hex_string):

    '''
        This function turns a hexadecimal string (type string) into a base64
        string (type string) by first breaking the hex string into its binary
        representation, collecting those bits into 6-bit bytes and then
        converting each of those bytes into the corresponding base64
        output.

        We collect into 6-bit bytes as 63_10 = 111111_2 i.e. we need at most
        6-bits to reprsent integers in the interval [0,63]

        Input: hex string.
        Output: base64 string.

    '''

    binary_string = hex_to_binary(hex_string)
    L = len(binary_string)
    N = L // 6                                  # This is the number of full 6-bit bytes.
    r = L % N                                   # This is the size of the left over byte.

    # Collect the bits into 6-bit bytes.
    sixbit_bytes = []

    # Note: we collect from the righthandside of the binary string.
    #       imagining we are reading the number as it is feed in from the
    #       left.
    for i in range(0,N):
        sixbit_bytes.append(binary_string[(L - 6 - (6*i)): L - (6*i)])

    sixbit_bytes.append(binary_string[0:r])

    # Now turn the bytes into their base64 characters.
    for i in range(0,N+1):
        sixbit_bytes[i] = decimal_to_base64(binary_to_decimal(sixbit_bytes[i]))

    # Because of the way we have read the bytes off we must reverse them.
    sixbit_bytes.reverse()

    base64_string = ''

    for i in range(0, N+1):
        base64_string += str(sixbit_bytes[i])

    return base64_string

# ---------------------------------------------------------------------------
#                       Arithmetic over p = 2
# ---------------------------------------------------------------------------

# Code for doing arithmetic in GF(2) and its finite extensions. For cryptography
# purposes a lot of work is done in GF(256). But code should be written for
# any finite extension of GF(2).

# When working in such an extension we must realise it has a quotient of the
# polynomial ring with coefficients in GF(2). For that, we have to *choose*
# an irreducible polynomial to quotient by for each GF(n).

# In the case of implementing the Advanced Encryption Standard (AES) block
# cipher one is required to use the following specified polynomial.

#           AES-Specficication: f(x) = x^8 + x^4 + x^3 + x + 1

# Polynomials over GF(2) have coefficients consiting of 0 or 1. Together with
# the powers of x. However, the powers of x are really just place holders.
# For this reason, we can (and will) represent a polynomial simply as a binary
# string. The coefficient of the highest power of x will be the left-most entry
# of the string, and they will descend along to the constant term at the right.

# Example: x^3 + x + 1 is represented as '1011'. The 0 represents the fact that
#          there are no x^2 terms. Each 1 represents the 1 in front of the other
#          terms of the polynomial.

# With this choice of notation made, we can now write functions which perform
# arithmetic on polynomials over GF(2). In particular we require functions
# which (i) add polynomials (ii) multiply polynomials (iii) calculate the
# remainder upon divison of one polynomial by another, and (iv) the greatest
# common divisor of two polynomials.

# Polynomial addition in GF(2)
def GF2_polynomial_sum(poly1, poly2):

    '''
        Input: Two binary strings representing polynomials over GF(2) (type str)
        Output: Binary string representing the sum of the polynomials over
                GF(2) (type str)

        Note: Polynomial addition mod 2 is nothing but XOR. That is to say, the
              sum is obtained by XOR'ing the coefficients of the same degree.

    '''

    l1 = len(poly1)
    l2 = len(poly2)

    if l1 < l2:
        poly1 = '0'*(l2-l1) + poly1
    elif l2 < l1:
        poly2 = '0'*(l1-l2) + poly2
    else:
        pass

    sum_list = [((int(x) + int(y))%2) for x,y in zip(list(poly1),list(poly2))]

    # Remove any leading zeroes, as these give the wrong degree for the sum.
    # However, we don't want to remove the leading zero if the polynomial
    # is the zero polynomial!
    leading_zeroes = True
    while leading_zeroes == True:

        # First check if the polynomial is the 0 polynomial. In which case, we
        # do not want to remove the leading 0.
        if len(sum_list) == 1:
            leading_zeroes = False

        # If the polynomial is of degree greater than 0, then we check for and
        # remove any leading zeroes from the calculation.
        elif sum_list[0] == 0:
            del sum_list[0]
            # Note: we deleting this entry shifts all elements along. So we
            #       do not need to change the index we are looking at.

        # If there are no (more) leading zeroes, then we can move on.
        else:
            leading_zeroes = False

    # Put the polynomial into a string.
    sum = ''
    for x in sum_list:
        sum += str(x)

    return sum

# Polynomial multiplication in GF(2)
def GF2_polynomial_product(poly1, poly2):

    '''
        Input: two binary strings representing polynomials over GF(2)
               (type, str)
        Output: one binary string repsrenting the product of input
                polynomials. (type, str)

    '''


    l1 = len(poly1)
    l2 = len(poly2)

    l = l1+l2-1

    # Reverse the inputs to make the degree of the terms in the polynomial
    # more naturally match the index of python range function.
    poly1 = list(poly1)
    poly1.reverse()

    poly2 = list(poly2)
    poly2.reverse()


    # Goal is to update this list with the appropiate coefficients of the
    # product of the input polynomials.
    product_list = [0]*l

    # Range over elements of the first polynomial: poly1
    for i in range(0,l1):
        # Note the degree of the current term in poly1 is equal to, i, the
        # counter of the for-loop.

        # Range over elements of the second polynomial: poly2
        for j in range(0,l2):

            # This product contributes to the coefficient of a term of
            # degree i + j ...
            c = int(poly1[i])*int(poly2[j])

            # ... so we update the i+jth coefficient of the product.
            product_list[i+j] = ((product_list[i+j] + c) % 2)

    product_list.reverse()
    product = ''
    for x in product_list:
        product += str(x)

    return product

# Polynomial division in GF(2)
def GF2_polynomial_remainder(dividend,divisor):

    '''
        Input: Two binary strings representating polynomials over GF(2). The
               first argument is the dividend (the polynomial to be dividend)
               and the second argument is the divisor. (Type, str)

        Output: One polynomial string corresponding to the polynomial remainder
                of the division of the dividend by the divisor. (Type, str)

        Note: this is division in the integral domain of polynomials over
              the field with two elements GF(2).

    '''

    # Edge cases to deal with: divisor = 0,1.
    # You can't divide by 0!
    if divisor == '0':
        print "You just divided by 0. You blew up the universe. Good job."
        return None
    # Since the length of the divisor does not change, I have to deal with
    # the case the divisor = 1 apart from the other cases.
    if divisor == '1':
        return '0'

    while len(dividend) >= len(divisor):

        # First, figure out the difference between highest powers.
        deg_dividend = len(dividend)
        deg_divisor = len(divisor)
        shift = deg_dividend - deg_divisor

        # Calculate the shift of the divisor.
        shifted_factor = '1' + '0'*shift
        shifted_divisor = GF2_polynomial_product(shifted_factor,divisor)

        # Update the dividend according to the long divison algorith. Note that
        # addition = subtraction in GF(2). That is why we sum here.
        dividend = GF2_polynomial_sum(dividend, shifted_divisor)

    return dividend

# ... more GF(2) polynomial division, this time returning the quotient
def GF2_polynomial_quotient(dividend,divisor):

    '''
        Input: Two binary strings representating polynomials over GF(2). The
               first argument is the dividend (the polynomial to be dividend)
               and the second argument is the divisor. (Type, str)

        Output: One polynomial string corresponding to the polynomial quotient
                of the division of the dividend by the divisor. (Type, str)

        Note: this is division in the integral domain of polynomials over
              the field with two elements GF(2). Executed using the long
              division algorithm.

    '''

    # Initialize the quotient. Note the length is derived from the difference
    # in degrees of the dividend and divisor.
    quotient = ['0']*((len(dividend)-len(divisor))+1)

    # Edge cases to deal with: divisor = 0,1.
    # You can't divide by 0!
    if divisor == '0':
        print "You just divided by 0. You blew up the universe. Good job."
        return None
    # Since the length of the divisor does not change, I have to deal with
    # the case the divisor = 1 apart from the other cases.
    if divisor == '1':
        return dividend

    while len(dividend) >= len(divisor):

        # First, figure out the difference between highest powers.
        deg_dividend = len(dividend)
        deg_divisor = len(divisor)
        shift = deg_dividend - deg_divisor
        # This updates the quotient polynomial
        quotient[(len(quotient) - (shift+1))] = '1'

        # Calculate the shift of the divisor.
        shifted_factor = '1' + '0'*shift
        shifted_divisor = GF2_polynomial_product(shifted_factor,divisor)

        # Update the dividend according to the long divison algorithm. Note
        # addition = subtraction in GF(2). That is why we sum here.
        dividend = GF2_polynomial_sum(dividend, shifted_divisor)

    # Turn the quotient into a string
    quotient_str = ''
    for x in quotient:
        quotient_str += str(x)

    return quotient_str

# Polynomial GCD in GF(2)
def GF2_euclid_gcd(poly1, poly2):

    '''
        Input: two binary strings representing the polynomials over GF(2) that
               we are to calculate the GCD of (Type, str)

        Output: binary string representing the polynomial that is the greatest
                common divisor of the input polynomials (Type, str)

        Note: This function implements Euclid's algorithim in the integral
              domain of polynomials over GF(2). This is a recursive algorithm.

        Edge cases of constant polynomials (0,1) treated seperately.

    '''
    # First consider the case(s) where either polynomial is 0.
    if poly1 == '0':
        return poly2
    elif poly2 == '0':
        return poly1

    # Again, we have to deal with the cases in which either polynomial is
    # 1 seperately to the other cases.
    elif (poly1 == '1' or poly2 == '1'):
        return '1'

    # We have to be careful about which polynomial is of greater degree.
    elif len(poly1) >= len(poly2):
        r = GF2_polynomial_remainder(poly1, poly2)
        return GF2_euclid_gcd(poly2, r)

    else:
        r = GF2_polynomial_remainder(poly2, poly1)
        return GF2_euclid_gcd(poly1, r)

# With the arithmetic of polynomials over GF(2) defined, we can begin to write
# code for arithmetic in finite extensions of GF(2). In particular, we can
# now perform arithmetic in GF(8) i.e. the field with 256 elements. As mentioned
# above we will use the AES specified irreducible degree 8 polynomial to do
# the arithmetic in GF(8).

# Since addition does not increase the degree of a polynomial, we can use
# the same GF(2) addition function all extens of GF(2). We need only worry about
# multiplication for a given extension.
def GF256_multiplication(x,y):

    '''
        Input: Two binary strings (max length 8) corresponding to an element in
               the field GF(256) i.e. the degree 8 extension of GF(2).

        Output: One binary string corresponding to the product xy in GF(8)

        Note: In order to do this arithmetic we must choose a polynomial to
              quotient by. Since our main application will be AES, we take the
              specified standard f(x) = x^8 + x^4 + x^3 + x + 1 = 100011011

    '''

    polynomial_product = GF2_polynomial_product(x,y)

    if len(polynomial_product) > 8:
        GF256_product = GF2_polynomial_remainder(polynomial_product, '100011011')
        GF256_product = '0'*(8 - len(GF256_product)) + GF256_product
        return GF256_product
    else:
        polynomial_product = '0'*(8 - len(polynomial_product)) + polynomial_product
        return polynomial_product

# Note: elements of GF(256) can be written compactly as two-character HEX
#       strings. So, it might be useful to have a function which manipulates
#       elements of GF(256) directly in this form.

# The next function is a version of the EEA for polynomials over GF(2). This
# will be used to find inverses in extensions of GF(2).
def GF2_extended_euclid_gcd(poly1, poly2):

    '''
        Input: Two polynomials (Type, str) whose GCD is sought.
        Output: greatest common divisor (Type, str) of the input polynomials.
                along with Bezout's Identity.

    '''


    s = '0'
    old_s = '1'
    t = '1'
    old_t = '0'
    r = poly2
    old_r = poly1


    while not ( r == '0' ):
        q = GF2_polynomial_quotient(old_r,r)
        (old_r,r) = (r, GF2_polynomial_sum( old_r, GF2_polynomial_product(q,r) ))
        (old_s,s) = (s, GF2_polynomial_sum(old_s,GF2_polynomial_product(q,s)) )
        (old_t,t) = (t, GF2_polynomial_sum(old_t,GF2_polynomial_product(q,t)) )


    print "Bezout coefficients: ", (old_s, old_t)
    print "[%s]*%s + [%s]*%s = gcd(%s,%s) = %s" % (old_s,poly1,old_t,poly2,poly1,poly2,old_r)
    print "Greatest common divisor: ", old_r
    return "What more could you want?"

# With the EEA written, we can now calculate inverses in GF(256)
def GF256_inverse(n):

    '''
        Input: Element of GF(256) (Type, str) whose inverse is sought.
        Output: Element of GF(256) (Type, str) which is the inverse of the
                input element.

        Note: This instance of GF(256) uses the AES-128 standard:
                    f(x) = x^8 + x^4 + x^3 + x + 1 = 100011011
              In order to calculate the product (and inverse) in the extension.

    '''


    s = '0'
    old_s = '1'
    t = '1'
    old_t = '0'
    r = n
    old_r = '100011011'              # This is the AES-standard.

    # This while loop executes the Extended Euclidean Algorithm.
    while not ( r == '0' ):
        q = GF2_polynomial_quotient(old_r,r)
        (old_r,r) = (r, GF2_polynomial_sum(old_r,GF2_polynomial_product(q,r)))
        (old_s,s) = (s, GF2_polynomial_sum(old_s,GF2_polynomial_product(q,s)))
        (old_t,t) = (t, GF2_polynomial_sum(old_t,GF2_polynomial_product(q,t)))


    return old_t

# Is it faster to calculate this everytime want it? Or is it better to look
# the inverses up in a dictionary? We now create a .txt file which contain the
# inverses, so we can write a dictionary.

# This code writes the inverses into a file.
# f = open("gf256_inverses.txt","w+")
# GF256_hex_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# for x in GF256_hex_list:
#     for y in GF256_hex_list:
#
#         x_hex = hex_to_binary(x)
#         x_hex = '0'*(4 - len(x_hex)) + x_hex
#
#         y_hex = hex_to_binary(y)
#         y_hex = '0'*(4 - len(y_hex)) + y_hex
#
#         xy_GF256 = x_hex + y_hex
#         xy_GF256 = list(xy_GF256)
#
#         # We don't want leading zeroes.
#         leading_zeroes = True
#         while leading_zeroes == True:
#
#             # First check if the polynomial is the 0 polynomial. In which case, we
#             # do not want to remove the leading 0.
#             if len(xy_GF256) == 1:
#                 leading_zeroes = False
#
#             # If the polynomial is of degree greater than 0, then we check for and
#             # remove any leading zeroes from the calculation.
#             elif xy_GF256[0] == '0':
#                 del xy_GF256[0]
#                 # Note: we deleting this entry shifts all elements along. So we
#                 #       do not need to change the index we are looking at.
#
#             # If there are no (more) leading zeroes, then we can move on.
#             else:
#                 leading_zeroes = False
#
#         xy = ''
#         for i in xy_GF256:
#             xy += i
#         xy_hex = binary_to_hex(xy)
#
#         # Calculate inverse.
#         inverse = GF256_inverse(xy)
#         inverse_hex = binary_to_hex(inverse)
#
#         # Write the inverse to the file.
#         f.write('"%s":"%s",\n' % (xy_hex,inverse_hex))
# f.close()

# This is a dictionary which stores the inverses of all elements in GF(256).
# This dictionary uses the compact HEX notation for writing elements of
# the finite field GF(256).
GF256_inverse_dict = {
"0":"0","1":"1","2":"8d","3":"f6","4":"cb","5":"52","6":"7b","7":"d1","8":"e8","9":"4f",
"a":"29","b":"c0","c":"b0","d":"e1","e":"e5","f":"c7","10":"74","11":"b4","12":"aa",
"13":"4b","14":"99","15":"2b","16":"60","17":"5f","18":"58","19":"3f","1a":"fd",
"1b":"cc","1c":"ff","1d":"40","1e":"ee","1f":"b2","20":"3a","21":"6e","22":"5a",
"23":"f1","24":"55","25":"4d","26":"a8","27":"c9","28":"c1","29":"a","2a":"98",
"2b":"15","2c":"30","2d":"44","2e":"a2","2f":"c2","30":"2c","31":"45","32":"92",
"33":"6c","34":"f3","35":"39","36":"66","37":"42","38":"f2","39":"35","3a":"20",
"3b":"6f","3c":"77","3d":"bb","3e":"59","3f":"19","40":"1d","41":"fe","42":"37",
"43":"67","44":"2d","45":"31","46":"f5","47":"69","48":"a7","49":"64","4a":"ab",
"4b":"13","4c":"54","4d":"25","4e":"e9","4f":"9","50":"ed","51":"5c","52":"5",
"53":"ca","54":"4c","55":"24","56":"87","57":"bf","58":"18","59":"3e","5a":"22",
"5b":"f0","5c":"51","5d":"ec","5e":"61","5f":"17","60":"16","61":"5e","62":"af",
"63":"d3","64":"49","65":"a6","66":"36","67":"43","68":"f4","69":"47","6a":"91",
"6b":"df","6c":"33","6d":"93","6e":"21","6f":"3b","70":"79","71":"b7","72":"97",
"73":"85","74":"10","75":"b5","76":"ba","77":"3c","78":"b6","79":"70","7a":"d0",
"7b":"6","7c":"a1","7d":"fa","7e":"81","7f":"82","80":"83","81":"7e","82":"7f",
"83":"80","84":"96","85":"73","86":"be","87":"56","88":"9b","89":"9e","8a":"95",
"8b":"d9","8c":"f7","8d":"2","8e":"b9","8f":"a4","90":"de","91":"6a","92":"32",
"93":"6d","94":"d8","95":"8a","96":"84","97":"72","98":"2a","99":"14","9a":"9f",
"9b":"88","9c":"f9","9d":"dc","9e":"89","9f":"9a","a0":"fb","a1":"7c","a2":"2e",
"a3":"c3","a4":"8f","a5":"b8","a6":"65","a7":"48","a8":"26","a9":"c8","aa":"12",
"ab":"4a","ac":"ce","ad":"e7","ae":"d2","af":"62","b0":"c","b1":"e0","b2":"1f",
"b3":"ef","b4":"11","b5":"75","b6":"78","b7":"71","b8":"a5","b9":"8e","ba":"76",
"bb":"3d","bc":"bd","bd":"bc","be":"86","bf":"57","c0":"b","c1":"28","c2":"2f",
"c3":"a3","c4":"da","c5":"d4","c6":"e4","c7":"f","c8":"a9","c9":"27","ca":"53",
"cb":"4","cc":"1b","cd":"fc","ce":"ac","cf":"e6","d0":"7a","d1":"7","d2":"ae",
"d3":"63","d4":"c5","d5":"db","d6":"e2","d7":"ea","d8":"94","d9":"8b","da":"c4",
"db":"d5","dc":"9d","dd":"f8","de":"90","df":"6b","e0":"b1","e1":"d","e2":"d6",
"e3":"eb","e4":"c6","e5":"e","e6":"cf","e7":"ad","e8":"8","e9":"4e","ea":"d7",
"eb":"e3","ec":"5d","ed":"50","ee":"1e","ef":"b3","f0":"5b","f1":"23","f2":"38",
"f3":"34","f4":"68","f5":"46","f6":"3","f7":"8c","f8":"dd","f9":"9c","fa":"7d",
"fb":"a0","fc":"cd","fd":"1a","fe":"41","ff":"1c"
}

# ---------------------------------------------------------------------------
#                      Arithmetic in Gaussian Integers
# ---------------------------------------------------------------------------

class Gaussian_Integers:

    '''
        Objects of this class are Gaussian Integers. With integer real and
        imaginary component.

    '''

    # This tells us that in order to define an object in this class we need
    # to specify two inputs: the real and imaginary components of the Gaussian
    # integer. We assume real and imaginary have Type int.
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    # This returns the norm of the Gaussian integer.
    def norm(self):
        norm = (self.real ** 2)+(self.imaginary ** 2)
        return norm

    # Is the object/instance prime? What is the factorisation?
    def isit_Gaussianprime(self):

        # If both components are non-zero, then primality is equivalent
        # to having a prime norm.
        if not ((self.real == 0) or (self.imaginary == 0)):
            return isit_prime(self.norm())
        # If the real part is 0, then primality is equivalent to the imaginary
        # component being a prime of the form 4n+3.
        elif (self.real == 0):
            if ( isit_prime(abs(self.imaginary)) ) and ((self.imaginary % 4) == 3):
                return True
            else:
                return False
        # Otherwise the Gaussian integer will not be prime.
        else:
            return False

    # Multiply Gaussian Integers.
    def gaussian_multiplication(self,g):
        # Product of self and specified Gaussian integer.
        return Gaussian_Integers(((self.real*g.real) - (self.imaginary*g.imaginary)),((self.real*g.imaginary) + (self.imaginary*g.real)))

    # Is it a unit?
    def isit_unit(self):
        if self.norm() == 1:
            return True
        else:
            return False

# Ideas: Use a polynomial to define an object in a class Algebraic Integers
#        This class could have functions (methods) which give information about
#        the monogenic ring this polynomial generates.
#        (i) is it the ring of integers of the field?
#       (ii) what is the group of units?
#      (iii) which primes ramify?
#       (iv) ... other number theoretically interesting things?

# Define a class whose objects are rings of algebraic integers whose type
# is a class so that one can then refer to the elements of that ring as
# the objects of the class defining the ring. Elements of the ring will be
# an object with in a class with in a class.
