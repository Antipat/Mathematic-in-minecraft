import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x+20
y = cor.y
z = cor.z
K = 25
s1 = -25
s2 = 26
for i in range (40):
    for n in range (s1, s2): 
        for j in range(s1, s2):
            if n**2+j**2<=(K**2):
                craft.setBlock(x+n, y, z+j, 35,1)
       
    s1=int(s1+0.5)
    s2=int(s2-0.5)
    y=y+1
    
    
    


