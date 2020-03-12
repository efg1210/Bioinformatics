a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
sum = 0

for x in range(a, b+1):
    if x % 2 == 1:
        sum+=x
        #print(x)

print(sum)