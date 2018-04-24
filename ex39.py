# /usr/bin/python
# _*_coding:UTF-8_*_
#################### Dictionary lovely dictionary   #####################
#Create a mapping of state to abbreviation(缩写词)
states ={
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
}                                                           #定义字典：州名的缩写。键：全拼；值：缩写
#Create a basic set of states and some cities in them
cities = {
        'CA':'San francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
}                                                            #定义字典：缩写的城市名。键：缩写；值：全拼

# add some more cities                                       #添加字典cities内容。添加2个键，2个城市全拼
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 30)                                              #打印30个"-"，下同
print("NY State has:",cities['NY'])
print("OR state has :",cities['OR'])

#print some states
print('-' * 30)
print("Michigan's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is :",states['Florida'])

#do it by using the state then cities dict
print('-' * 30)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbreviation
print('-' * 30)
for state,abbrev in states.items():
        print("%s is abbreviated %s" % (state,abbrev))

#print every city in state
print('-' * 30)
for abbrev,city in cities.items():
        print("%s has the city %s" % (abbrev,city))

#now do both at the same time
print('-' * 30)
for state,abbrev in states.items():
        print(" %s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev]))

print('-' * 30)
#safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
        print("Sorry,no Texas.")

#get a city with a default value
city = cities.get('Tx','Does Not Exist')
print("The city for the state 'TX' is : %s " % city)

