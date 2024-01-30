def sum(a,b):
    x=a+b
    return x

a=int(input('starting range:'))
b=int(input('end range:'))

t=sum(a,b)
print('The Sum of {} and {} is {}'.format(a,b,t))