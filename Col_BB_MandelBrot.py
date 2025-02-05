import mcpi.minecraft as minecraft
from ColorBlock import *
import math
import time

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

x0 =-2
x1 = 1.5
y0 = -1.5
y1 = 1.5

d = 0.015
c =0
#-0.8-0.156j
w = round((x1-x0)/d)
h = round((y1-y0)/d)

time.sleep(1)
Heigh = 1
print("Запуск")
for x in range(w):
    for y in range(h):
        z = complex(x0+x*d, y0+y*d)
        #Heigh = (abs(z)/2) * 10
        c=z
        phi = round(255*abs(math.atan2(c.imag, c.real))/math.pi)

        color =ChooseColor(phi)
        for H in range(255):
            if abs(z)>2:
                #Heigh = math.sin(H*math.pi/(2*255))*5
                #min((abs(z)/2), 20)
                color = ChooseColor(H)
                break

            z = z*z+c

        craft.setBlock(cor.x+x, cor.y+y, cor.z, color)

