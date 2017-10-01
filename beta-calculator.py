#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filename: beta-calculator
"""
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

def main():
    start = dt.datetime(2007,1,1)
    end = dt.datetime(2008,1,1)
    ticker = 'GS'
    
    beta = getBeta(ticker,start,end)
    print('Beta:', beta)

def getBeta(ticker,start,end):
#    returns beta value
    index = '^GSPC'

#    gets stock data for ticker and S&P500 as benchmark
    df = web.DataReader(ticker,'yahoo',start,end)
    bench = web.DataReader(index,'yahoo',start,end)
    
    total = pd.DataFrame()
    total[ticker]=df['Adj Close']
    total[ticker + ' Return']= total[ticker].pct_change()
    
    total[index]=bench['Adj Close']
    total[index+' Return']= total[index].pct_change()
        
    beta = (total[index+' Return'].cov(total[ticker + ' Return']))/total[index+' Return'].var()
   
    plot(total,index,ticker)
    return beta

def plot(df,index,ticker):
    fig,ax1 = plt.subplots()
    fig.set_figheight(4.5)
    fig.set_figwidth(6)
    
    plt.scatter(df[index+' Return'],df[ticker + ' Return'],c='k',alpha=0.7,marker=".")
    
    plt.grid()
    plt.xlabel(index+' Returns')
    plt.ylabel(ticker + ' Returns')
        
    plt.show()
    
if  __name__ =='__main__':main()
    
