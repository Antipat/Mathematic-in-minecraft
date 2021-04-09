import mcpi.minecraft as minecraft
import mcpi.block as block
import math


craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

k=0.1
for i in range (20):
    
    for j in range(360):
        y= y+k*math.sin((math.pi*j)/180)
        x = x+ k*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 57)
    k=k-0.005


