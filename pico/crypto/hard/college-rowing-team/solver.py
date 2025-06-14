import sys

# Helper function for the Iterative Extended Euclidean Algorithm
def iterative_egcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd
    """
    x, prev_x = 0, 1
    y, prev_y = 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, prev_x = prev_x - q * x, x
        y, prev_y = prev_y - q * y, y
    return a, prev_x, prev_y

# Updated modinv to use the iterative version of egcd
def modinv(a, m):
    """
    Returns x such that (a * x) % m == 1
    """
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

# Helper function for the Chinese Remainder Theorem (no changes here)
def chinese_remainder_theorem(items):
    N = 1
    for n, _ in items:
        N *= n
    
    result = 0
    for n_i, a_i in items:
        p = N // n_i
        result += a_i * modinv(p, n_i) * p
    return result % N

# Helper function for integer cube root using binary search (no changes here)
def integer_cbrt(n):
    if n < 0:
        return -integer_cbrt(-n)
    if n == 0:
        return 0
    x = 0
    # Set an initial guess for y. (bit_length + 2) // 3 is a good starting point.
    y = 1 << ((n.bit_length() + 2) // 3)
    while x != y:
        x = y
        y = (2 * x + n // (x * x)) // 3
    # Check if we found a perfect cube
    if x**3 != n:
        if (x+1)**3 == n:
            return x + 1
    return x

# Helper function to convert a large integer to bytes (no changes here)
def long_to_bytes(n):
    if n < 0:
        return b''
    length = (n.bit_length() + 7) // 8
    return n.to_bytes(length, 'big')

# --- Main Decryption Logic ---

# 1. Read and parse the file
try:
    with open('encrypted-messages-ori.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: 'encrypted-messages-ori.txt' not found.")
    print("Please ensure the file from the CTF challenge is in the same directory.")
    sys.exit(1)

entries = content.strip().split('\n\n')
parsed_data = []
for entry in entries:
    lines = entry.strip().split('\n')
    if len(lines) == 3:
        try:
            n = int(lines[0].split(': ')[1])
            c = int(lines[2].split(': ')[1])
            parsed_data.append({'n': n, 'c': c})
        except (ValueError, IndexError):
            # Skip malformed entries, if any
            continue

# 2. Group moduli by common ciphertext
grouped_by_c = {}
for item in parsed_data:
    c = item['c']
    if c not in grouped_by_c:
        grouped_by_c[c] = []
    grouped_by_c[c].append(item['n'])

# 3. Decrypt each group
print("Attempting to decrypt messages...\n")
for c, ns in grouped_by_c.items():
    if len(ns) >= 3:
        n1, n2, n3 = ns[0], ns[1], ns[2]
        
        congruences = [(n1, c), (n2, c), (n3, c)]
        
        m_cubed = chinese_remainder_theorem(congruences)
        
        m = integer_cbrt(m_cubed)
        
        try:
            decrypted_message = long_to_bytes(m)
            # Filter for printable ASCII to find the flag and readable messages
            if all(32 <= char < 127 for char in decrypted_message) and decrypted_message:
                 print(f"✅ Decrypted: {decrypted_message.decode('utf-8')}")
            else:
                 print(f"ℹ️  Decrypted data (non-printable): {decrypted_message}")
        except Exception as e:
            print(f"Could not decode message. Error: {e}")
