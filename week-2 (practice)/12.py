# Вывести слова, которые заканчиваются на "i"

text = input() 

words = text.split() 

for word in words: 
    last = word[-1].lower()  # берем последнюю букву и делаем строчной
    if last == "i": 
        print(word) 

