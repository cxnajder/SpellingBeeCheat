letters = input("The letters are... ").lower()
letters = "".join(dict.fromkeys(letters))

middle_letter = input("The middle letter is... ").lower()
middle_letter = middle_letter[0]

if middle_letter not in letters:
    letters = letters + middle_letter

print("")
print("Letters list:", letters.upper())
print("Main letter:", middle_letter.upper())

words = []
with open("word-list.txt", "rt") as wordsFile:
    for line in wordsFile:
        word = line.strip()
        if middle_letter in word:
            words.append(word.lower())

answers = []

for word in words:
    itFits = True
    for letter in word:
        if letter[0] not in letters:
            itFits = False
    if itFits:
        answers.append(word)


print("")
print("Ok, here we go...")
print("")

for answer in answers:
    print(answer)


