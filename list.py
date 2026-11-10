numbers = [-2,4,-5,9,-10,23,-12,32]
positive = [x for x in numbers if x>0]

print("Positive numbers:" , positive)


squares = [x*x for x in numbers]
print("Squares:",squares)

word ="computer"
vowels = [ch for ch in word if ch in "aeiouAEIOU"]
print("Vowels:" ,vowels)

ordinal_values = [ord(ch) for ch in word]
print("Ordinal values:", ordinal_values)