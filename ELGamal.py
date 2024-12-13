import random  # for generating random numbers

# check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# generate a prime number and its primitive root
def generate_prime_and_primitive_root():
    while True:
        p = random.randint(1000, 50000)  
        if is_prime(p):
            return p, 2  

# function to get the modular exponentiation g^exp % mod
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# get public and private keys
def generate_keys(p, g):
    x = random.randint(1, p-2)  # private key
    h = mod_exp(g, x, p)  # public key 
    return (p, g, h), x

# encrypt the message
def encrypt(public_key, M):
    p, g, h = public_key
    k = random.randint(1, p-2)
    c1 = mod_exp(g, k, p)
    c2 = (M * mod_exp(h, k, p)) % p
    return c1, c2

# decrypt the message
def decrypt(private_key, p, c1, c2):
    s = mod_exp(c1, private_key, p)
    s_inv = mod_exp(s, p - 2, p)  # inverse of s
    return (c2 * s_inv) % p

# terminal commands
if __name__ == "__main__":
    p, g = generate_prime_and_primitive_root()  # get the prime number and primitive root
    print(f"prime number (p): {p}")
    print(f"primitive root (g): {g}")
    
    # inputs
    while True:
        message = int(input("enter your message (must be intger and less than prime): "))
        if message < p:
            break
        print(f"message must be smaller than the prime number {p}")
    
    # generate keys
    public_key, private_key = generate_keys(p, g)
    print(f"private key: {private_key}")

    # encrypt the message
    ciphertext = encrypt(public_key, message)
    print(f"ciphertext: {ciphertext}")

    # decrypt the message
    decrypted_message = decrypt(private_key, p, *ciphertext)
    print(f"decrypted message: {decrypted_message}")