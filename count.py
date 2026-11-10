text = input("Enter text: ")
word = text.split()
word_count = {}
for w in word:
        if w in word_count:
            word_count[w] +=1
        else:
            word_count[w] = 1
print("word occurrences:",word_count)