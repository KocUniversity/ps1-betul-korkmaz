n, B = list(map(int, input().strip().split()))
T = 0

# your code here
Tmin =0
Tmax =10000

tp = 0

for index in range(n):
  i = index+1
  tn = n-i
  if i%2 == 0:
    pi = 2**i + 1
  else:
    pi = 3**i + 1

  pi = pi**tn 
  tp = tp + pi

exit = 0

while exit == 0:
  T = int((Tmin+Tmax)/2)

  if (tp*T > B):
    if (tp*(T-1) < B):
      exit = 1
    else:
      if T == 10000:
        T = -1
        exit = 1
      Tmax = T
    
  else:
    if (tp*(T+1) > B):
      T = T+1
      exit = 1
    else:
      if T == 9999:
        T = -1
        exit = 1
      Tmin = T
   
if T > 10000:
  T = -1
    
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)