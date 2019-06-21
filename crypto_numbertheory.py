# Number theory related functions.

# Primes are sweeeet.

# ---------------------------------------------------------------------------
#                          Euclidean Algorithm.
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

# # Binary to base64...
# def binary_to_base64(n):
#     '''
#         Input: binary (type string)
#         Output: base64 (type string)
#
#     '''
#     decimal_rep = binary_to_decimal(n)
#     base64_rep = decimal_to_base64(decimal_rep)
#
#     return base64_rep
#
# # ... and back again.
# def base64_to_binary(n):
#
#     '''
#         Input: base64 (type string)
#         Output: binary (type string)
#
#     '''
#
#     decimal_rep = base64_to_decimal(n)
#     binary_rep = decimal_to_base64(decimal_rep)
#
#     return binary_rep
#


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
#                          Arithmetic over p=2
# ---------------------------------------------------------------------------

# Code for doing arithmetic in GF(2) and its finite extensions. For cryptography
# purposes a lot of work is done in GF(256). But code should be written for
# any finite extension of GF(2).

# When working in such an extension we must realise it has a quotient of the
# polynomial ring with coefficients in GF(2). For that, we have to *chose*
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
        print poly1
        print poly2
    elif l2 < l1:
        poly2 = '0'*(l1-l2) + poly2
        print len(poly1)
        print len(poly2)
    else:
        print poly1
        print poly2


    sum_list = [((int(x) + int(y))%2) for x,y in zip(list(poly1),list(poly2))]

    sum = ''
    for x in sum_list:
        sum+=str(x)

    return sum

#print GF2_polynomial_sum('10011', '1101')

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

#print GF2_polynomial_product('10011', '1101')
