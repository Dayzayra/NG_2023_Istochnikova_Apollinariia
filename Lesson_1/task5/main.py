print("Given equation of the species ax^2+bx+c=0. Enter the values a,b,c.")
a=int(input ("a = "))
b=int(input ("b = "))
c=int(input ("c = "))
d= pow(b,2)-(4*a*c)
if(d>0):
    x1=(-b-pow(d,0.5))/(2*a),
    x2=(-b+pow(d,0.5))/(2*a),
    print("Roots of the equation: x1=",x1,"\n", "x2=",x2)
elif(d==0):
    x=-b/(2*a),
    print("Root of the equation: Х=",x)
else:
    x1= (-b-pow(abs(d),0.5)*1j)/(2*a),
    x2= (-b+pow(abs(d),0.5)*1j)/(2*a),
    print("Roots of the equation: x1=",x1,"\n", "x2=",x2)
