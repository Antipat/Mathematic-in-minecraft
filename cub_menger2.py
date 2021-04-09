import mcpi.minecraft as minecraft

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

x=cor.x+1
y=cor.y
z=cor.z

def menger(a):
    global x,y,z
    d=3**a
    k=d
    m = d-1
    h=int(d/3)
    s=[]
    f=h
    for i in range (a):
        s.append(f)
        f=int(f/3)
    print(s)
    
    craft.setBlocks(x,y,z,x+m,y+m, z+m, 35, 5)
    print(" x1 " +str(x)+" y1 " +str(y)+" z1 " +str(z))
    
    for i in range(a):
        
        
        if k==d:
            craft.setBlocks(x+h,y+h,z,x+2*h-1,y+2*h-1, z+d, 0)
            craft.setBlocks(x,y+h,z+h,x+d,y+2*h-1, z+2*h-1, 0)
            craft.setBlocks(x+h,y,z+h,x+2*h-1,y+d, z+2*h-1, 0)
        elif k==s[0]:
            for l in range(a):
                for j in range(a):
                    craft.setBlocks(x+s[1],y+s[1],z,x+2*s[1]-1,y+2*s[1]-1, z+d, 0)
                    craft.setBlocks(x+s[1],y+s[1],z+s[1],x+s[1],y+2*s[1]-1, z+2*h-1, 0)
                    craft.setBlocks(x+s[1],y+s[1],z+s[1],x+2*s[1]-1,y+s[1], z+2*h-1, 0)
                    print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                    
                    
                    x=x+s[0]
                x=cor.x+1
                
                for j in range(a):
                    craft.setBlocks(x,y+s[1],z+s[1],x+d,y+2*s[1]-1, z+2*s[1]-1, 0)
                    craft.setBlocks(x+s[1],y+s[1],z+s[1],x+s[1],y+2*s[1]-1, z+2*h-1, 0)
                    craft.setBlocks(x+s[1],y+s[1],z+s[1],x+2*s[1]-1,y+s[1], z+2*h-1, 0)
                    
                    
                    print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                    z=z+s[0]
                y=y+s[0]
                z=cor.z
            y=cor.y
            x=cor.x+1
            z=cor.z
            for l in range(a):
                for l in range(a):
                    craft.setBlocks(x+s[1],y,z+s[1],x+2*s[1]-1,y+d, z+2*s[1]-1, 0)
                    x=x+s[0]
                x=cor.x+1
                z=z+s[0]
                
            x=cor.x+1
            y=cor.y
            z=cor.z
            if len(s)==2:
                for l in range(a):
                    for j in range(a):
                        craft.setBlocks(x+s[1],y+s[1],z,x+2*s[1]-1,y+2*s[1]-1, z+d, 0)
                        craft.setBlocks(x+s[1],y+s[1],z+s[1],x+s[1],y+2*s[1]-1, z+2*s[1]-1, 0)
                        craft.setBlocks(x+s[1],y+s[1],z+s[1],x+2*s[1]-1,y+s[1], z+2*s[1]-1, 0)
            
                        for l in range(a+1):
                            craft.setBlocks(x,y+t,z+t,x+d,y+2*t-1, z+t, 0)
                            craft.setBlocks(x+t,y+t,z+h+t,x+t,y+2*t-1, z+h+2*t-1, 0)
                            craft.setBlocks(x+t,y+t,z+h+t,x+2*h-1,y+t, z+h+2*t-1, 0)
                            z=z+h
                            #print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=cor.z
                        x=x+s[0]
                    y=y+s[0]
                x=cor.x+1
                y=cor.y
                z=cor.z
                for l in range(a):
                    for l in range(a):
                        craft.setBlocks(x+s[1],y,z+s[1],x+2*s[1]-1,y+d, z+2*s[1]-1, 0)
                        x=x+s[0]
                    x=cor.x+1
                    z=z+s[0]
                
                x=cor.x+1
                y=cor.y
                z=cor.z
            elif len(s)==3:
                
                for l in range(a**2):
                    for j in range(a**2):
                        craft.setBlocks(x+s[2],y+s[2],z,x+2*s[2]-1,y+2*s[2]-1, z+d, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[1]
                    x=cor.x+1
                    
                    for j in range(a**2):
                        craft.setBlocks(x,y+s[2],z+s[2],x+d,y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[1]
                    y=y+s[1]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**2):
                    for l in range(a**2):
                        craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        x=x+s[1]
                    x=cor.x+1
                    z=z+s[1]

            elif len(s)==4:
                for l in range(a**2):
                    for j in range(a**2):
                        craft.setBlocks(x+s[2],y+s[2],z,x+2*s[2]-1,y+2*s[2]-1, z+d, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[1]
                    x=cor.x+1
                    
                    for j in range(a**2):
                        craft.setBlocks(x,y+s[2],z+s[2],x+d,y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[1]
                    y=y+s[1]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**2):
                    for l in range(a**2):
                        craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        x=x+s[1]
                    x=cor.x+1
                    z=z+s[1]
                    
                x=cor.x+1
                z=cor.z
                y=cor.y
                
                for l in range(a**3):
                    for j in range(a**3):
                        craft.setBlocks(x+s[3],y+s[3],z,x+2*s[3]-1,y+2*s[3]-1, z+d, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+s[3],y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+2*s[3]-1,y+s[3], z+2*s[3]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[2]
                    x=cor.x+1
                    
                    for j in range(a**3):
                        craft.setBlocks(x,y+s[3],z+s[3],x+d,y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+s[3],y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+2*s[3]-1,y+s[3], z+2*s[3]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[2]
                    y=y+s[2]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**3):
                    for l in range(a**3):
                        craft.setBlocks(x+s[3],y,z+s[3],x+2*s[3]-1,y+d, z+2*s[3]-1, 0)
                        x=x+s[2]
                    x=cor.x+1
                    z=z+s[2]
        elif len(s)==5:
                for l in range(a**2):
                    for j in range(a**2):
                        craft.setBlocks(x+s[2],y+s[2],z,x+2*s[2]-1,y+2*s[2]-1, z+d, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[1]
                    x=cor.x+1
                    
                    for j in range(a**2):
                        craft.setBlocks(x,y+s[2],z+s[2],x+d,y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+s[2],y+2*s[2]-1, z+2*s[2]-1, 0)
                        craft.setBlocks(x+s[2],y+s[2],z+s[2],x+2*s[2]-1,y+s[2], z+2*s[2]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[1]
                    y=y+s[1]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**2):
                    for l in range(a**2):
                        craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        x=x+s[1]
                    x=cor.x+1
                    z=z+s[1]
                    
                x=cor.x+1
                z=cor.z
                y=cor.y
                
                for l in range(a**3):
                    for j in range(a**3):
                        craft.setBlocks(x+s[3],y+s[3],z,x+2*s[3]-1,y+2*s[3]-1, z+d, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+s[3],y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+2*s[3]-1,y+s[3], z+2*s[3]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[2]
                    x=cor.x+1
                    
                    for j in range(a**3):
                        craft.setBlocks(x,y+s[3],z+s[3],x+d,y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+s[3],y+2*s[3]-1, z+2*s[3]-1, 0)
                        craft.setBlocks(x+s[3],y+s[3],z+s[2],x+2*s[3]-1,y+s[3], z+2*s[3]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[2]
                    y=y+s[2]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**3):
                    for l in range(a**3):
                        craft.setBlocks(x+s[3],y,z+s[3],x+2*s[3]-1,y+d, z+2*s[3]-1, 0)
                        x=x+s[2]
                    x=cor.x+1
                    z=z+s[2]
                y=cor.y
                x=cor.x+1
                z=cor.z    
                for l in range(a**4):
                    for j in range(a**4):
                        craft.setBlocks(x+s[4],y+s[4],z,x+2*s[4]-1,y+2*s[4]-1, z+d, 0)
                        craft.setBlocks(x+s[4],y+s[4],z+s[4],x+s[4],y+2*s[4]-1, z+2*s[4]-1, 0)
                        craft.setBlocks(x+s[4],y+s[4],z+s[3],x+2*s[4]-1,y+s[4], z+2*s[4]-1, 0)
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        
                        
                        x=x+s[3]
                    x=cor.x+1
                    
                    for j in range(a**4):
                        craft.setBlocks(x,y+s[4],z+s[4],x+d,y+2*s[4]-1, z+2*s[4]-1, 0)
                        craft.setBlocks(x+s[4],y+s[4],z+s[3],x+s[4],y+2*s[4]-1, z+2*s[4]-1, 0)
                        craft.setBlocks(x+s[4],y+s[4],z+s[3],x+2*s[4]-1,y+s[4], z+2*s[4]-1, 0)
                        #craft.setBlocks(x+s[2],y,z+s[2],x+2*s[2]-1,y+d, z+2*s[2]-1, 0)
                        
                        print(" x " +str(x)+" y " +str(y)+" z " +str(z))
                        z=z+s[3]
                    y=y+s[3]
                    z=cor.z
                y=cor.y
                x=cor.x+1
                z=cor.z
                for l in range(a**4):
                    for l in range(a**4):
                        craft.setBlocks(x+s[4],y,z+s[4],x+2*s[4]-1,y+d, z+2*s[4]-1, 0)
                        x=x+s[3]
                    x=cor.x+1
                    z=z+s[3]
        else:
            pass
                        
                        
        print("k= ", k)
        k=int(k/3)
        t=int(h/3)
        
menger(3)


