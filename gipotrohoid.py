import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z
k=0.3
k1=1
s=(k1-k)/k
for i in range (720):
    
    x=x+(k1-k)*math.cos((math.pi*i)/180)+(k1+k)*(math.cos(s*(math.pi*i)/180))
    z=z+(k1-k)*math.sin((math.pi*i)/180)-(k1+k)*(math.sin(s*(math.pi*i)/180))
    craft.setBlock(x, y, z, 35, 5)
    
           
    
    
    
    


