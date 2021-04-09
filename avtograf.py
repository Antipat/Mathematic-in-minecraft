import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time
craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z
for i in range (720):
       
    x=x+0.1
    y=y+0.5*math.cos((math.pi*i)/180) #y =y + f(i)
    craft.setBlock(x, y, z, 35, 7)
    
    x1=x
    y1=y
    
    time.sleep(0.5)
    
    craft.setBlock(x1, y1, z, 0)
    


