##import mcpi.minecraft as minecraft
##
##craft = minecraft.Minecraft.create()
##cor = craft.player.getTilePos()

BlockMaterial={
"black0":(251,15),"black1":173, "black2":(35,15), "red0":215, "red1":152, "red2":214, "red3":(251,14), "red4":(35,14), "red5":(159,14),
"red6":45, "red7":249, "red8":250, "orange0":(35,1), "orange1":(251,1), "orange2":213, "orange3":(5,4), "orange4":(125,4),
"orange5":(159,1), "orange6":(179,0), "orange7":(179,2), "orange8":(179,1),
"yellow0":41,"yellow1":(35, 4),"yellow2":(251, 4),"yellow3":223,
"lightGreen0":(19, 0),"lightGreen1":(19, 1),"lightGreen2":103,"lightGreen3":121,
"green0":165,"green1":133,"green2":(35, 5),"green3":(251, 5),"green4":224,"green5":(159, 5),"green6":(35, 13),
"cyan0":(168, 0),"cyan1":(168, 1),"cyan2":(35, 9),"cyan3":228,"cyan4":(251, 9),"cyan5":57,
"lightBlue0":(35, 3),"lightBlue1":222,"lightBlue2":(251, 3),
"blue0":79,"blue1":174,"blue2":22,"blue3":(35, 11),"blue4":(251, 11),"blue5":246,
"violet0":(35, 10), "violet1":245, "violet2":(251, 10),"violet3":(251,2),"violet4":221,"violet5":(35,2),
"violet6":(159, 11), "violet7":(159, 3),
"lilac0":229, "lilac1":202}


# функция назначения цвета
def ChooseColor(H):
     # красный насыщенный
    if (H>=0 and H<=6) or (H>=245 and H<=255):
        color = BlockMaterial['red1']
    elif (H>=7 and H<=10) or (H>=235 and H<=244):
        color = BlockMaterial['red2']
    elif (H>=11 and H<=14):
        color = BlockMaterial['orange2']
    elif (H>=15 and H<=18):
        color = BlockMaterial['orange1']
    elif (H>=19 and H<=25):
        color = BlockMaterial['orange0']
    elif (H>=26 and H<=30):
        color = BlockMaterial['yellow2']
    elif (H>=31 and H<=35):
        color = BlockMaterial['yellow1']
    elif (H>=36 and H<=45):
        color = BlockMaterial['yellow0']
    elif (H>=46 and H<=55):
        color = BlockMaterial['lightGreen0']
    elif (H>=56 and H<=60):
        color = BlockMaterial['lightGreen1']
    elif (H>=61 and H<=68):
        color = BlockMaterial['green2']
    elif (H>=69 and H<=100):
        color = BlockMaterial['green3']
    elif (H>=101 and H<=108):
        color = BlockMaterial['green6']
    elif (H>=109 and H<=115):
        color = BlockMaterial['cyan1']
    elif (H>=116 and H<=125):
        color = BlockMaterial['cyan2']
    elif (H>=126 and H<=131):
        color = BlockMaterial['cyan5']
    elif (H>=132 and H<=136):
        color = BlockMaterial['lightBlue0']
    elif (H>=132 and H<=140):
        color = BlockMaterial['lightBlue2']
    elif (H>=141 and H<=145):
        color = BlockMaterial['blue5']
    elif (H>=146 and H<=150):
        color = BlockMaterial['blue2']
    elif (H>=151 and H<=160):
        color = BlockMaterial['blue3']
    elif (H>=161 and H<=185):
        color = BlockMaterial['blue4']
    elif (H>=186 and H<=195):
        color = BlockMaterial['violet2']
    elif (H>=196 and H<=205):
        color = BlockMaterial['violet0']
    elif (H>=206 and H<=215):
        color = BlockMaterial['violet3']
    elif (H>=216 and H<=225):
        color = BlockMaterial['violet5']
    elif (H>=226 and H<=244):
        color = BlockMaterial['red4']

    return color