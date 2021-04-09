import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

for i in range (-10, 11):
    y1=-5*(0.1*i**2)
    craft.setBlock(x+i, y+y1, z, 35,0)

for i in range (-10, 11):
    y1=-2*(0.1*i**2)
    craft.setBlock(x+i, y+y1, z, 35,1)

#for i in range (-10, 11):
    #y1=-1*(0.1*i**2)
    #craft.setBlock(x+i, y+y1, z, 35,2)

#for i in range (-10, 11):
    #y1=1*(0.1*i**2)
    #craft.setBlock(x+i, y+y1, z, 35,3)

