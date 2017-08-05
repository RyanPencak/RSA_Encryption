# Ryan Pencak, Wesley Morlock, Evan Harrington
# RSA.py
# compile with: python3

import random
import math

def generated_random_prime (n_digits):
    prime = false
    while (prime == false):
        start = (10**(n_digits - 1))
        end = (10**(n_digits - 1))
        randNum = random.randint(start, end)
        prime = isPrime(randNum)
    p = randNum
    return p

# Checks if a number is prime
def isPrime(p):
    p = abs(p)
    x = 2
    while (i <= math.sqrt(p)):
        if (n%i == 0):
            return false
        i += 1
    return true

def gcd(j,k):
    if ((j%k) == 0):
        return k
    else:
        return gcd(k, (j%k))

def areRelativelyPrime(a,b):
    if (gcd(a,b) == 1):
        return true
    else:
        return false

def generated_e (p,q):
    isRelPrimeP = false
    isRelPrimeQ = false
    n = p*q
    start = (10**(n_digits - 1))
    end = (10**(n_digits - 1))

    while ((isRelPrimeP == false) or (isRelPrimeQ == false)):
        randNum = random.randint(start,end)
        areRelativelyPrime(randNum,p)
        areRelativelyPrime(randNum,q)

    e = randNum
    return e

def find_inverse (e,m):

    # return inv

def fast_exponentiate (a,e,m):
    e_bin = bin(e)
    k = len(e_bin) - 1
    expList = []
    powList = []
    expansionTotal = 1
    for i in e_bin:
        if(i == 1):
            expList.append(2**k)
        k -= 1

    for j in expList:
        expList[j] = expList[j]%m

    for x in expList:
        expansionTotal *= a**(expList[x])

    expansionTotal = expansionTotal%m

    return expansionTotal

def rsa (n_digits):
    p = generated_random_prime(n_digits)
    q = p

    while (q == p):
        q = generated_random_prime(n_digits)

    n = p*q

    phi = (p-1)*(q-1)

    e = generated_e(p,q)

    d = find_inverse(e,phi)

    return ((e,n),(d,n))

def encrypt (kp, plaintext):
    pass

def decrypt (kp, ciphertext):
    pass

if __name__ == '__main__':
    main()
