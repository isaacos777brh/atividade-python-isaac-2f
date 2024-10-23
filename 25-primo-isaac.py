num = int(input('digite um numero: '))
prim = 0

for i in range(1, (num + 1)):        
  if num % i == 0:
    prim += 1
    
if prim  == 2 :
  print('é primo')
else:
  print('não é primo')