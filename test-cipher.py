from cipher import*

#Testing shift letter function giving 3 as the shift number which will encode the letter based on the ASCII code system.
def test_shiftLetterby3():
    assert shiftLetter("a",3) == "d"
    
#Testing shift letter by 0, which should output the same letter inserted since 0 will not make any shift changes. 
def test_shiftLetterby0():
    assert shiftLetter("b",0) == "b"

#Function should get a word/message to encrypt and use the random uppercase pad generated to encrypt it and viceversa for the decryption function. 
#For this test I used the example given on the caesar cesar one time pad example. 

def test_encrypts():
    assert encrypts("Rally", "QWERT") == "Hwpcr"
    #Edge case: The program should be able to skip all blank spaces and punctuation signs that are not lowercase or uppercase letters.
def test_encryptspunctuation():
    assert encrypts("!@*!,","") == "!@*!,"

def test_decrypts():
    assert decrypts("Hwpcr","QWERT") == "Rally"
def test_decrypts_punctuation():
    assert decrypts("!@*!,", "") == "!@*!,"


#Since the generatePad() function takes the length of the message and counts how many characters it has to make a pad that has the same numbers of letters as the message,
#the the output of the function should be the same number of characters as the number of characters of the length. 
def test_generatePadlen():
    assert len(generatePad(5)) == 5 
    assert len(generatePad(0)) == 0

#Tests that each pad that is generated gives a unique random pad.
def test_generatePadunique():
    assert generatePad(150) != generatePad(150)

