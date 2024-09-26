# Lambda Expression


def triple_me(num):
    return num*3
o = triple_me(10)
print(o)



def triple_me(num):
    return num**3
o = triple_me(10)
print(o)


# we can use lambda and write the same code

o = lambda num:num**2
print(o(10))

def add(n):
    return n+10

o=lambda n:n+10
print(o(5))



def mul(a,b):
    return a*b



h=lambda a,b:a*b
print(h(3,2))
