import random

def r(list_input):
    a = random.randint(0, len(list_input)-1)
    return list_input[a]

def longest(list_input):
    longest = "Tim"
    for i in list_input:
        if len(i) > len(longest):
            longest = i
    return longest

def mean(list_input):
    total = sum(list_input)
    mean = total/len(list_input)
    return mean

def name_settlement():
    name_1 = ["White", "Black", "Red", "Scar", "Row", "Barn", "Long"]
    name_2 = ["bridge", "borough", "stone", "port", "ford", "croft", "chester", "field"]
    return str(r(name_1)+r(name_2))
    
def settlement_make():
    #Whats in a name?
    name = name_settlement()

    #size is important, sorry!
    sizes = ["hamlet", "village", "small town", "large town", "city"]
    size = r(sizes)

    #we need something to be made here
    industry_rural = ["coal mines", "potato farms", "fishing trade", "lumber", "hunting", "ore mines", "orchards",
                      "local cider", "clay pits", "horse trainers"]
    industry_urban = ["smithing", "textile industry", "banks and commerce", "strong trade network", "woodcarving", "carpentry",
                      "shipwrights"]
    if size == sizes[0] or size == sizes[1]:
        industry = r(industry_rural)
    else:
        industry = r(industry_urban)

    #some flavour is needed
    descriptors = ["full of crime", "very clean", "very well organised", "on fire", "dealing with a plague", "welcoming to all",
                   "wealthy", "poor", "very dangerous", "a safe haven for all"]
    descriptor = r(descriptors)

    #we know someone's going to be in charge
    leadership= ["a Sheriff", "a Baron", "a Mayor", "a Lord", "an Elected Council", "a Senate", "an Earl"]
    royal = ["the King", "the Queen"]
    kingqueen = r(royal)
    if size == sizes[(len(sizes)-1)]:
       leadership.append(kingqueen)
    ruler = r(leadership)

    qualities = ["cruel", "corrupt", "kind", "merciful", "undecisive", "rich", "a scoundrel"]
    quality = r(qualities)
       
    return (str(name)+", a "+str(size)+" known for its "+str(industry)+" said to be "+descriptor+". Ruled by "+str(ruler)+" who is "+quality+".")

def weather_get():
    weathers = ["It is raining.", "Birds sing.", "Lightning splits the sky.", "The wind picks up.", "The sun beats down.", "It begins to snow.",
                "Hail pelts down."]
    return r(weathers)

def location_make():
    loc_type = ["cave", "mine", "campsite", "grove", "ruins", "crag", "glacier", "glade", "beach", "marsh", "church", "manor"]
   
n = 1
messages = []

while n < 500:
    settlement = settlement_make()
    weather = weather_get()

    a = random.randint(1, 10)    
    if a < 7:
        message = (str(settlement))
    else:
        message = (str(settlement)+" "+str(weather))
    print(message)
    messages.append((message))
    n += 1

print(str(n)+" generated.")

lengths = [len(i) for i in messages]

print("Mean length: "+str(mean(lengths)))
print("Longest length: "+str(len(longest(messages))))
