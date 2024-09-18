numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers[1:]:
    for j in numbers[1:]:
        if i%j == 0 and i != j:
            not_primes.append(i)
            break
        elif i % j !=1 and i != j:
            primes.append(i)
            break
print (primes)
print (not_primes)
# я потратил на этот код в общей сложности 6 часов и много нервных клеток, а ошибка была в том, что
# я написал elif i % j ! = 0, а нужно было единицу!!!!!

