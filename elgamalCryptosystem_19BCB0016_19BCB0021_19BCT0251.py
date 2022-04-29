# ElGamal Using Python
# 19BCB0016
# 19BCB0021
# 19BCT0251


import random


def power(a, b):  # Function to generate a^b
    # Anything power 0 is 1
    if(b == 0):
        return 1

    # Initialize power value with 1
    pow = 1

    # Multiplying a to pow b times
    for i in range(1, b + 1):
        pow = a * pow

    return pow


def powerMod(a, b, c):  # Function to generate (a^b) mod c
    # Anything power 0 is 1
    if(b == 0):
        return 1 % c

    # Initialize power value with 1
    pow = 1

    # Multiplying a to pow b times along with modulus operation
    for i in range(1, b + 1):
        pow = (a * pow) % c

    return pow % c


def primesInRange(x, y):  # Function to generate prime numbers between x & y
    # List to store prime numbers
    primeList = []
    for i in range(x, y):
        isPrime = True

        for num in range(2, i):
            # If divisible then not prime
            if i % num == 0:
                isPrime = False

        # If prime add to the list
        if isPrime:
            primeList.append(i)

    return primeList


def keyGeneration(p, g):  # Function to generate keys (Public and Private)
    # Generating private key
    privateKey = random.randint(2, p - 1)

    # Generating public key
    publicKey = powerMod(g, privateKey, p)

    return publicKey, privateKey


def encryption(p, g, publicKey):  # Function to encrypt message
    # Choosing randome number k
    k = random.randint(2, p - 1)

    # List to store cipher text characters
    ct = []

    # Getting input message
    message = input("Enter message = ")

    # Appending each character of message into cipher text
    for i in range(0, len(message)):
        ct.append(message[i])

    # Calculating cipher text 1
    c1 = powerMod(g, k, p)

    # Calculation cipher text 2 multiplier
    c2 = powerMod(publicKey, k, p)

    # Calculating cipher text using c2
    for i in range(0, len(ct)):
        # Converting each character to ascii then multiplying it
        ct[i] = c2 * ord(ct[i])

    return c1, ct


def decryption(p, privateKey, c1, c2):
    # Calculating x
    x = powerMod(c1, privateKey, p)

    # List to store plain text characters
    pt = []

    for i in range(0, len(c2)):
        # Calculating each character of plain text
        pt.append(chr(int(c2[i] / x)))

    # Joining all the characters to form a string
    plainText = ''.join(pt)

    return plainText


def main():  # Main Function

    print("##########################################################")
    print("################## ELGAMAL CRYPTOSYSTEM ##################")
    print("##########################################################")

    print("\n\n=== CHOOSING PRIME & GENERATOR ===")
    print("\nPlease wait .....\n")

    # Generating prime numbers between 10000 to 20000
    primeList = primesInRange(10000, 20000)

    # Choosing prime number (large public prime number)
    p = random.choice(primeList)
    print("Large public prime number (P) = ", p)

    # Choosing generator such than 2 <= g <= p-1
    g = random.randint(2, p - 1)
    print("Generator (G) = ", g)

    # Key Generation process where we generate private and public key
    print("\n\n=== KEY GENERATION ===")

    publicKey, privateKey = keyGeneration(p, g)

    print("\nPublic Key (a) = ", publicKey)
    print("Private Key (a) = ", privateKey)

    # Encryption
    print("\n\n=== ENCRYPTION ===\n")
    c1, c2 = encryption(p, g, publicKey)

    print("\nCipher text (C1) = ", c1)
    print("Cipher text (C2) = ", c2)

    # Decryption
    print("\n\n=== DECRYPTION ===")

    m = decryption(p, privateKey, c1, c2)

    print("\nDecrypted Message (M) = ", m)
    print("\n##########################################################\n")


main()
