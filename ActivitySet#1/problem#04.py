hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour: ")
r = float(rate)
if h > 40 :
    x = h - 40
    h = 40
    b = r * 1.50
    m = h * r
    n = x * b
    print(m + n)

else:
    print(h*r)