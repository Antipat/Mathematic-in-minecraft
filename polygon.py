import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()
x=cor.x+10
y=cor.y
z=cor.z
d1 =[]
d2 =[]
d3 =[]

ff=0.20
f=10

#for i in range(360):
    #z = z+0.2*math.sin((math.pi*i)/180)
    #x = x+ 0.2*math.cos((math.pi*i)/180)
    #s=i%60
    #if s==0:
        #craft.setBlock(int(x), int(y),  int(z), 35,5)
        #print(x,y,z)
        #d1.append(x)
        #d2.append(y)
        #d3.append(z)
        
        
        
    #else:
        #craft.setBlock(x, y,  z, 35,1)
    
#print(d1)
#print(d2)
#print(d3)
#print(x,y,z)

def shesty():
    global x,y,z,ff,f
    d1.clear()
    d2.clear()
    d3.clear()
    for i in range(360):
    
        x = x+ ff*math.cos((math.pi*i)/180)
        z = z+ ff*math.sin((math.pi*i)/180)
        s=i%60
        if s==0:
            #craft.setBlock(int(x), int(y),  int(z), 35,5)
            #print(x,y,z)
            d1.append(x)
            d2.append(y)
            d3.append(z)
            
    k1=(d3[0]-d3[1])/(d1[0]-d1[1])

    #print("k = ", k1)
    # построение первой стороны
    for j in range(int(f)+1):
        z1=k1*j
        craft.setBlock(d1[0]+j, d2[0],  d3[0]+z1, 35,5)

    # построение второй стороны
    
    #Если вычислять по
    # k2=(d3[1]-d3[2])/(d1[1]-d1[2]), то
    # знаменатель обращается в ноль
    

    for j in range(int(f)+1):
        craft.setBlock(d1[1], d2[1],  d3[1]+j, 35,5)

    # построение третьей стороны  +2  
    k3=(d3[2]-d3[3])/(d1[2]-d1[3])

    for j in range(int(f)+1):
        z1=k3*j
        craft.setBlock(d1[2]- j, d2[2],  d3[2]-z1, 35,5)
    
    # построение четвёртой стороны
    k4=(d3[3]-d3[4])/(d1[3]-d1[4])

    for j in range(int(f)+1):
        z1=k4*j
        craft.setBlock(d1[3]-j, d2[3],  d3[3]-z1, 35,5)

    #построение пятой стороны

    #Если вычислять по
    #k5=(d3[4]-d3[5])/(d1[4]-d1[5]), то
    # знаменатель обращается в ноль
    
    for j in range(int(f)+1):
        craft.setBlock(d1[4], d2[4],  d3[4]-j, 35,5)

    # построение шестой стороны +2
    k6=(d3[5]-d3[0])/(d1[5]-d1[0])
    for j in range(int(f)+1):
        z1=k6*j
        craft.setBlock(d1[5]+j, d2[5],  d3[5]+z1, 35,5)

    
  
for t1 in range (10):

    for i in range(40):
        shesty()
        ff =ff -0.005
        f=f-0.25    
    
    ff=0.2
    f=10
    y=y+1

