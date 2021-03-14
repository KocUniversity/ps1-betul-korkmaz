n, B = list(map(int, input().strip().split()))
T = 0

# your code here
tp = 0

while tp < B and T <= 10000:
  T+=1
  tp = 0
  for index in range(n):
   i = index+1
   tn = n-i
   if i%2==0:
     pi = 2**i + 1
   else:
     pi = 3**i + 1

   pi = pi**tn 
   tp = tp + pi*T
  
if T > 10000:
 T = -1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)