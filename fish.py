import mcpi.minecraft as minecraft
import mcpi.block as block


craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
x=cor.x
y=cor.y
z=cor.z
def kvY(a, b, c, i1, i2, k, color):
    
    # y= a*x^2+b*x+c, Интервал построения [i1,i2), color - цвет графика
    # k - параметр для отклонения графика по оси X
    for i in range (i1, i2):
        y1 = a*0.1*(i**2)+b*0.1*i+c
        craft.setBlock(x+i+k, y+y1, z, 35,color)

def kvX(a, b, c, i1, i2, k, color):
    # y= a*x^2+b*x+c, Интервал построения [i1,i2), color - цвет графика,
    # k - параметр для отклонения графика по оси Y

    for i in range (i1, i2):
        x1 = a*0.1*(i**2)+b*0.1*i+c
        craft.setBlock(x+x1, y+i+k, z, 35,color)

