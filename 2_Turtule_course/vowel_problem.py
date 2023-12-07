def is_vowel(char):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if char in vowels:
        print("Its a vowel")
    else:
        print("Its a Consonant")
while True:
    print("Enter A Character")
    char = input("=>")
    is_vowel(char)