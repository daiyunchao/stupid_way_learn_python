#coding=utf-8
# 列表的操作

# create a mapping of state to abbreviation
states={
  'Oregon':'OR',
  'Flirida':'FL',
  'California':'CA',
  'New York':'NY',
  'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities={
  'CA':'San Francisco',
  'MI':'Detroit',
  'FL':'Jacksonville'
}

# add some more cities
cities['NY']='New Yourk'
cities['OR']='Portland'

#pring out some cities
print '-'*10
print 'NY State has: ',cities['NY']
print 'OR State has: ', cities['OR']

# print some states
print '-'*10
print "Michigan's  abbreviation is: ",states['Michigan']
print "Florida's a abbreviation is: ",states['Flirida']

# do it by using the state then cities dict
print '-'*10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states["Flirida"]]

# print every state abbreviation
print '-'*10
for state,abbrev in states.items():
  print "%s is abbreviated %s" %(state,abbrev)

# print every city in state
print '-'*10
for state,abbrev in cities.items():
  print "%s state is abbreviated %s and has city %s" %(
    state,abbrev,cities.get(state,'')
  )
print '-'*10
# safely get a abbreviation by state that might not be there
state=states.get('Texas',None)

if not state:
  print "Sorry, no Texas."

#get a city with a default value
city=cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s" %city 

# 字典的声明 variable ={key:value}
# 也可以像JS一样在声明外赋值 variable[key]=value
# 获取字典中的值的方法 variable=dic[key]
# 也可以像JS一样 嵌套使用 cities[states['Michigan']]
# for key,value in dic 一次将key和value 都获取出来
# 这种特点和 js中Map的 for of 类似
# 可以获取dic的时候,如果找不到指定的key指定一个默认值
# dic.get(key,default_val)