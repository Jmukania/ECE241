# Jordy Mukania
# ECE 241 Hw#1 solving monomials
# Aug 30, 2020

class solving_for_x:

    def monomial(a,b,c):                # Solves for ax-2b=c for x
        if a == 0:
            print("x is undefined, cannot divide by 0")
        else:
            x = (2*b+c)/a
            print('Solving for x in, '+str(a)+'*x - 2*'+str(b)+' = '+str(c)+'\nx =',x)

    def polynomial(a,b,c):              # Solves for sqrt(ax+2b)=c for x
        if a == 0:
            print("x is undefined, cannot divide by 0")
        else:
            x = (c**2 - 2*b)/a
            print('Solving for x in, sqrt('+ str(a) +'*x + 2*'+ str(b) +') = '+str(c)+'\nx =',x)


# User inputs
print('Please enter values a, b, and c to solve for x in: ax-2b = c')
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
solving_for_x.monomial(a,b,c)

print('Please enter values a, b, and c to solve for x in: sqrt(ax+2b) =c')
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
solving_for_x.polynomial(a,b,c)