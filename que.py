s=input()
leter_flag1 = False
numer_flag2 = False
for l in s:
  if l.isalpha():
      leter_flag1 = True
  if l.isdigit():
      numer_flag2 = True
if leter_flag1 and numer_flag2:
      print('Yes')
else:
  print('No')
