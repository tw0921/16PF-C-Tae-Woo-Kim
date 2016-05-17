# -*-coding:utf8
# 참고문헌 : http://learnpythonthehardway.org/book/ex33.html
#ex27 ~ 33까지 중요한 부분
i = 0
numbers = []

while i < 6: #32에서 for 문은 리스트에 좌우됐지만 whil은 조건식 즉 조건식에 의해 좌우된다
    print "At the top i is %d" % i # while이 참이면 밑에 무조건 실행 하지만 11번행이 없으면 무한으로 처리
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num