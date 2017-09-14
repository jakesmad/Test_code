# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('C:\\Users\\Ludek\\Dropbox\\Private\\Python\\Test data\\ReportRaw_20170729.csv')
df['settledDate'] = pd.to_datetime(df['settledDate'],format='%d/%m/%Y %H:%M')

basicGroup = df.groupby(['settledDate','eventDesc','marketDesc',
                         'runnerDesc','MatchID','Day','Period',
                         'BetfairPath','HomeGoals',
                         'AwayGoals','HomeReds','AwayReds']).agg({'sizeSettled':sum,
                                                                    'profit':sum, 
                                                                    'Minute': min,
                                                                    'wsGap2': 'mean'}) 
helperGroup = df.groupby(['settledDate','eventDesc','marketDesc',
                         'runnerDesc','MatchID','Day','Period',
                         'BetfairPath','HomeGoals',
                         'AwayGoals','HomeReds','AwayReds'])

df['priceMatchedAvg'] = df['sizeSettled'] / helperGroup.sizeSettled.transform("sum") * df['priceMatched']
df['FairPriceAvg'] = df['sizeSettled'] / helperGroup.sizeSettled.transform("sum") * df['FairPrice']
priceSeries = helperGroup['priceMatchedAvg'].sum()
priceSeriesFair = helperGroup['FairPriceAvg'].sum()
priceDF = priceSeries.to_frame()
priceDFFair = priceSeriesFair.to_frame()

finalGroup = pd.concat([basicGroup, priceDF, priceDFFair], axis=1)
finalGroup = finalGroup.reset_index()
finalGroup = finalGroup.sort_values('settledDate', ascending=True)
finalGroup['InternalID'] =""           
finalGroup = finalGroup[['settledDate','eventDesc','marketDesc',
                         'runnerDesc','sizeSettled','profit','priceMatchedAvg','InternalID', 
                         'MatchID','Minute','FairPriceAvg','Day','Period','wsGap2',
                         'HomeGoals','AwayGoals','HomeReds','AwayReds','BetfairPath']]
finalGroup.to_csv('out.csv')




#gg = df.groupby(['eventDesc'])['priceMatched','sizeSettled'].max()
#print (gg)
#print(gg.priceMatched.max())
#for eventDesc in gg:
 #   print(eventDesc)
    #print(eventDesc_df)
#meanprice2 = df.groupby(key),["priceMatched"].mean()
#with open('C:\\Users\\Ludek\\Dropbox\\Private\\Python\\Test data\\test.csv',) as csvfile:
#    readcsv = csv.reader(csvfile, delimiter= ',')
#    for row in readcsv:
#        print(row)