a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral")

    elif a == b or b == c or a == c:
        print("Isosceles")

    else:
        print("Scalene")

else:
    print("Invalid Triangle")