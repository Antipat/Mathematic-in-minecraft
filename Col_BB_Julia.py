import mcpi.minecraft as minecraft
import mcpi.block as block
import ColorBlock

import time

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

x0 =-1.7
x1 = 1.7
y0 = -1.0
y1 = 1.0

d = 0.015
c =-0.8-0.156j
w = round((x1-x0)/d)
h = round((y1-y0)/d)

time.sleep(30)
print("Запуск")
for x in range(w):
    for y in range(h):
        z = complex(x0+x*d, y0+y*d)

        color =ColorBlock.MaterialColor(2,2)
        for H in range(255):
            if abs(z)>2:
                if (H>=0 and H<=6) or (H>=245 and H<=255):
                    color=ColorBlock.MaterialColor(3,1)
                elif (H>=7 and H<=10) or (H>=235 and H<=244):
                    color=ColorBlock.MaterialColor(3,4)
                elif (H>=11 and H<=14):
                    color=ColorBlock.MaterialColor(4,2)
                elif (H>=15 and H<=18):
                    color=ColorBlock.MaterialColor(4,1)
                elif (H>=19 and H<=25):
                    color=ColorBlock.MaterialColor(4,0)
                elif (H>=26 and H<=30):
                    color=ColorBlock.MaterialColor(6,2)
                elif (H>=31 and H<=35):
                    color=ColorBlock.MaterialColor(6,1)
                elif (H>=36 and H<=45):
                    color=ColorBlock.MaterialColor(6,0)
                elif (H>=46 and H<=55):
                    color=ColorBlock.MaterialColor(7,0)
                elif (H>=56 and H<=60):
                    color=ColorBlock.MaterialColor(7,1)
                elif (H>=61 and H<=68):
                    color=ColorBlock.MaterialColor(8,2)
                elif (H>=69 and H<=100):
                    color=ColorBlock.MaterialColor(8,3)
                elif (H>=101 and H<=108):
                    color=ColorBlock.MaterialColor(8,6)
                elif (H>=109 and H<=115):
                    color=ColorBlock.MaterialColor(9,1)
                elif (H>=116 and H<=125):
                    color=ColorBlock.MaterialColor(9,2)
                elif (H>=126 and H<=131):
                    color=ColorBlock.MaterialColor(9,5)
                elif (H>=132 and H<=136):
                    color=ColorBlock.MaterialColor(10,0)
                elif (H>=132 and H<=140):
                    color=ColorBlock.MaterialColor(10,2)
                elif (H>=141 and H<=145):
                    color=ColorBlock.MaterialColor(11,2)
                elif (H>=146 and H<=150):
                    color=ColorBlock.MaterialColor(11,3)
                elif (H>=151 and H<=160):
                    color=ColorBlock.MaterialColor(11,4)
                elif (H>=161 and H<=185):
                    color=ColorBlock.MaterialColor(11,5)
                elif (H>=186 and H<=195):
                    color=ColorBlock.MaterialColor(12,0)
                elif (H>=196 and H<=205):
                    color=ColorBlock.MaterialColor(12,2)
                elif (H>=206 and H<=215):
                    color=ColorBlock.MaterialColor(12,3)
                elif (H>=216 and H<=225):
                    color=ColorBlock.MaterialColor(12,5)
                elif (H>=226 and H<=244):
                    color=ColorBlock.MaterialColor(3,3)
                break
            z = z*z+c
        craft.setBlock(cor.x+x, cor.y+y, cor.z+1, color)

