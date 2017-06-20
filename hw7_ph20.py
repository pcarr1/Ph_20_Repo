import random
import math

def isPrime(n):
    if n in [0, 1]:
        return False
    elif n in [2, 3]:
        return True
    c = 2
    while c <= n / 2:
        if n % c == 0:
            return False
        c += 1
    return True

def generatePrimeNumbers(N=255):
    primeNumbers = [1, 1]
    while not isPrime(primeNumbers[0]):
        primeNumbers[0] = random.randint(2, N)
    while (not isPrime(primeNumbers[1])) or primeNumbers[1] == primeNumbers[0]:
        primeNumbers[1] = random.randint(2, N)
    return primeNumbers

def generateProduct(primeNumbers):
    return primeNumbers[0] * primeNumbers[1]

def lcm(a, b):
    aMultiples = [a]
    bMultiples = [b]
    for i in range(int(1e5)):
        aMultiples += [aMultiples[-1] + a]
        bMultiples += [bMultiples[-1] + b]
    aMultiples = set(aMultiples)
    bMultiples = set(bMultiples)
    commonMultiples = aMultiples.intersection(bMultiples)
    return min(commonMultiples)

def divisors(a):
    divisorList = []
    for i in range(1, a + 1):
        if a % i == 0:
            divisorList += [i]
    return divisorList

def gcd(a, b):
    aDivisors = set(divisors(a))
    bDivisors = set(divisors(b))
    commonDivisors = aDivisors.intersection(bDivisors)
    return max(commonDivisors)

def totient(primeNumbers):
    return lcm(primeNumbers[0] - 1, primeNumbers[1] - 1)

def getRandomPrimeCoprimeNumber(a):
    coprimes = []
    for i in range(2, a + 2):
        if gcd(a, i) == 1:
            coprimes += [i]
    n = random.choice(coprimes)
    while not isPrime(n):
        coprimes.remove(n)
        n = random.choice(coprimes)
    return n

def multiplicativeModInverse(a, b):
    for i in range(b):
        if (i * a) % b == 1:
            return i
    raise ValueError('Multiplicative mod inverse not found.')

def getKeys(primes=''):
    if primes == '':
        primes = generatePrimeNumbers()
    n = generateProduct(primes)
    lam = totient(primes)
    e = getRandomPrimeCoprimeNumber(lam)
    d = multiplicativeModInverse(e, lam)
    publicKey = (n, e)
    privateKey = (n, d)
    return publicKey, privateKey

def encrypt(m, publicKey):
    n = publicKey[0]
    e = publicKey[1]
    return (m ** e) % n

def decrypt(c, privateKey):
    n = privateKey[0]
    d = privateKey[1]
    return int((c ** d) % n)

def getAllPrimes(n):
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes += [i]
    return primes

def pairPermutatePrimes(n):
    lst1 = getAllPrimes(n)
    lst2 = lst1[:]
    permutateList = []
    for item1 in lst1:
        for item2 in lst2:
            permutateList += [[item1, item2]]
    return permutateList

def hashFunction(n):
    return (5 * n) % 100 + 1

def simulateCollisionAttack():
    print('\nCollision attack simulation:')
    key1 = random.randint(0, 1000)
    print('Original key: %s' % key1)
    count = 1
    key2List = list(range(1000))
    key2 = random.choice(key2List)
    while hashFunction(key2) != hashFunction(key1):
        key2List.remove(key2)
        key2 = random.choice(key2List)
        count += 1
    print('Collision attack occurred with original key key1 = ' + str(key1)
          + ' and key2 = ' + str(key2) +  ', hash value of '
          + str(hashFunction(key1)) + '.')

def main():
    answer = raw_input("Run sample or random? ")
    while answer not in ['s', 'sample', '1'] + ['r', 'random', '2']:
        answer = raw_input("Run sample or random? ")
    if answer in ['s', 'sample', '1']:
        m = 65
        print('Message: %s' % m)
        publicKey = (3233, 17)
        privateKey = (3233, 413)
        print('Public key: %s, Private key: %s' % (publicKey, privateKey))
        c = encrypt(m, publicKey)
        print('Encrypted message: %s' % c)
        m2 = decrypt(c, privateKey)
        print('Decrypted message: %s' % m2)
    else:
        m = random.randint(2, 100)
        print('Message: %s' % m)
        publicKey, privateKey = getKeys()
        print('Public key: %s, Private key: %s' % (publicKey, privateKey))
        c = encrypt(m, publicKey)
        print('Encrypted message: %s' % c)
        m2 = decrypt(c, privateKey)
        print('Decrypted message: %s' % m2)

    simulateCollisionAttack()

if __name__ == '__main__':main()
