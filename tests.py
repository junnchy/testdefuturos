import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import pyRofex

pyRofex.initialize(user='juanichacho2557',
               password='gpovgB1!',
               account='sampleAccount',
               environment=pyRofex.Environment.REMARKET)


def getListaSimbolos():
    instruments = pyRofex.get_all_instruments()
    lI = []
    for i in instruments['instruments']:
        lI.append(i['instrumentId']['symbol'])
    lI.sort()
    return (lI)


def main():
    simbolos = getListaSimbolos()
    arraysim = np.array(simbolos)
    print(arraysim)

main()


