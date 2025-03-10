
def numbers():
    numbers = int(input("Enter a numbers: "))
    if numbers % 2 == 0:
        print()
        print(numbers, "is = even number")
    else:
        print()
        print(numbers, "is = odd number")
 
numbers()

while True:
    print()
    a = input(" again?: y/n ")
    if a == "y":
        numbers()

    else:
        print()
        b = print("OKE BYE")
        break 