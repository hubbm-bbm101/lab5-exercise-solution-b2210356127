N = int(input("give me a number please: "))
result1 = 0
result2 = 0
if N%2==0:
  for i in range (0,N+1,2):
    result1 = result1 + i
  print((result1)/(N/2))
else:
  for i in range (1,N+1,2):
    result2 = result2 + i
  print(result2)

