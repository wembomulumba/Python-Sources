#lambada express 
#combine the first and lastname

def build_quadratic_function(a, b, c):
    return lambda x: a*x*2 + b*x + c
f = build_quadratic_function(2,3,-5)

print(f(2))
#useful demonstration
sp1 = build_quadratic_function(3,0,1)(2)

print(sp1)
