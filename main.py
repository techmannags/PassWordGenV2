import random

#reads the banned_words.txt file and turns it into a usable list
b = open("banned_words.txt", 'r')
banned = b.read()
banned_words = banned.splitlines()

#Reads the words_alpha.txt file and turns it into a usable list
w = open('words_alpha.txt', 'r')
words = w.read()
words_list = words.splitlines()

# selection = random.randint(0, len(words_list))
# print(words_list)
# print(selection)
# print(words_list[selection])

#Number Generator
#function that generates a random set of numbers
#it can be told the required length and generate that many numbers
#converts those numbers into a char to be printed
def numberstring(length_number):
    number_string = ""
    for n in range(int(length_number)):
        number_string = number_string + str(random.randint(0, 9))
    return number_string


#Word Generator
#Generates a random word based of word length requirement
#using all words
def generateword(Length_word):
    gen_word = words_list[random.randint(0, len(words_list))]
    if len(gen_word) > int(Length_word):
        gen_word = generateword(Length_word)
    return gen_word



test = input("Test command: ")

print(generateword(test))


        
