def check_prime(n):
    if n ==1:
        return "1 is not prime nor composite"
    if n == 2:
        return "2 is prime"
    for i in range(2, int(n**(0.5)+1)):
        if n % i == 0:
            return f"{n} is not a prime number"
        else:
            return f"{n} is a prime number"
        
print(check_prime(66))