# How this should worck:
# 1) user enters a world/letter/sentence
# 2) programm tranclates whith a dic
# 3) print result abcdefghijklmnopqrstuvwxyz


import random

def coder(phrase, use_key):
    phrase = phrase.lower()
    letters_in_alphabet = "abcdefghijklmnopqrstuvwxyz"
    mass2 = list(letters_in_alphabet)
    if use_key == 0:
        
        mass = list(letters_in_alphabet)
        random.shuffle(mass)
    
    else: 
        mass = list(use_key)
    

    mass3 = list(phrase)
    print( ''.join(mass))
    
    out_put = ''
    for i in mass3:
        
        if i in ' ':
            out_put += '26 '
            
        else:
            out_put += str(mass2.index(i)) + ' '
    
    out_put = out_put.split()
    print(out_put)
    coded = ''
    for i in out_put:
        if int(i) == 26:
            coded += ' '
        else: 
            coded += mass[int(i)]
    print(coded)
    regim()
    
    
def decoder(phrase, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    phrase = phrase.lower()
    phrase  = list(phrase)
    key = list(key)
    out_put = ''
    for i in phrase:
        if i == ' ':
            out_put += '26 ' 
        else: 
            out_put += str(key.index(i)) + ' '       
        
    out_put = out_put.split()
    print(out_put)
    message = ''
    for i in out_put:
        if int(i) == 26:
            message += ' '
        else:
            message += alphabet[int(i)]
    print(message)
def regim():
    
    set_regim = int(input('Please tell, what you would like to do.\n[1 - cod meassege / 2 - decod measege]: '))
    if set_regim == 1:     
        key = int(input('Do u have a secret key?\n[1 - yes / 0 - no]: '))
        if key == 1:
            sel_key = input('Enter key: ')
        else:
            sel_key = 0
        coder(input("Phrase to cod: "), sel_key)
    elif set_regim == 2:
        key = input('Eanter a seacrat key: ')
        phrase = input('phrase to translate: ')
        decoder(phrase, key)
        
print('Wellcome to chiper')
regim()