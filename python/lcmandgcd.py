def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_result = find_gcd(num1, num2)
lcm_result = find_lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
