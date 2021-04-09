import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x+1
y=cor.y
z=cor.z

craft.setBlocks(x-20,y-1,z-60,x+250, y-1, z+60, 12)
def Pyramid(s):
    global x, y, z, cor
    
    for i in range(int((s/2)+1)):
        craft.setBlocks(x,y, z, x+s, y, z+s, 24)
        x=x+1
        y=y+1
        z=z+1
        s=s-2
    y=cor.y
    #z=cor.z
    #x=cor.x
 
    
Pyramid(50)
x=x+75
Pyramid(40)
x=x+50
Pyramid(30)

    
         
         
