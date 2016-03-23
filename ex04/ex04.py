#-*-coding:cp949
cars = 100 #자동차 100대
space_in_a_car = 4.0 #공간 안의 차의 대수 4대
drivers = 30 #운전자 30명
passengers = 90 #승객 90명
cars_not_driven = cars - drivers #운전자가 없는 차의 대수 = 자동차 - 운전자
cars_driven = drivers #운전가능한 차의 대수 = 운전자의 수
carpool_capacity = cars_driven * space_in_a_car #카풀가능한 수용량 = 운전자수 * 차 안의 자리
average_passengers_per_car = passengers / cars_driven #1대의 차량 당 평균 승객 = 승객 / 운전자


print "There are", cars, "cars available." #이용가능한 몇대의 차들이 있습니다. 출력
print "There are only", drivers, "drivers available." #오직 운전만 가능한 운전자가 몇명 있습니다. 출력
print "There will be", cars_not_driven, "empty cars today." #빈 차가 오늘 몇대 있을 것입니다. 출력
print "We can transport", carpool_capacity, "people today." #우리는 오늘 몇명의 사람들을 수송할 수 있습니다. 출력
print "We have", passengers, "to carpool today." #우리는 오늘 몇명의 사람들을 카풀 할 수 있습니다. 출력
print "We need to put about", average_passengers_per_car, "in each car." #각 차량 당 태워야할 평균 승객 출력