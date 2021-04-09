
import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

# функция вращения правой ветви параболы
def par(x1,z1,n,r):
    u=0.01
    for i in range (n):
        cor.y=cor.y+u*((i*0.1)**2)
        x1=dub.x+r*i*math.sin((math.pi*k)/180)
        z1=dub.z+r*i*math.cos((math.pi*k)/180)

        craft.setBlock(x1, cor.y, z1, 35, 5)

# клонируем первоначальные координаты     
dub=cor.clone()

# Цикл на построения параболоида
for k in range(360):
    cor.y=dub.y
    par(dub.x, dub.z, 80, 0.5)


    
    

    
         
         
