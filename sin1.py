import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z
for i in range (720):
    craft.setBlock(x, y, z, 35, 5)
    
    x=x+0.1
    y=y+0.5*math.sin((math.pi*i)/180)
    
x = cor.x
y = cor.y

for i in range (720):
    craft.setBlock(x, y, z, 35, 5)
    
    x=x+0.1
    y=y+0.5*2*math.sin((math.pi*i)/180)
    
x = cor.x
y = cor.y

for i in range (720):
    craft.setBlock(x, y, z, 35, 5)
    
    x=x+0.1
    y=y+0.5*math.sin((2*math.pi*i)/180)
    
x = cor.x
y = cor.y

