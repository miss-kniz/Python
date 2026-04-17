# Given this list:
numbers = [1, 2, 3, 4, 5]

# 1. Use a FOR loop to print each number squared
for n in numbers:
    print(n**2)
# 2. Use a LIST COMPREHENSION to create a new list of even numbers only
evenNumbers = [n for n in numbers if n%2==0];

print("Even Numbers: ",evenNumbers)
# 3. (Bonus) Use comprehension to create [4, 16, 36] from numbers (even numbers squared)

squaredEvenNumber = [n**2 for n in evenNumbers]
print("Square of even numbers: ", squaredEvenNumber)