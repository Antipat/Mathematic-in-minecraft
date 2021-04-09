import mcpi.minecraft as minecraft
craft=minecraft.Minecraft.create()

cor=craft.player.getTilePos()

print(cor.x, cor.y, cor.z)


















#craft.postToChat("x = "+str(cor.x)+" y = "+ str(cor.y)+" z = "+str(cor.z))

craft.postToChat(str(cor.x)+str(cor.y)+str(cor.z))









