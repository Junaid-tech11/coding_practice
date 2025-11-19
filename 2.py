num = int(input("Enter a number: "))

if num <= 1:
    print("It is not prime number")

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("it is prime number")
