#1x**2+2x+3=0
import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
desc = ((b**2) - 4*a*c)
if desc < 0:
    print("D<0 Корней нет - введите другие аргументы")
elif desc == 0:
        squar = -(b/2*a)
        print('D=0 2 корня x1=', squar,'x2=', -squar)
else:
        squar_1  = -b+math.sqrt((b**2) - 4*a*c)/2*a
        squar_2 = -b-math.sqrt((b**2) - 4*a*c)/2*a
        print('D>0 c округлением  x1=', round(squar_1),'x2=', round(-squar_2))