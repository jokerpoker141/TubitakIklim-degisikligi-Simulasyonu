import numpy as np

# Taban degerler #
maxHeight = 1000
co2 = np.random.randint(400, 500)
o2 = np.random.randint(400, 500)
havaOrtalamasi = o2/co2

#seed#
seed = int(input("herhangi bir girdi giriniz"))
print("UYARI: girdiginiz sayilar kilometre cinsindendir. ")
genislik = int(input("simulasyonun genisligin giriniz"))
uzunluk = int(input("simulasyonun uzunlugunu giriiniz"))
#terrain generation#
    #Terrain seed bulucu#
if seed >= 100 and seed < 200:
    terrainSeed = seed/2 + np.random.randint(50)
elif seed <= 10:
    terrainSeed = seed
    terrainSeed = terrainSeed + np.random.randint(100)
elif seed > 10 and seed < 100:
    terrainSeed = seed
    terrainSeed = terrainSeed + np.random.randint(50)
elif seed > 200 and seed < 1000:
    terrainSeed = seed
    terrainSeed = terrainSeed/10
    if seed < 50:
        terrainSeed = terrainSeed + np.random.randint(50)
else: terrainSeed = print("daha kucuk bir sayi giriniz")

terrainSeed = int(terrainSeed)
    #generation variables
y = 0
x = 0 # kordinat sistemi

    #generation
for y in range(uzunluk): # uzunluk iterator
    for x in range(genislik): # genislik iterator
        if uzunluk <= 9 and genislik <= 9:
            print(f"[{x+1},{y+1}]", end="")
        elif uzunluk >= 10 and genislik >= 10:
            if x <= 9 and y <= 9:
                print(f" [ {x+1},{y+1} ]", end="")
            if x >= 10 and y >= 10:
                print(f"[{x+1},{y+1}]", end="")

    print("")# line breaker