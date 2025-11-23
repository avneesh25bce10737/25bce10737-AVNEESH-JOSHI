def find_gcd(a,b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)  
            break

def find_prime_factors(n):
    n = int(n)
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            temp //= d
        else:
            d += 1
    if temp > 1:
        factors.append(temp) 
    print(factors)    
def fast_power(base,power):
    base=float(base)
    power=float(power)
    ans=base**power
    print(ans)
def base_conversion(number, base):
  number_int = int(number)
  base_int = int(base)

  if number_int == 0:
    print('0')
    return

  new_digits = []
  temp = number_int

  while temp > 0:
    remainder = temp % base_int
    new_digits.append(int(str(remainder)))
    temp //= base_int
  print(new_digits[::-1])   
