import random, textwrap
import sys
lines = \
[["\nPeople also ask/why is Harriet Tubman/important/to the world", "1/4", "2/3", "1"],\
#References google search terms
["\nin each pound of dollar bills/", "1/2", "3/4", "1"],\
#According to cotton.org
["\n\tthe dollar/hasn't/changed", "3/4", "1/2", "1"],\
["\n\tin no rush/the first quail calls", "1/3", "2/3", "1"],\
["\n\tto put Tubman/on the $20/bill", "2/4", "3/4", "1"], \
#According to a CNN Money article from ‘16
["\nour Moses/never lost a passenger/", "1/4", "2/4", "2"],\
#So it’s been said about Harriet Tubman’s track record
["\n\tJesus is/a friend with friends", "1/4", "2/4", "2"],\
["\nI just wanted the world/to see", "2/3", "2/3", "2"],\
#Spoken by Mamie Till as to why she wanted Emmett’s
#coffin open.
["\n\tSlave patrol/also called/patterrollers/pattyrollers/paddy rollers/patrollers/", "3/4", "1/3", "2"],\
#According to wikipedia
["\nshe said/a friend of a friend/of a friend/sent me", "3/4", "1/2", "2"],\
#According to https://tinyurl.com/yddx6qaj
["\n\tdrove toward Money, Mississippi/$$$$$$", "1/2", "1/2", "3"],\
#According to Wikipedia, Emmett Till’s abductors drove him
#toward the town of Money, Mississippi
["\n\tPeople also ask \twhat is Harriet Tubman/most/most famous for", "2/3", "3/4", "3"],\
["\nPeople also ask/what was Harriet Tubman's/life like?", "1/2", "2/3", "3"],\
["\n\tTreasure secretary/just like Jesus/we won't stay dead", "2/3", "1/4", "3"]]
#code adapted for Python3
#code from github and translated from the Italian
#is a reconstruction of the method thought to have been used
#for Nanni Balestrini’s electronic poem Tape Mark 1, 1962
# https://github.com/fanfani/TAPE-MARK-1
random.shuffle(lines)
stanza_one = [None] * 10
stanza_one[0] = lines[0]
lines.remove(stanza_one[0])

try:
    i = 1 ; j = 0
    while j < 9:
        if (lines[i][1][0] == stanza_one[j][2][0] \
        or lines[i][1][2] == stanza_one[j][2][0] \
        or lines[i][1][2] == stanza_one[j][2][2]) \
        and lines[i][3] != stanza_one[j][3]:
            stanza_one[j+1] = lines[i]
            lines.remove(lines[i])
            i = 0
            j += 1
        #otherwise examine the next item
        else:
            i += 2
            continue
except: sys.exit()
#Wikipedia was consulted for information about
#Mamie and Emmett Till, Harriet Tubman,
#the rock that struck Harriet Tubman in the head,
#and slave patrols.
#’To holler down the lions’ comes from
#’gay chaps at the bar’ by Gwendolyn Brooks
stanza = []
for line in stanza_one:
                stanza.append(line[0])
s = '/'.join(stanza).split("/")
print ("")
for k in range(len(s)):
                if k == (len(s) - 1): sys.stdout.write(s[k].lower())
                else: sys.stdout.write(s[k].lower() + " ")
                # if k > 0 and (k+1)%4 == 0: print ""
print ("")

