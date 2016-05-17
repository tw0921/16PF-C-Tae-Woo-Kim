# -*-coding:utf8
# 참고문헌 : http://learnpythonthehardway.org/book/ex32.html
#for 문을 사용할려면 배열을 넣고 받아주는 변수를 넣으면 된다

the_count = [1, 2, 3, 4, 5] #숫자와 문자 섞어써도 상관없고 리스트 안에 리스트를 만들 수 있다.
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:  #for 문은 코드에 있는것을 여러번 실행할 수 있다.
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# 또는 python 에서는 아래와 같이 할 수도 있다.
# list comprehension
elements2 = [i for i in range(0, 6)] #range 는 정수로 된 등차수열을 의미

# now we can print them out too
for i in elements:
    print "Element was: %d" % i