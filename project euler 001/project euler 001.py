# coding: utf-8
# 참고문헌 : http://euler.synap.co.kr/prob_detail.php?id=1

total_sum = 0
for i in range(1,10):
    if i % 3 == 0 or i % 5 == 0:
        total_sum = total_sum + i
print total_sum

total_sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        total_sum = total_sum + i
print total_sum
