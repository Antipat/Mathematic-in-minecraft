import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

# очистка пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

k=0.2
for h in range(20):
    for i in range (20):
    
        for j in range(360):
            z = z + k * math.sin((math.pi*j)/180)
            x = x + k * math.cos((math.pi*j)/180)
            craft.setBlock(x, y, z, 35,9)
        k=k-0.01
    y=y+1
    k=0.2
    

    
    
        
      
        
            

