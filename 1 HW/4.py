# Input a letter of the alphabet: k
# k is a consonant.
Letter=input('Input a letter of the alphabet: ')
if ord(Letter)<=122 and ord(Letter)>=97: 
    if Letter not in ['a','e','y','u','i','o']:
        print (f'{Letter} is a consonant')
    else: print(f'{Letter} is a vowel')
else: print ('your input is not small char')