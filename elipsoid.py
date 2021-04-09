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

#x**2/a**2 + y**2/b**2 + z**2/c**2 = 1

# Задаём коэффициенты
a = 10
b = 10
c = 10

# Построение эллипсоида

for k in range(-250,250):
    # создаём дробный шаг по Y для плотного заполнения поверхности
    y1=0.07*k
    # проверяем условие на то что значения y1 не будет превышать значение c
    if math.fabs (y1)<= c:
        r = math.sqrt(c**2 - y1**2)
    
        for j in range (360):
            x1 = (c/a)*r*math.cos((math.pi *j)/180)
            z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
            craft.setBlock(x+x1,y+y1,z+z1, 57)
      
        
            

