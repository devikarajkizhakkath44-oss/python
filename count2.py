names_inp = input("Enter a list of names separated by spaces:")
names = names_inp.split()
count_a =''.join(names).lower().count('a')
print("Total occurrence of 'a':",count_a)