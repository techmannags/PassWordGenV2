import random

#reads the banned_words.txt file and turns it into a usable list
b = open("banned_words.txt", 'r')
banned = b.read()
banned_words = banned.splitlines()

#Reads the words_alpha.txt file and turns it into a usable list
w = open('words_alpha.txt', 'r')
words = w.read()
words_list = words.splitlines()

sc = open("char_random.txt", "r")
specchars = sc.read()
special_characters = specchars.splitlines()

gw = open("galls_words.txt", "r")
gallswords = gw.read()
galls_words = gallswords.splitlines() 


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
    gen_word = galls_words[random.randint(0, len(galls_words)-1)]
    if len(gen_word) != int(Length_word):
        gen_word = generateword(Length_word)
    return gen_word

#Generate a 12 character password as a temp 
#
def windowspassword():
    word_one = random.randint(4, 8)
    word_two = random.randint(4, 8)
    numbers_one = random.randint(2, 4)
    char_special = random.randint(0, len(special_characters)-1)
    if random.randint(0, 1) == 1:
        password = generateword(word_one).upper() + " " + generateword(word_two).lower() + numberstring(numbers_one) + special_characters[char_special]
    else:
        password = generateword(word_one).lower() + " " + generateword(word_two).upper() + numberstring(numbers_one) + special_characters[char_special]

    return password

def gqpassword():
    numb_char = random.randint(2, 5)
    word_use = 10 - numb_char
    password = generateword(word_use).upper() + numberstring(numb_char)
    return password

state = True
while state == True:
    test = input("Test command: ")
    if test == "":
        print(windowspassword())
    elif test.lower() == "gq":
        print(gqpassword())
    else:
        state = False



        
