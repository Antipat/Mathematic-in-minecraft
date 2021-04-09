import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x+20
y = cor.y
z = cor.z

# очистка пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

k=20
d =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4]
for h in range(20):
    for i in range (-20,20):
        for j in range (-20, 20):
            if math.pow(i,2)+math.pow(j,2)<=math.pow(k,2):
                craft.setBlock(x+i, y, z+j, 35,d[h])
    y=y+1
    






    
    
        
      
        
            

