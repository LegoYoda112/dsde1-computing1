print("Counting up to 10...")

number = 0
while number <= 10:
    print(number)
    number += 1

print("---------")
print("Counting down from 10 using for...")

number = 10
for i in range(10, -1, -1):
    print(i)