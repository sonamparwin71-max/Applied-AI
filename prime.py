# Print prime numbers between 1 and 13

for num in range(1, 14):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)