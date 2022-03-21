from cipher import SimpleCipher
from diffie_hellman import DiffieHellmanKeyGenerator

#Some prime numbers for testing
#C1Public = 197, 757, 991
#C1Private = 199, 571, 89
#C2Public = 151, 53, 677
#C2Private = 157, 823, 139

if __name__ == '__main__':
    print('Client1: Enter your public key (must be a prime number):')
    client1_public = int(input())
    
    print('Client1: Enter your private key (must be a prime number):')
    client1_private = int(input())

    print('Client2: Enter your public key (must be a prime number):')
    client2_public = int(input())

    print('Client2: Enter your private key (must be a prime number):')
    client2_private = int(input())

    Client1 = DiffieHellmanKeyGenerator(client1_public, client2_public, client1_private)
    Client2 = DiffieHellmanKeyGenerator(client1_public, client2_public, client2_private)

    client1_partial = Client1.generate_partial_key()
    client2_partial = Client2.generate_partial_key()

    print(f'Partial key generated for Client1: {client1_partial}')
    print(f'Partial key generated for Client2: {client2_partial}')

    client1_full = Client1.generate_full_key(client2_partial)
    client2_full = Client2.generate_full_key(client1_partial)

    print(f'Full key generated for Client1: {client1_full}')
    print(f'Full key generated for Client2: {client2_full}')

    print(f'Input text to cipher:')
    text = input()
    ciphertext = SimpleCipher.encrypt_message(text, client1_full)
    print(f'Ciphered message: {ciphertext}')
    deciphertext = SimpleCipher.decrypt_message(ciphertext, client1_full)
    print(f'Deciphered message: {deciphertext}')
