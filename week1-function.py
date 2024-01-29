import random;

above = ['brow','mist','shape','layer','the crag','stone','forest','height']
below = ['flow','basin','shape','vein','rippling','stone','cove','rock']
transitive = ['command','pace','roam','trail','frame', 'sweep','exercise','range']
imperative = ['track','shade','translate','stamp','progress through','direct','run','enter']
intransitive = ['linger','dwell','rest','relax','hold','dream','hum']
texture = ['rough','fine']
adjectives = ['encomassing','sinuous','straight','objective','arched','cool','clear','dim','driven']

def path():
    plural = random.sample(['s',''],k=2)
    words = random.choice(above)
    if words == 'forest' and random.randrange(4)==0:
      words = "monkeys" + " " + random.choice(transitive)
    else:
        words += plural[0] + " "  + random.choice(transitive) + plural[1]

    words += " the " + random.choice(below) + random.choice(['s','']) + "."  
    return words.capitalize();

stance_count=10

for i in range(stance_count):
    nt = path()    
    print(nt)