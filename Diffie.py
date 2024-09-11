import random

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def diffie_hellman(p, g):
    print(f"Public parameters:\nPrime (p): {p}\nBase (g): {g}\n")
    
    a = random.randint(1, p-1)
    print(f"Alice's private key (a): {a}")
    
    b = random.randint(1, p-1)
    print(f"Bob's private key (b): {b}")
    
    A = mod_exp(g, a, p)
    print(f"Alice's computed value (A): {A}")
    
    B = mod_exp(g, b, p)
    print(f"Bob's computed value (B): {B}\n")
    
    S_Alice = mod_exp(B, a, p)
    
    S_Bob = mod_exp(A, b, p)
    
    print(f"Alice's shared secret key: {S_Alice}")
    print(f"Bob's shared secret key: {S_Bob}")
    
    assert S_Alice == S_Bob, "Error: Keys do not match!"
    print("\nKey exchange successful! Both parties have the same shared secret key.")

if __name__ == "__main__":
    p = 23
    g = 5
    
    diffie_hellman(p, g)