from functools import lru_cache

@lru_cache(maxsize=None)  # Unlimited cache
def factorial(n: int):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(0))