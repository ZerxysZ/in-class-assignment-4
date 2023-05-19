allowed_letters = {'I', 'O', 'S', 'H', 'Z', 'X', 'N'}
word_input = input()

for letter in word_input:
    if letter not in allowed_letters:
        print("NO")
        break
else:
    print("YES")
