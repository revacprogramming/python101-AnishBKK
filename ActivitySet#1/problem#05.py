# Functions
def computepay(h,r):
    if h > 40 :
        p1 = 40 * r
        r = r * 1.5
        h1 = h - 40
        p2 = r * h1
        p=p1 + p2
    return p

hrs = float(input("Enter Hours:"))
rate= float(input("Enter rate:"))
p = computepay(hrs,rate)
print("Pay",p)