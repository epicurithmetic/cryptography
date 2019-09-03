# Pollard Prime Factor Hunter
import ntteachingcode as nt
import math

# # Import a random 100 digit integer using the LCprng in my teaching code.
# n = nt.rng()
n = 123256927345872

k = 1

print "Pollard's (p-1) algorithm will be employed to find a prime divisor of %d" % n

# Boolean to stop the while-loop
prime_found = False

# While-loop.
while prime_found == False:

    # Calulate Mk                       # To get a speed up factorial should
    M = (2**(math.factorial(k)) -1)     # not be calculated directly. But only
    M_mod = (M % n)                     # mod n. Using FLT to speed up factorial.

    # Calculate gcd of Mk and n
    G_C_D = nt.euclid_gcd(M_mod,n)

    print k, M_mod, G_C_D

    # Check if a prime divisor has been found.
    if nt.isit_prime(G_C_D) == True:
        prime_divisor = G_C_D
        prime_found = True
    else:
        k += 1

    # Break before number of iterations gets too high
    if k > 12:
        #print nt.prime_factorisation(n)
        #print nt.prime_factorisation(n-1)
        print 'No prime divisor found after 12 iterations.'
        quit()


print "I have found that %d is a prime divisor of %d" % (prime_divisor,n)
