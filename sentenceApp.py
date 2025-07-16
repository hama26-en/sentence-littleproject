sentence = input("This is a test sentence ")

char_count = 0
word_count = 1
vowel_count = 0

for char in sentence:
    char_count += 1
    if char == ' ':
        word_count += 1
    if char.lower() in 'aeiou':
        vowel_count += 1

char_count -= 1

print("Character count:", char_count)
print("Word count:", word_count)
print("Vowel count:", vowel_count)
