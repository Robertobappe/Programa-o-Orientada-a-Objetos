a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = (b**2)-(4*a*c)

if delta > 0 and a != 0:
    R1 = (-b + (delta)**(1/2))/(2*a)
    R2 = (-b - (delta)**(1/2))/(2*a)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)

elif delta == 0 and a != 0:
    R = delta/2
    print("R = %.5f" % R)

else:
    if delta < 0 or a == 0:
        print('Impossível calcular')
