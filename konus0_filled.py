import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

# очистка пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

#x**2/a**2 + y**2/b**2 - z**2/c**2 = 0

a=  5
c = 3
P=a/c
s = 20
# Радиус первой окружности
n = 0.5*P *math.fabs(20)

# Построение конуса
for k in range(-20,0):
    y1=k
    r = 0.5*P *math.fabs(k)
    #Построение круга определённого радиуса на слое
    for h in range (200):
        for j in range (360):
            x1 = r*math.cos((math.pi *j)/180)
            z1 = r*math.sin((math.pi *j)/180)
        
            craft.setBlock(x+x1,y+y1,z+z1, 89)
        #Вычисление радиуса на каждом слое конуса
        r=r-(r/n)
    
    
        
      
        
            

