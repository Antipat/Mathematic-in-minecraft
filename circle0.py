import mcpi.minecraft as minecraft
import mcpi.block as block
import math


craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z


for j in range(360):
    z = z+0.2*math.sin((math.pi*j)/180)
    x = x+ 0.2*math.cos((math.pi*j)/180)
    craft.setBlock(x, y, z, 57)



