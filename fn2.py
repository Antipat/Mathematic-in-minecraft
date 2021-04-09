import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
x=cor.x
y=cor.y
z=cor.z

# строим оси координат
for j in range(50):
    craft.setBlock(x-25+j, y, z, 35,15)
    craft.setBlock(x, y-25+j, z, 35,15)


# построим график y=x^3-6*x^2+12*x+2
for i in range (-10, 11):
    y1=0.05*(math.pow(i, 3)+ (-6)*math.pow(i,2)+12*i+2)
    craft.setBlock(x+i, y+y1, z, 35, 1)



