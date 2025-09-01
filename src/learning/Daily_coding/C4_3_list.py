students = ["egoing", "sori", "maru"]
grades = [2,1,4]
print("students[1]", students[1])
print("len(students)", len(students))
print("min(grades)", min(grades))
print("max(grades)", max(grades))
print("sum(grades)", sum(grades))

#평균값
import statistics
print("statistics.mean(grades)", statistics.mean(grades))

#랜덤 선택
import random
print("random.choice(students)", random.choice(students))