class Option:
    def __init__(self, T):
        self.T = T
        
def some(T):
    return Option(T)

def run(input: Option, transformFunction):
    return transformFunction(input)

def hi(option: Option):
    return f"Hi {option.T}!"

inputAsOption = some(input("Name here: "))

print(run(inputAsOption, hi))