import textwrap;
import random;

wordstring ="Frosting Moon light fills my bed. Lift my head seeing the moon. Drop my head missing my hometown";

words = wordstring.split( );


words = random.sample(words,len(words));


# nwordstring = " ".join(words[round(random.random())]) 
nwordstring = " ".join(words) 

print(textwrap.fill(nwordstring,30));