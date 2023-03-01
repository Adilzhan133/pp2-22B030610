import re
txt = input()


#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
x = re.search('ab*', txt )

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
x = re.search("ab{2,3}", txt )

#Write a Python program to find sequences of lowercase letters joined with a underscore.
x = re.findall("[a-z]+_[a-z]+", txt )

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
x = re.findall("[A-Z]_[a-z]+", txt )

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
x = re.search("a.*?b$", txt )

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
x = re.sub("[ ,.]", ":", txt)

#Write a python program to convert snake case string to camel case string.
m = txt.split('_')
text = ''
for i in range(len(m)):
    x = m[i].capitalize()
    text += x

#Write a Python program to split a string at uppercase letters.
x = re.findall('[A-Z][^A-Z]*', txt)

#Write a Python program to insert spaces between words starting with capital letters.
x = re.findall('[A-Z][^A-Z]*', txt)
text = ' '.join(x)

#Write a Python program to convert a given camel case string to snake case.
m = re.findall('[A-Z][^A-Z]*', txt)
for i in range(len(m)):
    m[i] = m[i].lower()

text = '_'.join(m)