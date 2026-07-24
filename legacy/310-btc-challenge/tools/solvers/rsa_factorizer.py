#!/usr/bin/env python3
"""
RSA Factorization Tool
For educational purposes in the 310 BTC Challenge
"""

import math
import time
from sympy import isprime, nextprime

def isqrt(n):
    """Integer square root"""
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def fermat_factor(n):
    """Fermat's factorization method"""
    if n % 2 == 0:
        return 2, n // 2
    
    a = isqrt(n) + 1
    b2 = a * a - n
    
    while True:
        b = isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1
        b2 = a * a - n

def pollard_rho(n):
    """Pollard's Rho algorithm"""
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    d = 1
    f = lambda x: (x * x + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    
    return d

def trial_division(n, limit=10000):
    """Simple trial division"""
    for p in range(2, limit):
        if n % p == 0:
            return p
    return None

print("""
╔══════════════════════════════════════════════════════════╗
║           🔢 RSA FACTORIZATION TOOL 🔢                  ║
║     Educational tool for the 310 BTC Challenge           ║
╚══════════════════════════════════════════════════════════╝

This tool demonstrates RSA factorization methods.
Use it to understand the mathematics behind cryptography.

Methods available:
1. Trial Division (simple)
2. Fermat's Factorization (for close primes)
3. Pollard's Rho (probabilistic)
""")

def main():
    print("\nEnter a composite number to factorize:")
    try:
        n = int(input("N = "))
        
        if n < 2:
            print("Please enter a number >= 2")
            return
        
        print(f"\nFactoring {n}...")
        start = time.time()
        
        # Try different methods
        print("\nTrying trial division...")
        factor = trial_division(n)
        
        if factor:
            print(f"✓ Found factor: {factor}")
            print(f"  {n} = {factor} × {n // factor}")
        else:
            print("✗ Trial division failed")
            
            print("\nTrying Fermat's method...")
            try:
                p, q = fermat_factor(n)
                print(f"✓ Found factors: {p} × {q} = {n}")
            except:
                print("✗ Fermat's method failed")
                
                print("\nTrying Pollard's Rho...")
                factor = pollard_rho(n)
                if factor and factor != n:
                    print(f"✓ Found factor: {factor}")
                    print(f"  {n} = {factor} × {n // factor}")
                else:
                    print("✗ Pollard's Rho failed")
        
        elapsed = time.time() - start
        print(f"\n⏱️ Time elapsed: {elapsed:.3f}s")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
