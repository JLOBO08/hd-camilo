#!/usr/bin/python3
import re
import csv
POL = {}

def carrega_sentilex():
    with open("sentilexjj.txt") as f:
        for linha in f:
            linha = re.sub(r"ANOT=.*", "", linha)
            lista = re.split(r";",linha)
            if len(lista) == 5:
                pallemapos, flex, assina, pol, lixo = lista
                pal = re.split(r",",pallemapos)[0]
                pol = int( re.sub(r"POL:N[01]=", "", pol) )
                POL[pal] = pol
            elif len(lista) == 6:
                pallemapos, flex, assina, pol1, pol2, lixo = lista
                pal = re.split(r",",pallemapos)[0]
                pol1 = int( re.sub(r"POL:N[01]=", "", pol1) )
                pol2 = int( re.sub(r"POL:N[01]=", "", pol2) )
                POL[pal] = (pol1+pol2)/2 
            else:
                print(lista)
                exit()

def sentimento(frase):
    lp = re.findall(r"\w+", frase)    #  era...lp = frase.split()
    ptotalneg = 0 
    ptotalpos = 0
    qp = 0
    qn = 0

    for p in lp:
        if p in POL:
            v = POL[p]
            if  v > 0: 
                ptotalpos += v
                qp += 1

            if  v < 0: 
                ptotalneg += -v
                qn += 1


    return (ptotalpos,qp,ptotalneg,qn, len(lp)) 

carrega_sentilex()

txt = open("Camilo-A_mulher_fatal.md").read()
ptotalpos, qp,ptotalneg,qn,np= sentimento(txt)
Factor = ptotalpos / ptotalneg
#print( len(txt), ptotalpos,qp,pt,ptotalneg,qn,np,sep=",")
listacap = re.split(r"##", txt)

print("Cap,Nº carateres, totpos, quanpos, totneg, quanneg,palavras,rationeg")
n=0 
for cap in listacap:
    ptotalpos, qp,ptotalneg,qn,np= sentimento(cap)
    print( n,len(cap), ptotalpos,qp,ptotalneg,qn,np,Factor,sep =",")
    n=n+1


saida = "A _mulher_fatal_sent.csv"

with open(saida, "w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(["Cap", "Nº carateres", "totpos", "quanpos", "totneg", "quanneg", "palavras", "rationeg"])
    
    n = 0
    for cap in listacap:
        ptotalpos, qp, ptotalneg, qn, np = sentimento(cap)
        writer.writerow([n, len(cap), ptotalpos, qp, ptotalneg, qn, np, Factor])
        n += 1

print(saida)