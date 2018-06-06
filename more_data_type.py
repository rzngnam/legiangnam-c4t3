a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
delta = b ** 2 - 4*a*c

if a == 0:
    x3 = -c/b
    print("pt co 1 nghiem la",x3)

if delta < 0:
    print("Pt vo nghiem")

elif delta == 0:
        print("Pt co nghiem kep")
        x = (-b)/2*a
        print("nghiem la",x)

else:
        print("pt co 2 nghiem phan biet")
        x1 = (b-delta**0.5)/2*a
        x2 = (b+delta**0.5)/2*a
        print("nghiem la x1 = {0}, x2 = {1}".format(x1,x2))

