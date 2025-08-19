# Readability
# Prompt user for input text
text = input("Text: ")

letters = 0
words = 1   # start at 1 because last word won't be followed by a space
sentences = 0

# Count letters, words, and sentences
for char in text:
    if char.isalpha():
        letters += 1
    elif char == " ":
        words += 1
    elif char in [".", "!", "?"]:
        sentences += 1

# Compute averages number of letters and sentences for 100 words
L = (letters / words) * 100
S = (sentences / words) * 100

# Coleman–Liau index
grade = round(0.0588 * L - 0.296 * S - 15.8)

# Output result
if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
