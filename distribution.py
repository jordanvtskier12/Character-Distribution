"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import re
import operator

#stripping input down to only lower case letters
badd=input("Please enter a string of text (the bigger the better): ")
badd1=(badd.lower())
badd2=re.sub('[^ a-zA-Z]', '', badd1)
badd3=badd2.replace(" ", "")


letlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters={c:0 for c in letlist}

#put amount of each letter into a dictionary
for i in badd3:
    letters[i]+=1


#turn dictionary into a list so it can be sorted
let = sorted(letters.items(), key=operator.itemgetter(1),reverse=True)


#turn the sorted list back into a dictionary
d = dict(let)

print('The distribution of characters in "'+badd+'" is: ')

for key, value in d.items() :
    if value>0:
        print(key * value)
        

