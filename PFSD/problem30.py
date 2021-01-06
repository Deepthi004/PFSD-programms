one = int(input("Enter the first number:"))
two = int(input("Enter the Second Number:"))
for i in range(one, two):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print("Prime Number", i)
