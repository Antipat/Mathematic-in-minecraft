import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

# очистка пространства

craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

a = b = 1

for k in range(120):
    y1=0.1*k
    
    r = a * math.sqrt(k)
    
    for j in range (360):
        x1 = r*math.cos((math.pi *j)/180)
        z1 = r*math.sin((math.pi *j)/180)
        
        craft.setBlock(x+x1,y+y1,z+z1, 20)    

r1 = a * math.sqrt(10)

# Создание горячего супа из лавы
for i in range (19):
    
    for j in range (360):
        x1 = 0.2*r1*math.cos((math.pi *j)/180)
        z1 = 0.2*r1*math.sin((math.pi *j)/180)
        
        craft.setBlock(x+x1,y+11,z+z1, 10)
    r1=r1-2
    
         
         
