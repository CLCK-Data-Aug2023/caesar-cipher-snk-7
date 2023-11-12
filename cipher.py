letters = "abcdefghijklmnopqrstuvwxyz"
new_letters = "fghijklmnopqrstuvwxyzabcde"

user_phrase = input("Please enter a sentence: ")

new_phrase = ''

l = "TEST"
user_phrase = user_phrase.lower()
print(l)

for letter in user_phrase:
    if letter in letters:
        new_phrase += new_letters[letters.index(letter)]
    else:
        new_phrase += letter

print("The encrypted sentence is:", new_phrase)# add your code here
