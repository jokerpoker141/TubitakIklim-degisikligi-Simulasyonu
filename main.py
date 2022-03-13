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
    #genislik#
for i in range(uzunluk):
    for i in range(genislik):
        print(f"[{terrainSeed + np.random.randint(20)}]", end='')
    print("")

