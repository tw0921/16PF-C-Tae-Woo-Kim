#-*-coding:cp949
cars = 100 #�ڵ��� 100��
space_in_a_car = 4.0 #���� ���� ���� ��� 4��
drivers = 30 #������ 30��
passengers = 90 #�°� 90��
cars_not_driven = cars - drivers #�����ڰ� ���� ���� ��� = �ڵ��� - ������
cars_driven = drivers #���������� ���� ��� = �������� ��
carpool_capacity = cars_driven * space_in_a_car #īǮ������ ���뷮 = �����ڼ� * �� ���� �ڸ�
average_passengers_per_car = passengers / cars_driven #1���� ���� �� ��� �°� = �°� / ������


print "There are", cars, "cars available." #�̿밡���� ����� ������ �ֽ��ϴ�. ���
print "There are only", drivers, "drivers available." #���� ������ ������ �����ڰ� ��� �ֽ��ϴ�. ���
print "There will be", cars_not_driven, "empty cars today." #�� ���� ���� ��� ���� ���Դϴ�. ���
print "We can transport", carpool_capacity, "people today." #�츮�� ���� ����� ������� ������ �� �ֽ��ϴ�. ���
print "We have", passengers, "to carpool today." #�츮�� ���� ����� ������� īǮ �� �� �ֽ��ϴ�. ���
print "We need to put about", average_passengers_per_car, "in each car." #�� ���� �� �¿����� ��� �°� ���