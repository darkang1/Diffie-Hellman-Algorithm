# Diffie-Hellman Key Generator class that is used to generate partial/full keys for clients using their public and private key and other client's public key
class DiffieHellmanKeyGenerator:
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key

    # Method to create a partial encryption key using client's private and public key and other client's public key
    def generate_partial_key(self):
        return (self.public_key1 ** self.private_key) % self.public_key2
    
    # Method to generate a full key with which we can encrypt message for other client or decrypt other client message
    def generate_full_key(self, other_partial_key):
        return (other_partial_key ** self.private_key) % self.public_key2
