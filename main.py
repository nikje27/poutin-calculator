num1 = int(input("enter First number: "))
num2 = int(input("enter second number: "))

print("enter which operation would you like to perform?")
ch = input("enter -")

result = 0
if ch == '-':
    result = num1 - num2
else:
    exit()
print(num1, ch , num2, ":", result)