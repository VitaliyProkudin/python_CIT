import sys

nun_steps = int(sys.argv[1])


for x in range(nun_steps): 
      for i in range((nun_steps)-x):
         print(' ',end='')
      for y in range((x)+1):
         print('#',end='')
      print(end='\n')
    


