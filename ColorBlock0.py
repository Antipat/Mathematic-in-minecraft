import mcpi.minecraft as minecraft

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

BlockMaterial={
"white0": 80, "white1": (35,0),"white2": (155,0),"white3": (155,2), "white4": (155,1),"white5": 216,
"gray0": 42, "gray1": (251,0), "gray2": (1,4), "gray3": (1,3), "gray4": (43,0), "gray5": (35,8), "gray6": (251,8),
"gray7": (1,6), "gray8": (1,0), "gray9": (43,5), "gray10": 4, "gray11": 16, "gray12": 23, "black0":(251,15),
"black1":173, "black2":(35,15), "red0":215, "red1":152, "red2":214, "red3":(251,14), "red4":(35,14), "red5":(159,14),
"red6":45, "red7":249, "red8":250, "orange0":(35,1), "orange1":(251,1), "orange2":213, "orange3":(5,4), "orange4":(125,4),
"orange5":(159,1), "orange6":(179,0), "orange7":(179,2), "orange8":(179,1), "brown0":(159, 15),"brown1":(17, 13),
"brown2":(5, 5),"brown3":(162, 1),"brown4":(159, 7),"brown5":(159, 12),"brown6":(251, 12),"brown7":(35, 12),
"brown8":(17, 15),"brown9":(5, 1),"brown10":(17, 12),"brown11":(3, 1),"brown12":172,"brown13":(5, 3),"brown14":(5, 0),
"brown15":99,"brown16":(5, 2),"yellow0":41,"yellow1":(35, 4),"yellow2":(251, 4),"yellow3":223,"lightGreen0":(19, 0),
"lightGreen1":(19, 1),"lightGreen2":103,"lightGreen3":121, "green0":165,"green1":133,"green2":(35, 5),"green3":(251, 5),
"green4":224,"green5":(159, 5),"green6":(35, 13),"green7":(251, 13),"green8":232,"green9":(159, 13),"green10":(168,2),
"cyan0":(168, 0),"cyan1":(168, 1),"cyan2":(35, 9),"cyan3":228,"cyan4":(251, 9),"cyan5":57,"lightBlue0":(35, 3),
"lightBlue1":222,"lightBlue2":(251, 3),"blue0":79,"blue1":174,"blue2":22,"blue3":(35, 11),"blue4":(251, 11),"blue5":230,
"violet0":(35, 10), "violet1":245, "violet2":(251, 10),"violet3":(251,2),"violet4":221,"violet5":(35,2),
"violet6":(159, 11), "violet7":(159, 3),"lilac0":229, "lilac1":202,"pink0":(35, 6), "pink1":241, "pink2":(251, 6),
"pink3":225, "pink4":(159, 2) }

col = [['white0', 'white1', 'white2', 'white3', 'white4', 'white5'],
 ['gray0', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12'],
 ['black0', 'black1', 'black2'],
 ['red0', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'red7', 'red8'],
 ['orange0', 'orange1', 'orange2', 'orange3', 'orange4', 'orange5', 'orange6', 'orange7', 'orange8'],
 ['brown0', 'brown1', 'brown2', 'brown3', 'brown4', 'brown5', 'brown6', 'brown7', 'brown8', 'brown9', 'brown10', 'brown11', 'brown12', 'brown13', 'brown14', 'brown15', 'brown16'],
 ['yellow0', 'yellow1', 'yellow2', 'yellow3'],
 ['lightGreen0', 'lightGreen1', 'lightGreen2', 'lightGreen3'],
 ['green0', 'green1', 'green2', 'green3', 'green4', 'green5', 'green6', 'green7', 'green8', 'green9', 'green10'],
 ['cyan0', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'cyan5'],
 ['lightBlue0', 'lightBlue1', 'lightBlue2'],
 ['blue0', 'blue1', 'blue2', 'blue3', 'blue4', 'blue5'],
 ['violet0', 'violet1', 'violet2', 'violet3', 'violet4', 'violet5', 'violet6', 'violet7'],
 ['lilac0', 'lilac1'],
 [ 'pink0', 'pink1', 'pink2', 'pink3', 'pink4']]

##def MaterialColor(m,k):
##    return BlockMaterial[col[m][k]]
##
##def MaterialColor(k):
##    return BlockMaterial[k]

##N =0
##color = MaterialColor("black0")
##craft.setBlock(cor.x+1, cor.y+1, cor.z,color)

##print(len(col))
##for i in range(len(col)):
##    for j in range(len(col[i])):
##        craft.setBlock(cor.x+1+j, cor.y+1, cor.z+i, BlockMaterial[col[i][j]])
##    print(len(col[i]))
##    N+=len(col[i])
##print(N)
#def color(textColor):
    #return BlockMaterial.get(textColor)


#print(BlockMaterial.keys())
#idBlock = [(35,6),241,(251,6),225,(159,2)]
#print(color("white1")229
##for j in range(len(idBlock)):
##
##    print('"pink'+str(j)+'":'+str(idBlock[j])+', ',end='')
##
##for i in range(len(idBlock)):
##    craft.setBlock(cor.x+1+i, cor.y+1, cor.z, idBlock[i])


##craft.setBlock(cor.x+2, cor.y+1, cor.z, 209)
##craft.setBlock(cor.x+3, cor.y+1, cor.z, (35,15))
##craft.setBlock(cor.x+4, cor.y+1, cor.z, 49)
#craft.setBlock(cor.x+5, cor.y+1, cor.z, (95,15))

#craft.setBlock(cor.x+6, cor.y+1, cor.z, 130)

#craft.setBlock(cor.x+7, cor.y+1, cor.z, (159,15))
##craft.setBlock(cor.x+5, cor.y+1, cor.z, 173)


#craft.setBlock(cor.x+9, cor.y+1, cor.z, (252,15))
#craft.setBlock(cor.x+10, cor.y+1, cor.z, 234)
##craft.setBlock(cor.x+11, cor.y+1, cor.z, 4)
##craft.setBlock(cor.x+12, cor.y+1, cor.z, 16)
##craft.setBlock(cor.x+13, cor.y+1, cor.z, 23)


#craft.setBlock(cor.x+13, cor.y+1, cor.z, (43,3))

#craft.setBlock(cor.x+15, cor.y+1, cor.z, (97,0))
#craft.setBlock(cor.x+16, cor.y+1, cor.z, (97,1))

#craft.setBlock(cor.x+15, cor.y+1, cor.z, 227)


#craft.setBlock(cor.x+4, cor.y+1, cor.z, (95,0))
#craft.setBlock(cor.x+11, cor.y+1, cor.z, (17,2))
#craft.setBlock(cor.x+12, cor.y+1, cor.z, (99,10))

#craft.setBlock(cor.x+13, cor.y+1, cor.z, (99,14))
#craft.setBlock(cor.x+14, cor.y+1, cor.z, (100,14))




