# Consider a positive number n. Determine all its decompositions as sums of prime numbers.

import math

array = []


def isprime(i):
    if i == 2:
        return True
    if i < 2:
        return False
    if i % 2 == 0:
        return False
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            return False
    return True


def bkt_it(n, prime: list):
    for i in range(len(prime)):
        v = []

        j = i
        v.append(prime[i])
        while j < len(prime):
            if n - sum(v) < prime[j]:
                v.pop()
            while sum(v) < n:
                v.append(prime[j])

                if sum(v) == n:
                    print(v)
                    v.pop()
                    break

            if n - sum(v) < prime[j]:

                v.pop()
                if len(v) > 1:
                    v.pop()

            j = j + 1


def bkt_rec(n, first_num=1):
    # i = the number we want to add in the sum
    if n == 0:
        print(" + ".join(array))
    else:
        for i in range(first_num, n + 1):
            if isprime(i) == True:
                array.append(str(i))
                bkt_rec(n - i, i)
                array.pop()


def choose_way():
    print("Choose a way to solve the problem:")
    print("1-iterative")
    print("2-recursive")
    way = int(input("->"))
    n = int(input("Choose a number:"))
    prime = []
    remainder = n
    # We put in an array all the prime numbers smaller or equals to the number n
    for i in range(1, n + 1):
        if isprime(i) == True:
            prime.append(i)
    if way == 1:
        bkt_it(n, prime)
    else:
        bkt_rec(remainder, first_num=2)


print(choose_way())
