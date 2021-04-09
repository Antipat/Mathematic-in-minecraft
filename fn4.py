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


# построим график y=pi^x
for i in range (-10, 11):
    y1=(math.pow(math.pi,i))
    craft.setBlock(x+i, y+y1, z, 35, 14)

# построим график y=e^x
for i in range (-10, 11):
    y1=10*(math.pow(math.e,i))
    craft.setBlock(x+i, y+y1, z, 35, 4)

