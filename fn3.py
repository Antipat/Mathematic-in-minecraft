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


# построим график y=x^4+ 8*x^3+24*x^2+32*x+16
for i in range (-10, 11):
    y1=0.01*(math.pow(i,4)+8* math.pow(i, 3)+ 24*math.pow(i,2)+32*i+16)
    craft.setBlock(x+i, y+y1, z, 35, 1)



