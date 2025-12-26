
"""
experiments.py

Demonstrations for:
- p-adic convergence of left-infinite digit sequences (...99999 → -1)
- real convergence of right-infinite decimals (.99999... → 1)
- generating constant-digit zero patterns
"""

# ---------------------------------------
# 1. Right-infinite approximation of 0.999...
# ---------------------------------------

def right_infinite_real(limit=20):
    """
    Approximates 0.99999... using partial real series:
        ∑ 9/10^n
    """
    s = 0
    for n in range(1, limit+1):
        s += 9 * (10 ** -n)
    return s


# ---------------------------------------
# 2. Left-infinite approximation for ...99999
# ---------------------------------------

def left_infinite_p_adic(n):
    """
    Returns 10^n - 1.
    In p-adics, this approaches -1 as n increases.
    """
    return (10 ** n) - 1


# ---------------------------------------
# 3. Generate constant-digit zero patterns
# ---------------------------------------

def constant_digit_block(digit=8, length=10):
    """
    Returns a constant digit string of the form ddddd.ddddd (finite version).
    Used to illustrate that ...ddd.ddd... = 0 in your representation.
    """
    left = str(digit) * length
    right = str(digit) * length
    return f"{left}.{right}"


# ---------------------------------------
# Demo Execution
# ---------------------------------------

if __name__ == "__main__":
    print("\nRight-infinite approximation to 0.99999...")
    for n in [5, 10, 15, 20]:
        print(f"  n={n:<2} → {right_infinite_real(n)}")

    print("\nLeft-infinite approximation of ...99999")
    for n in range(1, 8):
        print(f"  n={n:<2} → {left_infinite_p_adic(n)}")

    print("\nExample constant zero-pattern blocks:")
    for d in [9, 8, 5, 2]:
        print(f"  Pattern for '{d}': {constant_digit_block(d)}")
