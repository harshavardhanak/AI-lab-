import cmath
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
root1 = (-b + cmath.sqrt(b*b-4*a*c)/(2 * a ))
root2 = (-b - cmath.sqrt(b*b-4*a*c)/(2 * a ))   
print("The roots of quadratic equation are {} and {} ".format(root1,root2))

# import cmath for complex square roots 1