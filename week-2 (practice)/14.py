#Вывести слова, которые начинаются с "a" и заканчиваются на "i"

text = input("Enter a line: ")

words = text.split()

print("Words starting with 'a':")
for word in words:
    if word.lower().startswith("a"):
        print(word)

print("Words ending with 'i':")
for word in words:
    if word.lower().endswith("i"):
        print(word)
