import mcpi.minecraft as minecraft
from ColorBlock import *

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

x0 =-1.7
x1 = 1.7
y0 = -1.0
y1 = 1.0

d = 0.015
c = 0.8j
## 0.35 + 0.35j
##-0.7269 + 0.1889j
##-0.8-0.156j
w = round((x1-x0)/d)
h = round((y1-y0)/d)

print("Запуск")
for x in range(w):
    for y in range(h):
        z = complex(x0+x*d, y0+y*d)

        color = BlockMaterial["black0"]
        for H in range(255):
            if abs(z)>2:
                color = ChooseColor(H)
                break
            z = z*z+c
        craft.setBlock(cor.x+x, cor.y+y, cor.z+1, color)

