import mcpi.minecraft as minecraft
import mcpi.block as block
import ColorBlock
import math
import time
import random

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()


x1=random.uniform(0,50)
y1=random.uniform(0,50)
z1=random.uniform(0,50)

time.sleep(5)
k = 50
print("Запуск")

def Apo(r, X0, Y0, Z0):
    global x1,y1,z1
    
    X = x1 - X0
    Y = y1 - Y0
    Z = z1 - Z0
    r2 = r*r
    dist = X*X + Y*Y + Z*Z + 1E-30;

    x1=  (r2 * X / dist + X0);
    y1=  (r2 * Y / dist + Y0);
    z1=  (r2 * Z / dist + Z0);
    
for i in range (100000): 
    n = random.randint(1,4)	

    if n==1:
        Apo(2.71869, 2.82842, 0, -1)	
        color=ColorBlock.MaterialColor(3,4)
    elif n==2:
        Apo(2.71869, -1.41421, 2.44949, -1)
        color=ColorBlock.MaterialColor(6,1)
    elif n==3:
        Apo(2.71869, -1.41421, -2.44949, -1)
        color=ColorBlock.MaterialColor(9,1)
    elif n==4 :
        Apo(2.71869, 0, 0, 3)
        color=ColorBlock.MaterialColor(12,3)
	
    if i>20 :
        craft.setBlock(cor.x+x1*k, cor.y+y1*k, cor.z+z1*k, color)
    time.sleep(0.0002)


print("Конец")

