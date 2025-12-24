#Сколько слов начинается с "е"
text = input()

words = text.split()
count = 0

for word in words:
    # убираем запятые и точки и делаем буквы маленькими
    clean_word = word.strip(".,!?").lower()
    
    if clean_word.startswith("е"):
        count += 1

print(count)


