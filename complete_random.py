import random

rando = random.randint(1, 999999999999999999999999999)

def random_consecutive_numbers(target_sum):
    while True:
        a = random.randint(1, target_sum // 3)  # Pick a starting number
        b = random.randint(a + 1, target_sum - 1)  # Ensure b > a
        c = target_sum - (a + b)  # Calculate c to ensure sum is 108

        if b > a and c > b:  # Ensure they are strictly increasing (consecutive)
            return a, b, c


numbers = random_consecutive_numbers(rando)
print("Three random consecutive numbers that sum to", {rando}, numbers)
input("\nPress Enter to Exit")