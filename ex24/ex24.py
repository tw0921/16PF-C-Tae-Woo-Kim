# -*-coding:utf8
#-*-coding:cp949
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print poem
print("--------------")


five = 10 - 2 + 3 - 6  #five라는 변수에 저장
print("This should be five: %s" % five) #함수의 유효범위 위에 five 라는 변수와 만약 함수에도 five라는 변수가 있다.
# 이때 함수내에서만 five라는 변수가 따로 적용되고 밖에서는 위에 five가 적용

def secret_formula(started):   #secret formula 라는 함수를 호출
    jelly_beans = started * 500 #  함수안에 있는 변수들은 기본적으로 함수안에서만 사용할수 있다.
    jars = jelly_beans / 1000 # 함수는 계산 도중 따로 공간을 만들어 복잡한 계산만 할수있도록 해준다.
    crates = jars / 100
    return jelly_beans, jars, crates #retunrn 을 통해 결과값을 밖으로 내준다.


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
