import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

# Оси координат
for j in range(50):
    craft.setBlock(x-25+j, y, z, 35,15)
    craft.setBlock(x, y-25+j, z, 35,15)


for i in range(-10, 11):
    y1=-2*0.1*(i**2) - 2*0.1*i-2 
    craft.setBlock(x+i, y+y1, z, 35,0)



for i in range(-10, 11):
    y1=-2*0.1*(i**2) - 2*0.1*i+2 
    craft.setBlock(x+i, y+y1, z, 35,1)
