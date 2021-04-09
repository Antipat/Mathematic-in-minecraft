import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

# Очистка рабочего пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

#x**2/a**2 + y**2/b**2 - z**2/c**2 = 1
# x=a chu cosv, y = b chu sin v, z= c shv u [0, 2pi] 

a= b = 3
c = 1
for k in range(-20,20):
    y1=k
    #r = a * math.sqrt(1 + (k / c)**2)
    if (k/c)**2>=1:
        r = a * math.sqrt((k / c)**2 -1)
    
        for j in range (360):
            x1 = 0.2*r*math.cos((math.pi *j)/180)
            z1 = 0.2*r*math.sin((math.pi *j)/180)
        
            craft.setBlock(x+x1,y+y1,z+z1, 57)
      
        
           

