from cipher import*

#Functions to test functions from cipher.py program.
def test_shiftLetterby3():
    assert shiftLetter("a",3) == "d"
    

def test_shiftLetterby0():
    assert shiftLetter("b",0) == "b"

#Function to test encryption from cipher.py program.
def test_encrypts():
    assert encrypts("R", "Q") == "H"
    assert encrypts("!@*!,","") == "!@*!,"

def test_decrypts():
    assert decrypts("Hwpcr","QWERT") == "Rally"
    assert decrypts("!@*!,", "") == "!@*!,"


#Confused on how to use random_Upper as an argument for generate pad function
def test_generatePad():
    assert len(generatePad(8)) == 8 
    assert len(generatePad(0)) == 0

