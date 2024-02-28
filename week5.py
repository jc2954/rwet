import random;
import textwrap;
import tracery;

from tracery.modifiers import base_english


f = open("read.txt").read()
readout = f.split("\n")

dontwant= ['the ','The ','a ', ',' ,'when ','as ', 'what ','when ', 'and ', 'by ']

rtaa = {}
ct =0;
for x in readout:
    if x!='':
        for i in dontwant:
           x = x.replace(i,'')
        print(x)
        ct = x.count(" ")
        cname = str(ct)
        if cname in rtaa:
         rtaa[cname].insert(0,x)
        else:
            rtaa[cname]=[x] 
           


listbyorder = sorted(rtaa)
print(rtaa['7'])

rules = {
    'origin': 'Haiku for Feb 12\n#firstline#\n#secondline#\n#thirdline#',
    'firstline': rtaa["6"],
    'secondline':rtaa["7"],
    'thirdline':rtaa["5"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#origin#"))