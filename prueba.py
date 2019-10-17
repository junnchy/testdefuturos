import pyRofex
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from _datetime import datetime
import sys
from datetime import datetime
import pymongo
from pymongo import MongoClient
import json
from pymongo.errors import ConnectionFailure


pyRofex.initialize(user='juanichacho2557',
               password='gpovgB1!',
               account='sampleAccount',
               environment=pyRofex.Environment.REMARKET)


def buscarInstrumentos(c):

    l = len(c)

    a = getInstrumentos()

    print(type(a))

    b = a['instruments']

    print(b)

    for i in b:
        if i['instrumentId']['symbol'][:l] == c:
            print(i['instrumentId']['symbol'])



def listarSegmentos():
    segments = pyRofex.get_segments()
    return segments

def getInstrumentos():
    instruments = pyRofex.get_all_instruments()
    return instruments

def listarInstrumentos():
    instruments = pyRofex.get_all_instruments()
    for i in instruments['instruments']:
        print(i['instrumentId']['symbol'])


def getSimbolos():
    instruments = pyRofex.get_all_instruments()
    for i in instruments['instruments']:
        return (i['instrumentId']['symbol'])


def getListaSimbolos():
    instruments = pyRofex.get_all_instruments()
    lI = []
    for i in instruments['instruments']:
        lI.append(i['instrumentId']['symbol'])
    lI.sort()
    return (lI)

def armarListadoDeTrades(a):
    trades = pyRofex.get_trade_history(ticker=a,
                                       start_date='2019-08-01',
                                       end_date='2019-10-17')

    return trades

def armarTrades(a):
    trades = pyRofex.get_trade_history(ticker=a,
                                       start_date='2019-08-07',
                                       end_date='2019-09-02')

    return trades

def graficar(t):
    l = pd.DataFrame(t['trades'])[['price','datetime']]
    l.plot(x = 'datetime', y ='price' )
    plt.gcf().autofmt_xdate()
    plt.show()

def dbManager():
    "Connect to MongoDB"
    try:
        c = MongoClient(
            host="localhost",
            port=27017
        )
        print("Connected successfully")
    except ConnectionFailure:
        sys.stderr.write("Could not connet to MongoDB")
        sys.exit(1)

    db = c['rofex']

    return db

def cargarDolar(db, trade):
    #Reformar para que tome cualquier mercado
    print(DataFrame(trade['trades']))
    for i in trade['trades']:
        dolar_doc = {
            'price': i['price'],
            'size': i['size'],
            'datatime':i['datetime'],
            'servertime':i['servertime']
        }

        db.DOSep19.insert_one(dolar_doc)
        print ('Carga exitosa en el documento: ', dolar_doc)

def main():
    #buscarInstrumentos('SO')
    #a = armarListadoDeTrades('DOSep19')

    #graficar(armarListadoDeTrades('SOJ.ROSNov19'))
    #getInstrumentos()
    #listarInstrumentos()
    #db = dbManager()
    #cargarDolar(db, a)

    #buscarInstrumentos('DOSep19')
    print(armarTrades('DODic19'))
    #print(DataFrame(getListaSimbolos()))

main()
