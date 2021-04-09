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

#x**2/a**2 + y**2/b**2 - z**2/c**2 = 0

a= b = 5
c = 3
# Создание конусного жилья
for k in range(-20,0):
    y1=k
    r = (a/c) *math.fabs(k) 
    
    for j in range (360):
        x1 = 0.2*r*math.cos((math.pi *j)/180)
        z1 = 0.2*r*math.sin((math.pi *j)/180)

        #Создание окна
        if k>=-15 and k<-10 and j>=150 and j<=220:
            craft.setBlock(x+x1,y+y1,z+z1, 20)
        #Создание входа
        elif k>=-20 and k<-18 and j>=150 and j<=220:
            craft.setBlock(x+x1,y+y1,z+z1, 0)

        #Создание стен дома
        else:
            craft.setBlock(x+x1,y+y1,z+z1, 45)
      
        
            

