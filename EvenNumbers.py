def is_even(num):
    if number % 2 == 0:
        return True
    else:
        return False

# Example usage:
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
