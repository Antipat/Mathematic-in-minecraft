import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

a=0.1

for i in range (2080):
    
    x = x +0.1*math.cos((math.pi*i)/180)
    z = z +0.1*math.sin((math.pi*i)/180)
    y=y+0.01
    craft.setBlock(x, y, z, 35,1)


