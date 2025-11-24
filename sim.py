# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 20:05:56 2025

@author: Varad
"""

import math
import pandas as pd

inputs = []
outputs = []
outfreq = {}
TT = {}
Hfinal = 0
ins = 0
ous = " "
b = int(input("Enter base: "))
inp = int(input("Enter number of inputs: "))
out = int(input("Enter number of outputs: "))

for i in range(b**inp):
    temi = []
    for i in range(inp):
        I = int(input("Enter Input bit: "))
        temi.append(I)
    inputs.append(tuple(temi))
    temo = []
    for j in range(out):
        O = int(input("Enter Output bit: "))
        temo.append(O)
    outputs.append(tuple(temo))
    TT[tuple(temi)] = tuple(temo)
s = pd.Series(outputs)
fre = s.value_counts()

outfreq = fre.to_dict()

for j in outfreq:
    P = outfreq[j]/(b**inp)
    Hf = -(P * math.log(P,2))
    Hfinal = Hfinal + Hf

Hini = inp
Qmin = ((1.380*(10**-23)) * math.log(2,math.e) * 300) * (Hini-Hfinal)
print("Minimum Landauer heat per erased bit: ",Qmin, "J")

binp = False
c = input("Do You Want a real time simulation(y/n): ").lower()
if c == "y":
    binp = True
elif c == "n":
    binp = False
else:
    print("Please Enter A Valid Input")
while binp == True:
    rlinps = []
    rlouts = []
    print("==== I N P U T ======")
    for i in range(inp):
        inps = input(">> ")
        if inps == "":
            rlinps.append(0)
        elif inps == "*":
            rlinps.append(1)
        else:
            print("Please enter a valid input")
    for k in TT:
        if k == tuple(rlinps) :
            for i in TT[k] :
                rlouts.append(i)
    print("==== O U T ======")
    prl = 0
    for ct in outfreq:
        if ct == tuple(rlouts):
            prl = outfreq[ct]
    for l in rlouts:
        if l == 0:
            ous = ""
        else:
            ous = "*"
        print("[",ous, "]", end = " ")
        print("")
    print("Minimum theoretical heat dissipation for this logic operation: ")
    print(((1.380*(10**-23)) * math.log(2,math.e) * 300) * math.log(prl,2), "J")
    c = input("Try again?: (y/n) ").lower()
    if c == "y":
        binp = True
    elif c == "n":
        binp = False
    else:
        print("Please Enter A Valid Input")
    