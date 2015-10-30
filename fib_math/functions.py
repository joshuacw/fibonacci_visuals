import scipy.constants
import decimal

#implementing Binet's formula to produce the Nth term
def nth_term(term):
    phi = scipy.constants.golden
    return int(round((phi**term - (1 - phi)**term) / 5**0.5))

#produces a list of the first N Fibonacci terms
def fib_list(term): 
    fib_list = [0, 1]
    for i in range(2, term + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list

#produces a list of the first N prime numbers
def prime_list(term): 
    prime_list = [2]
    number = 3

    while len(prime_list) < term + 1:
        counter = 0
        for n in range(2, number):
            if number % n == 0:
                counter += 1
            else:
                counter += 0
        if counter == 0:
            prime_list.append(number)
        number += 1
    return prime_list

# check how many digits quotient of last 2 terms matches phi out to
def phi_match(term):
    phi1000list = []
    phi_dec_list = []
    with open('phi1000.txt', 'r') as phi:
        phi1000 = phi.read()
        phi_dec = str(decimal.Decimal(nth_term(term)) / decimal.Decimal(nth_term(term - 1)))

        for char in phi1000:
            phi1000list.append(char)

        for char in phi_dec: 
            phi_dec_list.append(char)

    for i in range(1001):
        if(phi1000list[i] == phi_dec_list[i]):
            i += 1
        else:
            break

    return i - 1
