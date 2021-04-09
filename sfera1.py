import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()
x=cor.x
y=cor.y
z=cor.z

R=100

x1=x+10
z1=z
y1=y


t1=1

for i in range(10):
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R:
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1+t1*math.sin(((math.pi)*j)/180)
    y1 = y1+t1
    
y1=y
for i in range(10):
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R:
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1+t1*math.sin(((math.pi)*j)/180)
    y1 = y1-t1
y1=y    
for i in range(10):
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R:
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1-t1*math.sin(((math.pi)*j)/180)
    y1 = y1+t1
    
y1=y
for i in range(10):
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R:
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1-t1*math.sin(((math.pi)*j)/180)
    y1 = y1-t1


