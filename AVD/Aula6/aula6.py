import re


with open("sentilexjj.txt") as f:
    for linha in f:
        linha = re.sub (r"ANOT=.*","", linha)
        lista = re.split(r";", linha)
        if len(lista) == 5:
            pallemapos, flex, assina, pol, lixo = lista
            re.split(r"," ,pallemapos)[0]
            pol = re.sub (r"POL:NO=", "", pol)
            print (pal, pol)