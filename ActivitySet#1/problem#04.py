h = float(input("Enter Hours:"))
r = float(input("Enter Rate per hour: "))
if h > 40 :
    m = 40*r
    n = (h-40)*(r*1.50)
    print(m + n)
else: 
    print(h*r)