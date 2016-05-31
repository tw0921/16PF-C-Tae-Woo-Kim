#-coding:utf8
# 참고문헌 : http://learnpythonthehardway.org/book/ex39.html

import hashmap

# oreate a mapping for states to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Hawaii', 'HI')

#oreate a basio set of states and  some oities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Los Angeles')
hashmap.set(cities, 'Hi', 'Honolulu')
hashmap.set(cities, 'FL', 'Orlando')

# add some more oities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some oities
print('-' * 10)
print("NY State has: %s" % hashmap.get(cities, 'NY'))
print("Hi State has: %s" % hashmap.get(cities, "HI"))

# print some states
print('-' * 10)
print("Hawaii`s abbreviation is: %s" % hashmap.get(states, 'Hawaii'))
print("Florida`s abbreviation is: %s" % hashmap.get(states, 'Florida'))

# do it by using the state then cities dict.
print('-' * 10)
print('Hawaii has: %s' % hashmap.get(cities, hashmap.get(states, 'Hawaii')))
print('Florida has : %s' % hashmap.get(cities, hashmap.get(states, 'Florida')))

# print every state abbreviaiton
print('-' * 10)
hashmap.list(states)

# print every city in state
print('-' * 10)
hashmap.list(cities)

print('-' * 10)
state = hashmap.get(states, 'Texas')

if not state:
    print("Sorry, no Texas")

# default values using II = with the nill result
# can you do this one line?
city = hashmap.get(cities,'TX', 'Not Entered Yet')
print("The city forthestate 'TX' is: %s" % city)