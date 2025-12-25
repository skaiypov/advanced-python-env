# text to alphabet

text = input()
words = text.split()

print("sorted:")

for w in words:

    sorted_letters = sorted(w)
    
    # Print letters one by one
    for letter in sorted_letters:
        print(letter, end="")
    
    # space between words
    print(end=" ")

