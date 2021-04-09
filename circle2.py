import mcpi.minecraft as minecraft
import mcpi.block as block

import math


craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z
k=20

for i in range (-20,20):
    for j in range (-20, 20):
        if math.pow(i,2)+math.pow(j,2)<=math.pow(k,2):
            craft.setBlock(x+i, y, z+j, 35,2)
    
    
    




