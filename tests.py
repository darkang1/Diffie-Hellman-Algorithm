import random
from diffie_hellman import DiffieHellmanKeyGenerator

# Checking if specified number is prime or not
def isPrime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

# Generating a prime number array withing specified range
def generatePrimesArray(start, end):
    return [i for i in range(start,end) if isPrime(i)]

# Generating a randomized prime number array withing specified range and amount of numbers to be generated
def generateRandomPrimesArray(count, start = 1, end = 1000):
    primesInRange = generatePrimesArray(start, end)
    primesArray = []
    
    for i in range(0, count):
        primesArray.append(random.choice(primesInRange))
    
    return primesArray

# Simulation function of two clients
def simulation(client1_public, client1_private, client2_public, client2_private):
    print(f'Client1 public key: {client1_public}. Client1 private key: {client1_private}. Client2 public key {client2_public}. Client2 private key: {client2_private}')

    Client1 = DiffieHellmanKeyGenerator(client1_public, client2_public, client1_private)
    Client2 = DiffieHellmanKeyGenerator(client1_public, client2_public, client2_private)

    client1_partial = Client1.generate_partial_key()
    client2_partial = Client2.generate_partial_key()
    client1_full = Client1.generate_full_key(client2_partial)
    client2_full = Client2.generate_full_key(client1_partial)

    print(f'Partial key generated for Client1: {client1_partial}')
    print(f'Partial key generated for Client2: {client2_partial}')
    print(f'Full key generated for Client1: {client1_full}')
    print(f'Full key generated for Client2: {client2_full}')
    
    if client1_full == client2_full:
        print('Test is successful. Full keys are equal')
    else:
        print('Test failed. Full keys are not equal')

# Simulation starting function
def test():
    primes = generateRandomPrimesArray(4)
    simulation(primes[0], primes[1], primes[2], primes[3])

if __name__ == '__main__':
    print('Enter how many tests you want to run: ')
    num_of_tests = int(input())

    if (num_of_tests > 0):
        separator_string = '------' 
        print('Generated tests:')
        for i in range(0, num_of_tests):
            print(separator_string)
            test()
    else:
        print(f'Invalid number of tests. Should be at least 1. User input: {num_of_tests}')