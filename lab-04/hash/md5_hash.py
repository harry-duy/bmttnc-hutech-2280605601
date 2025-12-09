import struct
import math

# MD5 constants
# T-constants, derived from the sine function
K = [int(abs(math.sin(i + 1)) * 2**32) for i in range(64)]

# Shift amounts
S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    # Initialize variables
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    
    # Pre-processing
    msg = bytearray(message, 'utf-8')
    msg_len = len(msg) * 8
    msg.append(0x80)
    
    while len(msg) % 64 != 56:
        msg.append(0)
    
    msg += struct.pack('<Q', msg_len)
    
    # Process message in 512-bit chunks
    for offset in range(0, len(msg), 64):
        chunk = msg[offset:offset + 64]
        M = list(struct.unpack('<16I', chunk))
        
        A, B, C, D = a0, b0, c0, d0
        
        # Main loop
        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                F = C ^ (B | ~D)
                g = (7 * i) % 16
            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, S[i])) & 0xFFFFFFFF
        
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF
    
    # Pack the final hash values as little-endian unsigned integers
    digest = struct.pack('<IIII', a0, b0, c0, d0)
    return digest.hex()

if __name__ == "__main__":
    message = input("Enter message to hash: ")
    hash_result = md5(message)
    print(f"MD5 Hash: {hash_result}")
