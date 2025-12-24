#Посчитать количество слов с точкой

text = "This is a simple sentence."

text = text[:-1]

words = text.split()

word_count = len(words)

print("Number of words:", word_count)
