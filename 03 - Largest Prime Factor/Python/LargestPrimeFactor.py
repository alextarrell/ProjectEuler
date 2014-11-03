#! /usr/bin/env python

import math, sys, random

def main():
	if len(sys.argv) < 2:
		print 'Specify the number to find the largest prime factor of'
	else:
		print primefactors(long(sys.argv[1]))

def primefactors(n, sort=False):
    factors = []

    limit = int(n ** .5) + 1
    for checker in smallprimes:
        print smallprimes[-1]
        if checker > limit: break
        while n % checker == 0:
            factors.append(checker)
            n //= checker


    if n < 2: return factors
    else : 
        factors.extend(bigfactors(n,sort))
        return factors

def bigfactors(n, sort = False):
    factors = []
    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) 
        factors.extend(bigfactors(factor,sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()    
    return factors

def pollard_brent(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g

def primesbelow(N):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    #""" Input N>=6, Returns a list of primes, 2 <= p < N """
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve = [True] * (N // 3)
    sieve[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve[i]:
            k = (3 * i + 1) | 1
            sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]

smallprimeset = set(primesbelow(100000))
_smallprimeset = 100000
def isprime(n, precision=7):
    # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test#Algorithm_and_running_time
    if n == 1 or n % 2 == 0:
        return False
    elif n < 1:
        raise ValueError("Out of bounds, first argument must be > 0")
    elif n < _smallprimeset:
        return n in smallprimeset


    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for repeat in range(precision):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1: continue

        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == 1: return False
            if x == n - 1: break
        else: return False

    return True

smallprimes = primesbelow(1000) # might seem low, but 1000*1000 = 1000000, so this will fully factor every composite < 1000000
def primefactors(n, sort=False):
    factors = []

    limit = int(n ** .5) + 1
    for checker in smallprimes:
        if checker > limit: break
        while n % checker == 0:
            factors.append(checker)
            n //= checker
            limit = int(n ** .5) + 1
            if checker > limit: break

    if n < 2: return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(primefactors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()

    return factors

def factorization(n):
    factors = {}
    for p1 in primefactors(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors

totients = {}
def totient(n):
    if n == 0: return 1

    try: return totients[n]
    except KeyError: pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1)  *  p ** (exp - 1)

    totients[n] = tot
    return tot

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# def largestPrimeFactor(val):
# 	PrimeTable = genPrimeTable(val)
# 	PrimeFactors = []
# 	for i in PrimeTable:
# 		if (val % i == 0):
# 			PrimeFactors.append(i)
# 	
# 	print 'The Prime factors of %d are: ' % (val)
# 	print PrimeFactors
# 	print 'The Largest Prime Factor of %d is %d' % (val, PrimeFactors.pop())
#
# def genPrimeTable(max):
# 	knownPrimes = [2, 3]
# 	set = range(2, max+1)
# 	for i in set:
# 		if isPrime(i, knownPrimes):
# 			# print '%d is Prime' % (i)
# 			knownPrimes.append(i)
# 	
# 	print 'There are %d entries in the knownPrimes list' % (len(knownPrimes))
#  	# print knownPrimes
# 	
# 	return knownPrimes
# 
# def isPrime(val, knownPrimes):
# 	prime = True
# 	max = int(math.sqrt(val)) + 1
# 	for i in knownPrimes:
# 		if i > max:
# 			break
# 		if val % i == 0:
# 			prime = False
# 			# print '%d is divisible by the prime %d' % (val, i)
# 			return False
# 	return prime

if __name__ == "__main__":
	main()