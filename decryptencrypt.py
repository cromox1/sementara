__author__ = 'cromox'
"""
$ python3 decryptencrypt.py
Your sentences: Test Encrypt Sentence 2468 to 3690 or aything
Word shift: testword
Encrypt/Decrypt: Encrypt

Kjik Jbnhyfk Ijbkjbnj 8765 kc 3690 ch pyktebw

$ python3 decryptencrypt.py
Your sentences: Kjik Jbnhyfk Ijbkjbnj 8765 kc 3690 ch pyktebw
Word shift: testword
Encrypt/Decrypt: Decrypt

Test Encrypt Sentence 2468 to 3690 or aything
$
"""
ayattotest = input('Your sentences: ')
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
        ayattwo = processtukar(charone, chartwo, ayatone)
    else:
        ayatone = processtukar(chartwo, charone, sentence)
        ayattwo = processtukar(chartwo, charone, ayatone)
    return ayattwo

print()
ayattukar = encryptdecrypt(whattodo, wordshift, ayattotest)
print(ayattukar)
