def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

try:
    n = int(input("Enter a number: "))
    while n != 1:
        n = collatz(n)
except ValueError:
    print("Please enter a valid integer.")
