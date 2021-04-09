import mcpi.minecraft as minecraft
import mcpi.block as block

import math


craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

for i in range (360):
       
    
    x=x+1*math.sin(3*((math.pi*i)/180)+ (math.pi)/3)
    z=z+1*math.sin(2*((math.pi*i)/180)+(math.pi)/2)
    craft.setBlock(x, y, z, 35, 4)  


