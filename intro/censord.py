"""print("skriv en mening is svenska")
sentence = input()

Banwords = "ö,å,å"
for letter in sentence:
    if letter in Banwords:
        print(sentence)

"""
print("skriv en mening is svenska")
sentence = input()
new_sentence = ""

for letter in sentence:

    is_uppercase = True
else:
    is_uppercase = False


    if letter.lower() == "ö":
        if is_uppercase:
            new_sentence += "O"
        else:
            new_sentence += "o"
           

    elif letter.lower() == "ä" or letter.lower()== "å":
        if is_uppercase:
            new_sentence == "A"
        else:
            new_sentence += "a"

    else:
        new_sentence += letter
    
    print(new_sentence)