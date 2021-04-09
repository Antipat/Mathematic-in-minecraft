import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
x=cor.x
y=cor.y
z=cor.z

# построим график y=x^0.5

for i in range (50):
    y1=1.5*math.sqrt(i)
    craft.setBlock(x+i, y+y1, z, 35, 13)

for i in range (-20, 20):
    y1=math.sqrt(i**2)
    craft.setBlock(x+i, y+y1, z, 35, 8)



#for i in range (50):
    #y1=1.5*math.pow(i, 1/3)
    #craft.setBlock(x+i, y+y1, z, 35, 4)
    
#for i in range (-50,0):
    #y1=-1.5*math.pow(math.fabs(i), 1/3)
    #craft.setBlock(x+i, y+y1, z, 35, 4)

#for i in range (-50,50):
    #if i>=0:
        #y1=2*math.pow(i, 1/3)
    #else:
        #y1=-2*math.pow(math.fabs(i), 1/3)
    #craft.setBlock(x+i, y+y1, z, 35, 5)





