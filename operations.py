# Markhus Dammar
# 2/11/2020
# This program demonstrates list operations, like sorting numbers, etc...

import time
from collections import Counter

print("""--------------------------
Welcome.
For some reason, I really want to do some math,
but first I need your help.
Give me a whole number (one at a time) and hit enter. 
I need 5 digits in total
--------------------------""")

numbers = []

for number in range(5):
    usernumbers = input(">>> ")
    numbers.append(usernumbers)

print(f"Your numbers are: {numbers}")
numbers_copy = list(numbers)
numbers_copy2 = list(numbers)

print("Cool. Let's do some math!")
time.sleep(0.5)
input("Press ENTER to continue")

print("I need to sort the numbers first...")
numbers.sort()
numbers_copy.sort()
time.sleep(1.5)
print(numbers)
time.sleep(1.5)

print("\nNow, I'm gonna find the sum of your numbers...")
time.sleep(1.5)
total = 0
for adding in numbers:
    total = total + int(adding)
print(f"The sum is {total}.")
time.sleep(2)

print("\nOkay, I want the product of your numbers now...")
time.sleep(1.5)
product = 1
for multiply in numbers:
    product = product * int(multiply)
print(f"The product is {product}.")
time.sleep(2)

print(f"""\nNext, Let's calculate the mean.
We have a total of {total} and 5 numbers, so...""")
time.sleep(1.3)
mean = total / 5
print(f'Our mean for this set is {mean}')
time.sleep(2)

print("\nWell that was easy!")
print("I'm gonna get the median now. This is even easier!")
time.sleep(1.5)
print(f"The median is {numbers[2]}")
time.sleep(2)

print("\nAnd now, to find the mode, or most recurring number")
time.sleep(1.5)
n = len(numbers_copy2)

data = Counter(numbers_copy2)
the_mode = dict(data)
calc_mode = [k for k, v in the_mode.items() if v == max(list(data.values()))]

if len(calc_mode) == n:
    the_mode = "There is no mode!"
else:
    the_mode = "Mode is: " + ', '.join(map(str, calc_mode))
print(the_mode)
time.sleep(2)

print(f"\nThe largest number in the list is {numbers[4]}")
time.sleep(1.5)
print(f"The smallest number in the list is {numbers[0]}")
time.sleep(2)

numbers_copy = list(set(numbers_copy))
print("\nHere is the list without duplicates...")
time.sleep(1)
numbers_copy.sort()
print(numbers_copy)
time.sleep(2)


def split(numbers_copy2):
   even = []
   odd = []
   for i in numbers_copy2:
      if int(i) % 2 == 0:
         even.append(i)
      else:
         odd.append(i)
   print("\nHere is the list without Odds:", even)
   print("Here is the list without Evens:", odd)


split(numbers_copy2)

time.sleep(2)

userinput = input("\nType in a number, and we'll see if it is in the list >>>")
while userinput != numbers[0] or userinput != numbers[1] or userinput != numbers[2] or userinput != numbers[3] or userinput != numbers[4]:
    print(f"{userinput} is NOT in the list.")
    userinput = input("\nType in a number, and we'll see if it is in the list >>>")
    if userinput in numbers:
        print(f"{userinput} is in the list.")
        break

print("Last thing, because this was actually extremely easy.")
time.sleep(2)
print("Since the numbers list is already sorted, the second largest number is:")
time.sleep(2)
print(numbers[3])
time.sleep(3)
print("Thanks for watching me do math. Have a great day.")
time.sleep(1.3)
exit()


