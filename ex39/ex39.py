#-coding:utf8
# 참고문헌 : http://learnpythonthehardway.org/book/ex39.html

# oreate a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Hawaii' : 'HI',
}

# oreate a basio set of states and some oities in them
cities = {
    'CA' : 'Los Angeles',
    'HI' : 'Honolulu',
    'FL' : 'Jacksonville',
}

# add some more oities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some oities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('Or State has: %s' % cities['OR'])

# print some states
print('-' * 10)
print("Hawaii`s abbreviation is: %s" % states['Hawaii'])
print("Florida`s abbreviation is: %s" % states['Florida'])

# print every state abbreviation
print('-' * 10)
print("states = %s" % states)
print("states.items() = %s" % str(states.items()))
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print avery city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]
    ))

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Not Entered Yet')
print("The city for the state 'TX' is: %s" % city)

# 입력 후 add. comit # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit
# 오류노트에 각자 오류노트 작성성