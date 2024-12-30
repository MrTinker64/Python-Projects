def multiply(m, n):
    return (lambda x : lambda y : x + y) (m) (n)
    
print(multiply("two", "three"))