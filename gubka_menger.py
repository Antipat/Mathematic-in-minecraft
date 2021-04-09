import mcpi.minecraft as minecraft

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x+1
y=cor.y
z=cor.z

# 3^1
craft.setBlocks(x,y,z,x+2,y+2, z+2, 35, 2)

craft.setBlocks(x+1,y+1,z,x+1,y+1, z+2, 0)

craft.setBlocks(x,y+1,z+1,x+2,y+1, z+1, 0)
craft.setBlocks(x+1,y,z+1,x+1,y+2, z+1, 0)

z=z+10

# 3^2
craft.setBlocks(x,y,z,x+8,y+8, z+8, 35, 2)

craft.setBlocks(x+3,y+3,z,x+5,y+5, z+8, 0)

craft.setBlocks(x+1,y+1,z,x+1,y+1, z+8, 0)
craft.setBlocks(x+4,y+1,z,x+4,y+1, z+8, 0)
craft.setBlocks(x+7,y+1,z,x+7,y+1, z+8, 0)
craft.setBlocks(x+1,y+4,z,x+1,y+4, z+8, 0)
craft.setBlocks(x+7,y+4,z,x+7,y+4, z+8, 0)
craft.setBlocks(x+1,y+7,z,x+1,y+7, z+8, 0)
craft.setBlocks(x+4,y+7,z,x+4,y+7, z+8, 0)
craft.setBlocks(x+7,y+7,z,x+7,y+7, z+8, 0)

craft.setBlocks(x,y+3,z+3,x+8,y+5, z+5, 0)

craft.setBlocks(x,y+1,z+1,x+8,y+1, z+1, 0)
craft.setBlocks(x,y+1,z+4,x+8,y+1, z+4, 0)
craft.setBlocks(x,y+1,z+7,x+8,y+1, z+7, 0)
craft.setBlocks(x,y+4,z+1,x+8,y+4, z+1, 0)
craft.setBlocks(x,y+4,z+7,x+8,y+4, z+7, 0)
craft.setBlocks(x,y+7,z+1,x+8,y+7, z+1, 0)
craft.setBlocks(x,y+7,z+4,x+8,y+7, z+4, 0)
craft.setBlocks(x,y+7,z+7,x+8,y+7, z+7, 0)

craft.setBlocks(x+3,y,z+3,x+5,y+8, z+5, 0)

craft.setBlocks(x+1,y,z+1,x+1,y+8, z+1, 0)
craft.setBlocks(x+4,y,z+7,x+4,y+8, z+7, 0)
craft.setBlocks(x+7,y,z+7,x+7,y+8, z+7, 0)
craft.setBlocks(x+1,y,z+4,x+1,y+8, z+4, 0)
craft.setBlocks(x+4,y,z+1,x+4,y+8, z+1, 0)
craft.setBlocks(x+7,y,z+1,x+7,y+8, z+1, 0)
craft.setBlocks(x+7,y,z+4,x+7,y+8, z+4, 0)
craft.setBlocks(x+1,y,z+7,x+1,y+8, z+7, 0)
