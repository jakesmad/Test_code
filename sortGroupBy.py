
import pandas as pd

df = pd.read_csv('C:\\Users\\Ludek\\Dropbox\\Private\\Python\\Test data\\ReportRaw_20170729.csv')

df['settledDate'] = pd.to_datetime(df['settledDate'], format='%d/%m/%Y %H:%M')

basicGroup = df.groupby(['settledDate', 'eventDesc', 'marketDesc'
                         ]).agg({'sizeSettled': sum,
                                 'profit': sum,
                                 'Minute': min,
                                 'wsGap2': 'mean'})
basicGroup = basicGroup.reset_index()
basicGroup['x'] = ""
basicGroup['xx'] = ""
basicGroup = basicGroup[['settledDate', 'xx', 'eventDesc', 'profit', 'x']]
basicGroup = basicGroup.sort_values('settledDate', ascending=True)
print(basicGroup[:5])

helperGroup = df.groupby(['settledDate', 'eventDesc', 'marketDesc',
                          'runnerDesc', 'MatchID', 'Day', 'Period',
                          'BetfairPath', 'HomeGoals',
                          'AwayGoals', 'HomeReds', 'AwayReds'])
df['priceMatchedAvg'] = df['sizeSettled'] / helperGroup.sizeSettled.transform("sum") * df['priceMatched']
priceSeries = helperGroup['priceMatchedAvg'].sum()
priceDF = priceSeries.to_frame()
priceDF.reset_index()


