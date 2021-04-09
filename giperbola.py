import mcpi.minecraft as minecraft
import mcpi.block as block

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y
z = cor.z

# очистка пространства
craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

#построение гиперболы
for i in range (-20, 20):
    # обходим момент достижения i значения ноль
    if i==0:
        continue
    # для каждого значения i ставим в соответствие значение y1 =1/(x^2)
    y1=100*1/(i**2)
    
    #строим блок
    craft.setBlock(x+i,y+y1,z,17)
    
    
    

