import pyRofex
import pandas as pd
import matplotlib.pyplot as plt
from _datetime import datetime


pyRofex.initialize(user='juanichacho2557',
               password='gpovgB1!',
               account='sampleAccount',
               environment=pyRofex.Environment.REMARKET)


def buscarInstrumentos(c):

    l = len(c)

    a = listarInstrumentos()

    b = a['instruments']

    print(b)

    for i in b:
        if i['instrumentId']['symbol'][:l] == c:
            print(i['instrumentId']['symbol'])

def listarSegmentos():
    segments = pyRofex.get_segments()
    return segments

def listarInstrumentos():
    instruments = pyRofex.get_all_instruments()
    return instruments

def armarListadoDeTrades(a):
    trades = pyRofex.get_trade_history(ticker=a,
                                       start_date='2019-08-01',
                                       end_date='2019-08-15')

    return trades

def graficar(t):
    l = pd.DataFrame(t['trades'])[['price','datetime']]
    l.plot(x = 'datetime', y ='price' )
    plt.gcf().autofmt_xdate()
    plt.show()

def main():
    buscarInstrumentos('SO')
    print(armarListadoDeTrades('SOJ.ROSNov19'))
    graficar(armarListadoDeTrades('SOJ.ROSNov19'))


