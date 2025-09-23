def my_add(a, b):
    return a + b
print(my_add(3, 7))

def get_vat(V):
    return V*0.1
print(get_vat(10000))

a=[10,20,30]
print(sum(a)/len(a))

def get_avg(number):
    return sum(number)/len(number)
print(get_avg([10,20,30]))

def solution(n):
    answer = [] 
    for i in range(1,n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer
print(solution(10))






