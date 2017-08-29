#coding=utf-8
s1=72
s2=85
r=(s2-s1)/s1*100
print('小明成绩提升%.1f%%' % r)

L=L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

height=1.75
weight=80.5
bmi=weight/(height*height)
if bmi<18.5:
    print('过轻')
elif (bmi>=18.5)and(bmi<=25):
    print('正常')
else:
    print('超重')

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)

i=0
while i<3:
    print(L[i])
    i=i+1

n1=255
n2=10000
print('n1 = %s,n2 = %s' % (hex(n1),hex(n2)))

def quadratic(a,b,c):
    pass



L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1)
L2 = [x for x in L1 if (isinstance(x,str)==True)]
print(L2)


def now():
    print('2017-08-25')

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s' % func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print('hello')

now()
