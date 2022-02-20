from random import random
#Code previously shown and explained by Professor Brewer on caesar cipher.
def shiftLetter(char,shift):
    #Get ASCII number for character 
    ascii = ord(char)
    #Shift and unshift by 65 so A = 0 and Z = 25
    if (ascii >= 65) and (ascii <= 90):
        shifted = (ascii - 65 + shift) % 26 + 65 

    #if the ASCII code is lowercase letter, 
    #shift and unshift by 97 so a = 0 and z = 25
    elif (ascii >= 97) and (ascii <=122):
        shifted = (ascii - 97 + shift) % 26 + 97
    
    #if the ASCII code isnt a letter, dont shift it at all.
    else:
        shifted = ascii 
    
    #return the shifted ASCII code as a character
    return chr(shifted)

#Functions that will assign an index to each letter making exceptions with punctuations and blank spaces.
#Iterates over index of message given to the program.
def encrypts(message,pad):
    index_message = []
    index = 0 
    for i in range(0,len(message)):
        ascii = ord(message[i])
        if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <=122)):
            letter = shiftLetter(message[i],ord(pad[index])-65) #converts letter  to ASCII number.
            index_message.append(letter)
            index += 1
        else:
            letter = message[i]
            index_message.append(letter)
            
    return "".join(index_message) #adds letter to empty list

#Function that will take the message encyrpted and decode it, once again using the index created but this time going backwards.
def decrypts(message,pad):
    index_message = []
    index = 0 
    for i in range(0,len(message)):
        ascii = ord(message[i])
        if ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <=122)):
            letter = shiftLetter(message[i],-(ord(pad[index])-65))
            index_message.append(letter)
            index += 1
        else:
            letter = message[i]
            index_message.append(letter)

    return "".join(index_message)


#Random uppercase letter generator
def randomUpper():
    return chr(65 + int(26*random()))

#one time pad random generator using len in order to specify length
def generatePad(len):
    pad = []
    for i in range(0,len):
        pad.append(randomUpper())
    return "".join(pad)

#creates a file using previous random pad generated.
def generatePadFile(file,len):
    pad = generatePad(len)
    file = open(file, "w")
    file.write(pad)
    file.close()


#function that will decipher a message using the one time pad produced and stored earlier
def decipher(message,padfile):
    f = open(padfile)
    pad = f.read()
    return decrypts(message,pad)

#function that enciphers a message using a one time pad produced and stored earlier
def encipher(message,padfile):
    f = open(padfile)
    pad = f.read()
    return encrypts(message,pad)

#Test using txt files provided on moodle and using message within message.txt file to encrypt and generate a one time pad.
#Reads the file with the encrypted message
with open("encrypted-message.txt") as file:
    text = file.read()
print(decipher(text,"pad.txt"))

#Reads other message within message.txt file.
with open("message.txt") as file:
    tocipher = file.read()
print(encipher(tocipher, "pad.txt"))


# Citations: 
# -https://www.geeksforgeeks.org/with-statement-in-python/
# -https://www.journaldev.com/22767/python-ord-chr
# -https://www.learnpythonwithrune.org/understand-the-security-of-one-time-pad-and-how-to-implement-it-in-python/
# -Code previously shown by Professor Brewer on caesar cipher.
# Work with:
# -TAs: Waka, Yanning, Allison.





