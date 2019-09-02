# Example code for Math3301/6114
import timeit

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

    #print '\n'
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
        q = old_r / r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)


    # I have commented out three print statements because I call this
    # function in the linear_diophantine function. You can uncomment them
    # if you want to use this function by itself.

    #print "Bezout coefficients: ", (old_s, old_t)
    #print "[%s]*%s + [%s]*%s = gcd(%s,%s) = %s" % (old_s,a,old_t,b,a,b,old_r)
    #print "Greatest common divisor: ", old_r
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
#             print x,y
#
#         # If x,y aren't solutions, then do nothing.
#         else:
#             pass

# Exercise 5: XOR-binary strings.
#... coming soon.


# Exercise 6: XOR Single-Byte Encryption.
#... coming soon.


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

# Exercise 3: Pollard's (p-1) Algorithm.
def pollard_prime_hunter(n):

    '''
        This function employs Pollard's algorithm to find a prime divisor
        of an integer. See the notes for Week 4 for an explanation of
        Pollard's algorithm.

    '''

    # Rather than calculating the factorial every iteration, we can simply
    # update the value L by raising it to the kth power. Reducing mod n
    # at each stage as this keeps the numbers below n.
    L = 2
    k = 1
    prime_found = False

    # While no prime divisor has been found, we loop.
    while prime_found == False:

        L = (L ** k) % n

        M_k = (L - 1) % n

        # Calculate the GCD
        G_C_D = euclid_gcd(M_k,n)

        # Print the data of each stage. As presented in the notes.
        print 'k = %d, 2^(%d!) - 1 = %d mod %d, gcd(%d,%d) = %d' % (k, k, M_k,n,M_k,n,G_C_D)

        # Check if a prime divisor has been found.
        if isit_prime(G_C_D) == True:
            prime_divisor = G_C_D
            prime_found = True
            return G_C_D
        else:
            k += 1

        # Break if loop goes on for too long...
        if k > 100:
            return 'No prime divisor found after 100 iterations.'
            quit()

# Exercise 4: Frequency Analysis
#... coming soon.

# Exercise 5: Break Single-Byte XOR
#... coming soon.


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
def exp_mod(a,e,m):

    '''
        This calculates the a to the power of e mod m. It leverages the
        fact that reducing mod m commutes with multiplication to keep the
        integers small enough to not get a memory error.

        Note: if m is too large, then we can't get around that using this
        function. Other methods will have to be employed in order to
        get around the fact that computers only have limited memory.

        All of this seems overkill as Python has the ability to handle
        large integers built into its structure. <type, long-int>

        Note: This is far too slow when used in the Miller test. In order
              to get better speed you can use the in-built Python function
              pow(base,exponent,moduli) to do the same job... much faster.

    '''

    exp_a = a
    exp = 2

    while exp <= e:

        exp_a = (exp_a*a) % m
        exp += 1
        #print exp

    return exp_a

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
    print test_integer

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
        test_integer = pow(a,e,n)
        #print test_integer, j

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
        #print '%d is composite.' % n
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
# print miller_rabin(a)
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
# # For define the coefficients
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
#... coming soon

# Exercise 2: Affine Cipher
#... coming soon

# Exercise 3: Vigenere Cipher
#... coming soon

# Exercise 4: Break Them All
#... coming soon

# ------------------
# Exercise Sheet 7:
# ------------------

# Exercise 1: Fast Exponentiation
#... coming soon

# Exercise 2: Pseudo-Randon Number Generator.

# This code will implement the Linear Congruential PRNG.
def lcprng():


    # We need to determine a seed value to start the process. I will use the
    # timeit module to access the time and use some of the digits from that
    # number as the seed value.
    seed_time = timeit.default_timer()
    seed = int((seed_time - int(seed_time))* (10 ** 10))

    # Store the sequence
    random_numbers = []

    # Use the LCPRNG algorithm with the following paramters:
    a = 6364136223846793005
    c = 1442695040888963407
    m = (2**63)

    # Set a counter for the loop.
    k = 1

    # Loop through the algorithm.
    while k < 10:

        seed = (a*seed + c) % m
        random_numbers.append(seed)
        k += 1

    return random_numbers

# In order to get a prime number largue enough for RSA to be secure, we need to
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
    print count
    return seed

print random_prime_generator()
