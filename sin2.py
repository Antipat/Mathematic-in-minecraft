import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z


for i in range(10):
    for i in range (720):
        craft.setBlock(x, y, z, 35,3)
        x=x+0.1
        y=y+0.5*math.sin((math.pi*i)/180)
    
    x = cor.x
    y = cor.y
    z=z+1


