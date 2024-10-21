#In the Tennis world, all the vowels are replaced with t/T.
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "T"
            else:
                translation += "t"
        else:
            translation += letter
    return translation

print(translate("hello world"))