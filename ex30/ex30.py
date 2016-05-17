# -*-coding:utf8
# 참고문헌 : http://learnpythonthehardway.org/book/ex30.html

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the truchks.")
else:
    print("Fine, let's stay home then.")
# branch : 새로운 기능을 만들면 성공할지 안할지 몰라서 branch를 만들어 만든후 성공하면 merge를 한다
