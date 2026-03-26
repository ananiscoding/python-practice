# Greeting with parameter
def hello(name):
    print("Hello, " + name)

hello("Siam")

# Return values
def square(n):
    return n * n

result = square(5)
print(result)

# Local vs global scope demo
eggs = "global"

def show_scope():
    eggs = "local"
    print("Inside function:", eggs)

show_scope()
print("Outside function:", eggs)