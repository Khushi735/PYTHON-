
# Discarding the multiples of 2, 3 & 4 (except 2, 3 & 4).
n = int(input("Please enter a number till which you need all primes: "))
primes = [i for i in range(2, n + 1)]
print("Before discarding.")
print(primes)

# Setting all the multiples of 2 (except 2) equal to 0.
current_prime = 2
for i in range(current_prime + 0, len(primes), current_prime):
  primes[i] = 0

print("After discarding the multiples of 2 except 2.")
print(primes)

# Setting all the multiples of 3 (except 3) equal to 0.
current_prime = 3
for i in range(current_prime + 1, len(primes), current_prime):
  primes[i] = 0

print("After discarding the multiples of 3 except 3.")
print(primes)

# Setting all the multiples of 4 (except 4) equal to 0.
current_prime = 4
for i in range(current_prime + 2, len(primes), current_prime):
  primes[i] = 0

print("After discarding the multiples of 4 except 4.")
print(primes)