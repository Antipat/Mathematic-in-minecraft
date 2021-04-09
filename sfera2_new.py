import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()
x=cor.x
y=cor.y
z=cor.z

# квадрат радиуса
R=100

x1=x+10
z1=z
y1=y

#коэффициент пропорциональности - размер сферы
t1=1
# построение первой и четвёртой четверти
for i in range(21):
    
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R and (x1-x)**2+(y1-y)**2+(z1-z)**2>=(R-1):
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1+t1*math.sin(((math.pi)*j)/180)
    if i<10 :
        n=1
    elif i==11:
        y1=y
    else:
        n=-1
    y1 = y1+n*t1
    
    
y1=y

# построение второй и третьей четверти
for i in range(21):
    for j in range(360):
        for p in range (360):
            if (x1-x)**2+(y1-y)**2+(z1-z)**2<=R and (x1-x)**2+(y1-y)**2+(z1-z)**2>=(R-1):
                craft.setBlock(x1, y1, z1, 35, 3)
            x1=x1+t1*math.cos((math.pi*p)/180)
        z1=z1-t1*math.sin(((math.pi)*j)/180)
    if i<10 :
        n=1
    elif i==11:
        y1=y
    else:
        n=-1
    y1 = y1+n*t1
    
y1=y


