import Levenshtein
s1 = input("Enter a sentence 1: ")
s2 = input("Enter a sentence 2: ")

similarity = 1 - (Levenshtein.distance(s1, s2)/max(len(s1),len(s2)))

print("The string similarity between {} and {} is {}".format(s1,s2,similarity))