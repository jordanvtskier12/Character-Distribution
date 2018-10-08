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
badd=input("enter string")
badd=(badd.lower())
#print(badd)
letlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bignumlist=[0]*26
#bignumlist[1]=1
newlist=['3a']*26
for i in range(len(bignumlist)):
    bignumlist[i]=badd.count(letlist[i])
    newlist[i]=str(bignumlist[i])+letlist[i]
    #print(bignumlist[i])
    #print(letlist[i])

newlist.sort(reverse=True)
print(newlist)

for i in range(len(bignumlist)):
    thelen=len(newlist[i])-1
    tempstring=newlist[i]
    thenum=tempstring[0:thelen]
    thelet=tempstring[thelen]
#temp=[thelet]*thenum
#print(temp)
    
    
#twoway=zip(letlist,bignumlist)
#from operator import itemgetter
#twoway.sort(reverse=True)
#twowayset=set(twoway)
#twowayset.sort(key=itemgetter(1), reverse=True)
#print(twowayset)
