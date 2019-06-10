# Number theory related functions.

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
