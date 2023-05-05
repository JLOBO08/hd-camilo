import re

POL = {}

def carrega_sentilex():
    with open ("sentilexjj.txt") as f:
        for linha in f:
            linha = re.sub(r"ANOT=.*", "", linha)
            lista = re.split(r";", linha)
            if len(lista) == 5:
                pallemapos, flex, assina, pol, lixo = lista
                pal= re.split(r",", pallemapos)[0]
                pol = int (re.sub(r"POL:N[01]=", "", pol))
                POL[pal] = pol
                #print (pal, pol)
            elif len(lista) == 6:
                pallemapos, flex, assina, pol1, pol2, lixo = lista
                pal= re.split(r",", pallemapos)[0]
                pol1 = int (re.sub(r"POL:N[01]=", "", pol1))
                pol2 = int (re.sub(r"POL:N[01]=", "", pol2))
                POL[pal] = (pol1+pol2)/2
                # print(pal, (pol1+pol2)/2)
            else:
                print (lista)
                exit()


#frase = "O Manel está feliz e contente"

def sentimento(frase):
    # lp = frase.split()
    lp = re.findall(r"\w+", frase)
    poltotal = 0
    for p in lp:
        if p in POL:
            poltotal += POL [p]
    return poltotal

carrega_sentilex()

# frase = "O assassino está feliz e contente, até radiante"

txt = open("harry_potter_pedra_filosofal.txt").read()
listacap = re.split(r"#", txt)
for cap in listacap:

    print(sentimento(cap))

# print(poltotal)
