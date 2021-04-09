import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z
# список для записи радиусов окружностей.
d =[]

# Очистка рабочего пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

a= b = 5
c = 1
# Создание гиперболоида
for k in range(-20,20):
    y1=k
    
    if k==0:
        craft.setBlock(x+x1,y+y1,z+z1, 0)
    else:
        r = a * math.sqrt((k / c)**2 +1)
        
    for j in range (360):
        x1 = 0.2*r*math.cos((math.pi *j)/180)
        z1 = 0.2*r*math.sin((math.pi *j)/180)
        
        craft.setBlock(x+x1,y+y1,z+z1, 20)
        
#Создание дна и потолка часов
r=20
for e in range (40):
    for j in range (360):
        x1 = r*math.cos((math.pi *j)/180)
        z1 = r*math.sin((math.pi *j)/180)
        craft.setBlock(x+x1,y-21,z+z1, 20)
        craft.setBlock(x+x1,y+22,z+z1, 20)
    r=r-1
    
# Заполнение верхней части часов водой
r1 = a/1.2 * math.sqrt((20 / c)**2 +1)
for i in range (38):
    # Запись радиусов в список d
    d.append(r1)
    for j in range (360):
        x1 = 0.2*r1*math.cos((math.pi *j)/180)
        z1 = 0.2*r1*math.sin((math.pi *j)/180)
        
        craft.setBlock(x+x1,y+21,z+z1, 8)
    r1=r1-2

craft.player.setTilePos(x+30,y,z)

# Задержка по времени
for w in range(5,-1, -1):
    craft.postToChat("До начала = "+str(w))
    time.sleep(2)

# Процесс заполнения водой нижней половины часов послойно
# Удаление воды в верхней половине часов послойно
for m in range (16):
    b=len(d)
       
    for h in range (b, 0,-1):
        r2=d[h-1]
        for j in range (360):
            x1 = 0.2*r2*math.cos((math.pi *j)/180)
            z1 = 0.2*r2*math.sin((math.pi *j)/180)
        
            craft.setBlock(x+x1,y-20+m,z+z1, 8)
            craft.setBlock(x+x1,y+21-m,z+z1, 0)
        time.sleep(0.01)
        
    if b>=3:
        d.pop(0)
        d.pop(1)
        d.pop(2)
    
    
           

