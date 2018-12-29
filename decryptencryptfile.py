__author__ = 'cromox'
"""
$ python3 decryptencryptfile.py
Your Input File: testGC.py
Your Output File: testGCrosli3.py
Word shift: abcefg
Encrypt/Decrypt: e

$
"""
fileinput = input('Your Input File: ')
fileoutput = input('Your Output File: ')
wordshift = input('Word shift: ')
whattodo = input('Encrypt/Decrypt: ')

def processshift(wordshift):
    import string

    original_chars = string.ascii_uppercase
    wshift = wordshift.upper()
    wordshift = ''
    for i in range(len(wshift)):
        for j in range(len(wshift)):
            if i != j:
                if wshift[j] != wshift[i]:
                    if wshift[i] not in wordshift:
                        wordshift = wordshift + wshift[i]

    numswift = len(wordshift)
    shift_chars = wordshift
    for i in range(numswift, len(original_chars) + numswift):
        if original_chars[i - numswift] not in shift_chars:
            shift_chars = shift_chars + original_chars[i - numswift]

    original_chars = original_chars + original_chars.lower() + string.digits
    k = len(wshift)%9
    newstringdigit = string.digits[k::-1][::-2] + string.digits[k:0:-1][::-2] + string.digits[:k:-1][::-2] + string.digits[:k+1:-1][::-2]
    shift_chars = shift_chars + shift_chars.lower() + newstringdigit

    return original_chars, shift_chars

def processtukar(firstchars, secondchars, sentence):
    sentencetwo = ''
    for i in range(len(sentence)):
        mychar = firstchars.find(sentence[i])
        if mychar >= 0:
            sentencetwo = sentencetwo + sentence[i].replace(firstchars[mychar], secondchars[mychar])
        else:
            sentencetwo = sentencetwo + sentence[i]
    return sentencetwo

def encryptdecrypt(ccrypt, wordshift, sentence):
    tukaran = processshift(wordshift)
    charone = tukaran[0]
    chartwo = tukaran[1]

    if ccrypt == 'e' or ccrypt == 'encrypt' or ccrypt == 'E' or ccrypt == 'Encrypt':
        ayatone = processtukar(charone, chartwo, sentence)
        return processtukar(charone, chartwo, ayatone)
    else:
        ayatone = processtukar(chartwo, charone, sentence)
        return processtukar(chartwo, charone, ayatone)

with open(fileinput) as filein:
    open(fileoutput, 'w')
    for line in filein:
        linetukar = encryptdecrypt(whattodo, wordshift, line)
        print(linetukar, end='', file=open(fileoutput, 'a'))
