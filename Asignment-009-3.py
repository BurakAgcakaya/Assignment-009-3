num = int(input("Enter a number: "))
y = len(str(num))
sum = 0
while num > 0:
   digit = num % 10
   sum += digit ** y
   num //= 10
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")