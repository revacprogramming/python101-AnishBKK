#loo.Iter_ex5.2
lar = 0 
sma = 9999
while True:
    num = input("Enter a number? ")
    if num == "done" :
     break
    else :
      try :
       num = int(num)
       if num > lar :
          lar = num
       if num < sma :
         sma = num
      except :
       print("invalid type")
print("Maximum", lar)
print("Minimum", sma)