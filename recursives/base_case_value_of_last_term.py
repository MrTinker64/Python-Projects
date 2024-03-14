from functools import lru_cache

sequence = []

@lru_cache(maxsize=None)  # Unlimited cache
def iterative_loop(n: int):
    sequence.append(round(n, 1))
    if sequence[len(sequence) - 1] >= 0:
        print(sequence)
        print(f"Length: {len(sequence)}")
    else:
        iterative_loop(1.04*n+75)
    
iterative_loop(int(input("Starting value: ")))