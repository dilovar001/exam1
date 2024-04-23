a=int(input())
cnt=0
for i in range(1,a+1):
  if a%i==0 :
    cnt+=1
    if cnt<=2:
     print("The entered number is a prime number.")
    elif cnt>2 : print("The entered number is a not prime number.")