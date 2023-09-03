#3 a) Write a Python program that accepts a sentence and find the number of words, digits, uppercase letters and lowercase letters
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
digit_count = sum(i.isdigit() for i in sentence)
uppercase_count = sum(i.isupper() for i in sentence)
lowercase_count = sum(i.islower() for i in sentence)

print("Number of words: ", word_count);
print("Number of Digits", digit_count)
print("Number of Uppercase Letters", uppercase_count)
print("Number of Lowercase Letters", lowercase_count)