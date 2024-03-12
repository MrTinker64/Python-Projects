from functools import lru_cache

sequence = []

@lru_cache(maxsize=None)  # Unlimited cache
def iterative_loop(n: int):
    if len(sequence) >= 8:
        print(sequence)
    else:
        sequence.append(round(n, 1))
        iterative_loop(0.5*n+4)
    
iterative_loop(int(input("Starting value: ")))