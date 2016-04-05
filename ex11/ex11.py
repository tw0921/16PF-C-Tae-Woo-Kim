#-*-coding:cp949
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (
    age, height, weight) #raw_input은 숫자도 문자로 인식 %r은 변환으로 밑에 출력에 따옴표
