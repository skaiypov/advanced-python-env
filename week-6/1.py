#  Text File Analysis
#
# 1. Reads a .txt file (text.txt)
#
# Counts:
#    - Total number of lines
#    - Total number of words
#    - Frequency of each word
#
# 2. Save the analysis result into analysis.txt.



lines = 0
words = 0
dictionary = {}

with open("text.txt") as text_txt:
    for i in text_txt:
        lines += 1
        arr = i.strip().lower().split()
        words += len(arr)

        for j in arr:
            if j in dictionary:
                dictionary[j] += 1
            else:
                dictionary[j] = 1


with open("analysis.txt", "w") as analysis_txt:
    analysis_txt.write("lines: " + str(lines) + "\n")
    analysis_txt.write("words: " + str(words) + "\n\n")

    for i in dictionary:
        analysis_txt.write(i + ": " + str(dictionary[i]) + "\n")

