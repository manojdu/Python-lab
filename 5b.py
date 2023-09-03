def display_first_n_lines(filename, n):
  with open(filename, 'r') as file:
    lines = file.readlines()
    for i in range(min(n,len(lines))):
      print(lines[i].strip())

def display_word_frequency(filename, word):
  with open(filename, 'r') as file:
    content = file.read()
    word_count = content.count(word)
    print("The number of occurences are---->",word_count)

filename = input("Enter the name of the File: ")
n = int(input("Enter the number of lines to display: "))
display_first_n_lines(filename, n)

word = input("Entner the word to find its frequency: ")
display_word_frequency(filename, word)