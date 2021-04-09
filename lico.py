import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()


def kv(a, b, c, color):
    cor = craft.player.getTilePos()

    x=cor.x
    y=cor.y
    z=cor.z


    for i in range (-20, 21):
        y1 = a*0.1*(i**2)+b*0.1*i+c
        craft.setBlock(x+i, y+y1, z, 35,color)


def kv1(a, b, c, color):
    cor = craft.player.getTilePos()

    x=cor.x
    y=cor.y
    z=cor.z
    for i in range (-15, -5):
        y1 = a*0.1*(i**2)+b*0.1*i+c
        craft.setBlock(x+i, y+y1, z, 35,color)
        
def kv2(a, b, c, color):
    cor = craft.player.getTilePos()

    x=cor.x
    y=cor.y
    z=cor.z
    for i in range (5, 16):
        y1 = a*0.1*(i**2)+b*0.1*i+c
        craft.setBlock(x+i, y+y1, z, 35,color)


def line(k,b, color):
    cor = craft.player.getTilePos()

    x=cor.x
    y=cor.y
    z=cor.z
    y=y+20
    x=x-5
    for i in range (-5, 5):
        x1 = k*i
        craft.setBlock(x+x1, y+i, z, 35,color)
    x=x+10
    for i in range (-5, 5):
        x1 = k*i
        craft.setBlock(x+x1, y+i, z, 35,color)
        
def line1(k,b, color):
    cor = craft.player.getTilePos()

    x=cor.x
    y=cor.y
    z=cor.z
    for i in range (-5, 5):
        y1 = k*i+b
        craft.setBlock(x+i, y+y1, z, 35,color)
    y=y+20
    for i in range (-5, 5):
        x1 = k*i
        craft.setBlock(x+x1, y+i, z, 35,color)


#for j in range(50):
        #craft.setBlock(x-25+j, y, z, 35,15)
        #craft.setBlock(x, y-25+j, z, 35,15)
